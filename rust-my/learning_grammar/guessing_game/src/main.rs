//! 该程序是一个猜数字游戏，玩家需要猜一个数字，程序会提示玩家猜大了还是猜小了，直到玩家猜中为止。
//!
//! 主要实现的功能有：
//! - 随机生成一个数字作为答案 (为了调试方便，该数字在最开始公布)
//! - 让玩家输入一个数字，并判断输入的数字是否正确
//! - 输出提示信息，提示玩家猜大了还是猜小了
//! - 循环以上流程，直到玩家猜中为止

use std::cmp::Ordering;
use std::io;

use rand::Rng;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1, 101);
    println!("The secret number is: {}", secret_number);

    loop {
        println!("Guessing Number Game");
        println!("Please enter a number between 1 and 100");

        let mut guess = String::new();
        io::stdin().read_line(&mut guess).expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => { println!("Too small!"); }
            Ordering::Greater => { println!("Too large!"); }
            Ordering::Equal => {
                println!("Congratulations! You guessed the number!");
                break;
            }
        }
    }
}
