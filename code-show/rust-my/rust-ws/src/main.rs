fn main() {
    let mut s = String::from("hello world from the rust programming language");

    // usize 在 string 的上下文才有意义
    let word_start = first_word(&s);
    println!("The first word starts at index {}", word_start);

    s.clear();  // 清空s ""
    // word_start 依然是5 但s是空的
    // 后续尝试对s使用word_start 变量获取值会报错

}

fn first_word(s: &String) -> usize {
    let bytes = s.as_bytes();  // 将字符串转化为字节数组

    // 遍历字节数组，找到第一个空格的位置
    for (i, &item) in bytes.iter().enumerate() {  // 字节数组 迭代器 元组返回
        if item == b' ' {  
            return i;
        }
    }

    s.len()
}