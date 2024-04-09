//! 该程序用于从zip文件中解压出所有文件
//!
//! 示例：cargo run data/example.zip
//!
//! 实现思路：
//! 1. 读取命令行参数，获取zip文件名
//! 2. 打开zip文件，读取zip文件内容
//! 3. 遍历zip文件内容，解压文件到指定目录
//! 4. 设置文件权限
//! 5. 输出解压结果
//!
//! 注意：
//! 1. 该程序依赖于zip库，需要在Cargo.toml中添加zip库依赖
//! 2. 该程序仅支持解压zip文件，不支持压缩文件
//! 3. 该程序仅支持解压文件到指定目录，不支持解压到内存
//! 4. 该程序目前仅支持解压到项目的根目录，不支持解压到指定目录

use std::fs;
use std::io;
use std::path::Path;

fn main() {
    std::process::exit(logic_main());  // 调用 logic_main() 函数并退出程序
}


fn logic_main() -> i32 {
    let args: Vec<_> = std::env::args().collect();  // 获取命令行参数
    if args.len() < 2 {
        println!("Usage: {} <filename>", args[0]);
        return 1;
    }

    // 参数正确传递
    let zip_filename = Path::new(&args[1]);  // 获取文件名
    let file = fs::File::open(zip_filename).unwrap();  // 打开文件
    let mut archive = zip::ZipArchive::new(file).unwrap();  // 读取zip文件 可变存档

    // 根据存档一个个地解压文件
    for i in 0..archive.len() {
        let mut file = archive.by_index(i).unwrap();  // 获取文件
        let output_path = match file.enclosed_name() {  // 获取文件名
            Some(path) => path.to_owned(),
            None => continue,
        };

        // 打印文件信息
        {
            let comment = file.comment();  // 获取注释
            if !comment.is_empty() {  // 注释不为空
                println!("File {} comment: {}", i, comment);
            }
        }

        // 如果文件名以/结尾 则创建目录 (否则解压文件)
        if (*file.name()).ends_with('/') {
            println!("File {} extracted to \"{}\"", i, output_path.display());
            fs::create_dir_all(&output_path).unwrap();  // 创建目录
        } else {
            println!("File {} extracted to \"{}\" ({} bytes)", i, output_path.display(), file.size());

            // 检查父级目录
            if let Some(p) = output_path.parent() {
                if !p.exists() {
                    fs::create_dir_all(p).unwrap();  // 创建辅机目录
                }
            }

            let mut outfile = fs::File::create(&output_path).unwrap();  // 创建outfile
            io::copy(&mut file, &mut outfile).unwrap();  // 复制文件到outfile 即解压文件操作
        }

        // 设置权限 (否则解压的文件权限将会丢失)
        #[cfg(unix)]
        {
            use std::os::unix::fs::PermissionsExt;
            if let Some(mode) = file.unix_mode() {
                fs::set_permissions(&output_path, fs::Permissions::from_mode(mode)).unwrap();
            }
        }
    }
    0
}