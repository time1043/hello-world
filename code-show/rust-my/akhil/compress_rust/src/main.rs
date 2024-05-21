//! 该程序用于压缩文件。
//!
//! 示例：cargo run data/book.pdf data/compressed_file.pdf
//!
//! use介绍：
//! - flate2 crate 用于压缩文件。
//! - copy 函数用于复制文件。
//! - GzEncoder 用于创建 GzEncoder 对象。
//! - Compression::default() 用于设置压缩级别。
//! - finish 函数用于完成压缩。
//! - metadata 函数用于获取文件大小。
//! - Instant 用于记录时间。

extern crate flate2;

use std::env::args;
use std::fs::File;
use std::io::{BufReader, copy};
use std::time::Instant;

use flate2::Compression;
use flate2::write::GzEncoder;

fn main() {
    // 期待三个参数
    if args().len() != 3 {
        eprintln!("Usage: `source` `target`");
        return;
    }

    let mut input = BufReader::new(File::open(args().nth(1).unwrap()).unwrap());  // 打开源文件
    let output = File::create(args().nth(2).unwrap()).unwrap();  // 打开目标文件
    let mut encoder = GzEncoder::new(output, Compression::default());  // 创建 GzEncoder 对象
    let start = Instant::now();  // 记录开始时间

    copy(&mut input, &mut encoder).unwrap();  // 复制文件
    let output = encoder.finish().unwrap();  // 压缩文件

    println!("Source len: {:?}", input.get_ref().metadata().unwrap().len()); // 打印源文件大小
    println!("Target len: {:?}", output.metadata().unwrap().len());  // 打印压缩后的文件大小
    println!("Elapsed time: {:?}s", start.elapsed());  // 打印压缩和复制所需的时间 用户提示
}
