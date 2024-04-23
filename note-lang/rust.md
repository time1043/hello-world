# rust

- 语言的比较

  java：爆内存

  go：

  rust：





# rust (个性)

## 速通基础

### 前言

#### 背景

- rust：新的编程语言

  (rust有c的性能、bug在编译时消灭)

  运行速度快、内存安全、更好地利用多处理器

  Functional、zero-cost

- 编程语言比较

  `c`、`c++`：性能好；但类型系统和内存都不太安全

  `java`、`c#`：有垃圾搜集器GC，保证内存安全；但性能不行

  `rust`：安全、无需GC、已于维护调式、代码安全且高效

- rust的应用领域

  高性能webService、webAssembly、命令行工具

  网络编程、嵌入式设备、系统编程



- 参考课程

  [tsinghua 程序设计 (rust)](https://lab.cs.tsinghua.edu.cn/rust/)、[tsinghua 操作系统 (rust)](https://rcore-os.cn/rCore-Tutorial-Book-v3)、[tsinghua 软件工程](https://lab.cs.tsinghua.edu.cn/software-engineering/basic/web/)、[tsinghua 实验物理的大数据方法 (python)](https://hep.tsinghua.edu.cn/~orv/teaching/physics-data/)

  [程序君的 Rust 培训](https://www.bilibili.com/video/BV19b4y1o7Lt/)；[Rust 项目实操 - xdiff](https://www.bilibili.com/video/BV1dG4y167M9/)；[xdiff源码](https://github.com/Tubitv/xdiff)、[Rust 项目实操 - 预订系统](https://www.bilibili.com/video/BV1aV4y1L72b/)；
  
  [Learn Rust Programming - Complete Course (freeCodeCamp.org)](https://www.youtube.com/watch?v=BpPEoZW5IiY)、
  
  [50 Rust Projects - New Playlist Announcement](https://www.youtube.com/watch?v=qru3L4BvrOU&list=PL5dTjWUk_cPYuhHm9_QImW7_u4lr5d6zO)、[50 源码](https://github.com/AkhilSharma90/Rust-Compress)；
  
  [基于rust语言的小项目](https://www.bilibili.com/video/BV1v64y1R7mq/)
  
- 参考资料

  [rust程序设计语言](https://www.rustwiki.org.cn/zh-CN/book/foreword.html)、[CS198Rust](http://cis198-2016s.github.io/)、[RustLanguageCheatSheet](https://cheats.rs/)\

  [埼玉大学 rust](https://www.aise.ics.saitama-u.ac.jp/~gotoh/RustOnUbuntu2004.html)
  
- 官网

  [rust 官网](https://www.rust-lang.org/)、[crates](https://crates.io/)



- 学习规划

  基础入门：基础语法

  进阶：并发编程

  算法：

  web开发：原生、Actix、Rocket





#### 快速入门

- [安装rust](https://www.rust-lang.org/)、[playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2021)

- win

  ```
  # 更新与卸载rust
  rustup update
  rustup self uninstall
  
  # 安装验证
  rustc --verison
  
  # 本地文档
  rustup doc
  
  ```

- Windows Subsystem for Linux

  ```
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  ```

  



- 开发工具：vscode (提示弱)

  rust插件

  ```
  cd /d/code2/hello-world/rust/learning_grammar
  mkdir hello_world
  cd h*
  code .  # vscode打开
  ```

  hello_world.rs

  ```rust
  fn main() {
      println!("hello world");
  }
  ```
  
  rustc (编译工具 用得少)

  ```
  move hello_world.rs main.rs
  
  rustc main.rs  # 编译 简单的rs程序
  
  .\main.exe  # win运行
  ./main  # linux运行
  ```

- 开发工具：IDEA

  rust插件

  



- Cargo：rust的构建系统和包管理工具

  构建代码、下载依赖的库、构建这些库
  
  ```
  # 查看版本信息
  cargo --verison  # cargo 1.76.0 (c84b36747 2024-01-18)
  
  # 创建项目
  cargo new hello_cargo
  
  cargo build
  cargo build --release  # 为发布构建 编译优化
  cargo run  # 编译代码 + 执行结果
  cargo check  # 检查代码 确保通过编译  快
  
  ```
  
  



#### 猜数游戏

- 语法点

  let、match等方法

  相关的函数

  外部的crate (包 库)



- 一次猜测

  ```
  # 建项目
  cargo new guessing_game
  code .
  ```

  ```rust
  use std::io;
  
  fn main() {
      println!("Guessing Number Game");
      println!("Please enter a number between 1 and 100");
  
      let mut guess = String::new();  // immutable -> mut
      io::stdin().read_line(&mut guess).expect("Failed to read line");  // io::Result  Ok, Err
      println!("You guessed: {}", guess);
  }
  
  ```
  
  ```
  cargo run
  ```
  
- 生成神秘数字

  https://crates.io/crates/rand

  D:\code\hyz-code-rust\learning_grammar\guessing_game\Cargo.toml

  ```toml
  [dependencies]
  rand = "0.3.14"
  ```

  ```rust
  use std::io;  // prelude 预导入模块
  use rand::Rng;  // trait
  
  fn main() {
      println!("Guessing Number Game");
      println!("Please enter a number between 1 and 100");
  
      let mut guess = String::new();
      io::stdin().read_line(&mut guess).expect("Failed to read line");  
      println!("You guessed: {}", guess);
  
      let secret_number = rand::thread_rng().gen_range(1, 101);  // i32 u32 u64
      println!("The secret number is: {}", secret_number);
  }
  
  ```
  
- 比较猜测数字与神秘数字

  ```rust
  use std::cmp::Ordering;
  use std::io;
  
  use rand::Rng;
  
  fn main() {
      println!("Guessing Number Game");
      println!("Please enter a number between 1 and 100");
  
      let mut guess = String::new();
      io::stdin().read_line(&mut guess).expect("Failed to read line");
      println!("You guessed: {}", guess);
  
      let secret_number = rand::thread_rng().gen_range(1, 101);
      println!("The secret number is: {}", secret_number);
  
      let guess: u32 = guess.trim().parse().expect("Please type a number!");  // shadow
      match guess.cmp(&secret_number) {
          Ordering::Less => { println!("Too small!"); } // arm
          Ordering::Equal => { println!("Congratulations! You guessed the number!"); }
          Ordering::Greater => { println!("Too large!"); }
      }
  }
  
  ```

- 允许多次猜测

  ```rust
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
          println!("You guessed: {}", guess);
  
          let guess: u32 = guess.trim().parse().expect("Please type a number!");
          match guess.cmp(&secret_number) {
              Ordering::Less => { println!("Too small!"); }
              Ordering::Equal => { println!("Congratulations! You guessed the number!"); }
              Ordering::Greater => { println!("Too large!"); }
          }
      }
  }
  
  ```

- 优化

  输入正确答案正常结束程序

  输入非数字程序奔溃 (健壮性)

  ```rust
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
  
  ```
  
  



### 通用的编程概念

- 概览

  变量与可变性

  数据类型：标量类型、复合类型

  函数

  注释

  控制流



#### 变量

- 变量与可变性

  声明变量使用 `let` 关键字

  默认情况下，变量是不可变的Immutable

  声明变量时，在变量前加上 `mut`，则变量可变

  ```
  cargo new variables
  code .
  ```

  ```rust
  const MAX_POINTS: u32 = 100_000;
  
  fn main() {
      println!("Hello, world!");
  
      let mut x = 5; // i32  mut
      println!("The value of x is {}", x);
  
      x = 6; // cannot assign twice to immutable variable
      println!("The value of x is {}", x);
  }
  
  ```

- 变量与常量

  常量 `constant` 在绑定值后也是不可变的，但是其与不可变的变量有很多区别：

  - 不可以使用 `mut` ，常量永远都是不可变的
  - 声明常量使用 `const` 关键字，其类型必须被标注
  - 常量可在任何作用域内进行声明，包括全局作用域
  - 常量只可以绑定到常量表达式，无法绑定到函数的调用结果、无法绑定到只能在运行时才能计算出的值

  在程序运行期间，常量在其声明的作用域内一直有效

  命名规范：全大写、下划线分隔

- 隐藏shadowing

  可以使用相同的名字声明新的变量，新的变量就会shadowing之前声明的同名变量

  shadowing和把变量标记为 `mut` 是不一样的：

  - 使用 `let` 声明的同名新变量，其类型可以与之前不同

  ```rust
  fn main() {
      let x = 5;
      // x = x + 1;  // err
      let x = x + 1; // shadowing
      println!("The value of x is {}", x);
  
      // let mut spaces = "    ";
      // spaces = spaces.len();  // expected `&str`, found `usize`
  
      let spaces = "    "; // str
      let spaces = spaces.len(); // usize
      println!("{}", spaces);
  }
  
  ```

  

#### 数据类型

- 数据类型

  标量类型和复合类型

  rust是静态编译语言，在编译时必须知道所有变量的类型

  - 基于使用的值，编译器通常能够推断出它的具体类型

  - 但如果可能的类型比较多，则必须添加类型标注，否则编译器报错 (例子)

  ```rust
  fn main() {
      let guess:u32 = "42".parse().expect("Not a number");  // i32 u32
      println!("{}", guess);
  }
  
  ```

  

- 标量类型

  一个标量类型代表一个单个的值

  rust有四个主要的标量类型：整数、浮点、布尔、字符

  - 整数：有符号（如`i8`, `i16`, `i32`, `i64`, `i128`）和无符号（如`u8`, `u16`, `u32`, `u64`, `u128`）、两个特殊的整数类型：`isize`和`usize`

    整数的字面值：`98_222` (Decimal)、`0xff` (Hex)、`0o77` (Octal)、`0b111_0000` (Binary)、`b'A'` (Byte u8 only)

    整数溢出：在调试模式下编译，rust会检查整数溢出，若溢出，程序在运行时就会panic；在发布模式下编译，rust不会检查，若溢出执行环绕操作

  - 浮点：`f32`和`f64`(默认)、IEEE-754

  ```rust
  fn main() {
      let x = 2.0;  // f64
      let y:f32 = 3.0;  // f32
  
      let t = true;
      let f: bool = false; // with explicit type annotation
  
      let c = 'z';
      let z = 'ℤ';
      let heart_eyed_cat = '😻';
  }
  
  ```

  数值运算

  加减乘除余

  ```rust
  fn main() {
      // addition
      let sum = 5 + 10;
  
      // subtraction
      let difference = 95.5 - 4.3;
  
      // multiplication
      let product = 4 * 30;
  
      // division
      let quotient = 56.7 / 32.2;
      let floored = 2 / 3; // Results in 0
  
      // remainder
      let remainder = 43 % 5;
  }
  
  ```

  

- 复合数据类型

  **复合类型**（compound type）可以将多个值组合成一个类型。

  Rust 有两种基本的复合类型：元组（tuple）和数组（array）。

- tuple：

  将多个类型的多个值放在一个类型里

  长度固定，一旦声明无法修改

  创建、获取其元素值、访问其元素

  ```rust
  fn main() {
      // tuple 创建
      let tup: (i32, f64, u8) = (500, 6.4, 1);
      
      // 获取元素值：模式匹配 解构destructure
      let (x, y, z) = tup;
      println!("{}, {}, {}", x, y, z);
      
      // 访问其元素：点索引
      println!("{}, {}, {}", tup.0, tup.1, tup.2);
  
  }
  
  ```

- array：

  可以将多个值放在一个类型里

  但每个元素的类型必须相同、长度固定

  类型：`[类型; 长度]`

  创建：`let a: [i32; 5] = [3; 5];`

  访问：索引 `a[1]`

  when：**将数据存放在stack**而非heap、有固定数量

  (vetor：长度可变、推荐)

  ```rust
  fn main() {
      // array 创建
      let a: [i32; 5] = [3; 5];  // [初始值; 长度] [3,3,3,3,3]
      let months = [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December",
      ];
      println!("{}", a[1]);
  
      let index = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23];
      println!("{}", index[2]);  // cargo build  Compiling Finished
      println!("{}", months[index[2]]);  // runtime panicked
  
      // vector
  }
  
  ```
  
  

#### 函数

- 函数

  声明函数用 `fn` 关键字

  函数和变量的命名规范：snake case (全小写、下划线隔开)

  ```rust
  fn main() {
      println!("hello world");
      another_function();
  }
  
  fn another_function() {
      println!("Another function")
  }
  
  ```
  
- 函数的参数

  parameters (定义时)、arguments (调用时传入)

  在函数的签名里，必须声明每个参数的类型

  ```rust
  fn main() {
      println!("hello world");
      another_function(5, 4); // arguments
  }
  
  fn another_function(x: i32, y: i32) { // parameters
      println!("the value of x is: {}", x);
      println!("the value of y is: {}", y);
  }
  
  ```
  
- 函数体中的语句*statement*和表达式*expression*

  函数体由一系列语句组成，可选的由一个表达式结束

  rust是一个基于表达式的语言

  *statement* 是执行一些 **动作** 的指令    如：`...;` // ()

  *expression* 会计算产生一个 **值**    如：`6 + 6`、`println!(...)`、`{...}`

- 函数的定义也是语句

  语句不返回值，所以不可以用let将一个语句赋给一个变量

  ```rust
  fn main() {
      let x = 6 + 6;
      println!("the value of x is {}", x);
      let y = {
          let x = 1;
          x + 3
      };
      println!("the value of y is {}", y)
  }
  
  ```
  
- 函数的返回值
  
  在`->`符号后边声明函数返回值的类型，但是不可以为返回值命名

  在Rust里面，返回值就是函数体里面**最后一个表达式的值**

  若想提前返回，需使用 `return` 关键字，并指定一个值

  - 大多数函数都是默认使用最后一个表达式最为返回值

  ```rust
  fn main() {
      let x = plus_five(1);
      println!("the value of x is {}", x);
  }
  
  fn plus_five(x: i32) -> i32 {
      x + 5
  }
  
  ```
  
  
  
- 注释

  单行注释、多行注释、文档注释

  ```rust
  /* multiline comment
  multiline comment */
  fn main() {
      let x = plus_five(1);
      println!("the value of x is {}", x);
  }
  
  // This is a function
  fn plus_five(x: i32) -> i32 {
      x + 5
  }
  
  ```

  

#### 控制流

- 控制流：条件分支 (if)

  if表达式：通过条件(bool类型)来执行不同的代码分支arm、else

  多个条件分支，最好用match重构

  ```rust
  fn main() {
      let number = 6;
  
      if number % 4 == 0 {
          println!("number is divisible by 4");
      } else if number % 3 == 0 {
          println!("number is divisible by 3");
      } else if number % 2 == 0 {
          println!("number is divisible by 2");
      } else {
          println!("number is not divisible by 4, 3, or 2");
      }
  
      match (number % 4, number % 3, number % 2) {
          (0, _, _) => println!("number is divisible by 4"),
          (_, 0, _) => println!("number is divisible by 3"),
          (_, _, 0) => println!("number is divisible by 2"),
          (_, _, _) => println!("number is not divisible by 4, 3, or 2"),
      }
  }
  
  ```

  if表达式可以放在 `=` 右边

  ```rust
fn main() {
      let condition = true;
      let number = if condition { 5 } else { 6 };
      println!("the value of number is {}", number);
  }
  
  ```
  
  

- 控制流：循环 (loop、while、for)

  `loop` 关键字告诉 Rust 一遍又一遍地执行一段代码直到你明确要求停止 (`break`)

  ```rust
  fn main() {
      let mut counter = 0;
      
      let result = loop {
          counter += 1;
          println!("counter += 1;");
  
          if counter == 10 {
              break counter * 2;
          }
      };
      println!("the result is {}", result)
  }
  
  ```

  `while` 条件循环：每次执行循环体之前都判断一次条件

  ```rust
  fn main() {
      let mut number = 3;
  
      while number != 0 {
          println!("{}!", number);
          number = number - 1;
      }
      println!("left off")
  }
  
  ```

  `for` 循环：遍历集合

  ```rust
  fn main() {
      let a = [10, 324, 5325, 24232, 532];
      let mut index = 0;
  
      // 低效 易出错
      while index < 5 {
          println!("the value is {}", a[index]);
          index = index + 1
      }
  
      // 紧凑
      for element in a.iter() {
          // element:&i32  没有复制 而是直接引用
          println!("the value is {}", element);
      }
      println!("lefr off");
  }
  
  ```

- Range

  标准库提供

  指定开始数字和结束数字，Range可以生成他们之间的数字(包前不包后)

  rev方法可实现反转

  ```rust
  fn main() {
      for number in (1..4).rev() {
          println!("{}!",number)
      }
      println!("lefr off");
  }
  
  ```
  
  



### 所有权

#### 所有权规则、内存和分配

- 所有权*ownership*：使得rust无需GC，就可以保证内存安全

  **rust把内存管理工作提前到编译时**

- Rust的核心特性就是所有权

  所有程序在运行时都必须管理它们使用计算机内存的方式

  - 有些语言有垃圾收集机制，在程序运行时，它们会不断地寻找不再使用的内存
  - 在其他语言中，程序员必须显式地分配和释放内存

  Rust 采用了第三种方式:

  - 内存是通过一个所有权系统来管理的，其中包含一组编译器在编译时检查的规则。
  - 当程序运行时，所有权特性不会减慢程序的运行速度。

- 栈内存Stack vs 堆内存Heap

  在像 Rust 这样的系统级编程语言里，一个值是在stack上还是在 heap 上对语言的行为和你为什么要做某些决定是有更大的影响的。

  在你的代码运行的时候，Stack和Heap 都是你可用的内存，但他们的结构很不相同。

  

- **存储数据**

  Stack 按值的接收顺序来存储，按相反的顺序将它们移除 (后进先出，LIFO)

  - 添加数据叫做压入栈

  - 移除数据叫做弹出栈

  所有存储在 Stack上的数据必须拥有已知的固定的大小

  - 编译时大小未知的数据或运行时大小可能发生变化的数据必须存放在heap上

  Heap 内存组织性差一些:

  - 当你把数据放入 heap 时，你会请求一定数量的空间

  - 操作系统在 heap 里找到一块足够大的空间，把它标记为在用，并返回一个指针，也就是这个空间的地址

  - 这个过程叫做在 heap 上进行分配，有时仅仅称为"分配"

- 把值压到 stack 上不叫分配

  因为指针是已知固定大小的，可以把指针存放在 stack上。

  - 但如果想要实际数据，你必须使用指针来定位。

  把数据压到 stack 上要比在 heap 上分配快得多: 

  - 因为操作系统不需要寻找用来存储新数据的空间，那个位置永远都在stack的顶端

  在 heap 上分配空间需要做更多的工作: 

  - 操作系统首先需要找到一个足够大的空间来存放数据，然后要做好记录方便下次分配

  

- **访问数据**

  访问 heap 中的数据要比访问 stack 中的数据慢，因为需要通过指针才能找到heap 中的数据

  - 对于现代的处理器来说，由于缓存的缘故，如果指令在内存中跳转的次数越少，那么速度就越快

  如果数据存放的距离比较近，那么处理器的处理速度就会更快一些(stack上)

  如果数据之间的距离比较远，那么处理速度就会慢一些(heap上)

  - 在 heap 上分配大量的空间也是需要时间的

  

- **函数调用**

  当你的代码调用函数时，值被传入到函数(也包括指向heap的指针)。函数本地的变量被压到 stack上。当函数结束后，这些值会从stack上弹出



- 所有权解决的问题:

  - 跟踪代码的哪些部分正在使用 heap 的哪些数据

  - 最小化 heap 上的重复数据量

  - 清理 heap 上未使用的数据以避免空间不足。

  一旦你懂的了所有权，那么就不需要经常去想 stack或 heap 了。

  但是知道管理 heap 数据是所有权存在的原因，这有助于解释它为什么会这样工作。



- 所有权规则

  每个值都有一个变量，这个变量是该值的所有者

  每个值同时只能有一个所有者

  当所有者超出作用域(scope)时，该值将被删除

  ```rust
  fn main() {
      // s不可用
      let s = "hello"; // s可用 可操作
  } // s作用域结束 s不再可用
  
  ```

  

- String

  String 比那些基础标量数据类型更复杂

  字符串字面值：程序里手写的那些字符串值。它们是不可变的

  Rust还有第二种字符串类型：String

  - 在 heap上分配。能够存储在编译时未知数量的文本

- 创建String类型的值

  可以使用 from 函数从字符串字面值创建出 String 类型

  `let s = String::from("hello");`

  - `::` 表示 from 是 String 类型下的函数

  这类字符串是可以被修改的(例子)

  ```rust
  fn main() {
      let mut s = String::from("hello");
      s.push_str(", world");
      println!("{}", s)
  }
  
  ```
  
- 为什么 String 类型的值可以修改，而字符串字面值却不能修改?

  - 因为它们处理内存的方式不同

- 内存和分配

  字符串字面值，在编译时就知道它的内容了，其文本内容直接被硬编码到最终的可执行文件里

  - 速度快、高效。是因为其不可变性。

  String 类型，为了支持可变性，需要在 heap 上分配内存来保存编译时未知的文本内容:

  - 操作系统必须在运行时来请求内存

    这步通过调用 String::from 来实现

  - 当用完 String 之后，需要使用某种方式将内存返回给操作系统

    这步，在拥有 GC 的语言中，GC会跟踪并清理不再使用的内存

    没有 GC，就需要我们去识别内存何时不再使用，并调用代码将它返回。

    - 如果忘了，那就浪费内存。
- 如果提前做了，变量就会非法
    - 如果做了两次，也是 Bug。必须一次分配对应一次释放
    
    
  Rust采用了不同的方式：对于某个值来说，当拥有它的变量走出作用范围时，内存会立即自动的交还给操作系统。（例子）
  
    - 当变量走出作用域时，会自动调用drop函数

  

- 变量和数据交互的方式：移动Move

  多个变量可以与同一个数据使用一种独特的方式来交互

  `let x=5; let y = X;`

  整数是已知且固定大小的简单的值，这两个5被压到了stack中

- string版本

  `let s1 = String::form("hello"); let s2 = s1;`

  一个String 由3部分组成: 

  - 一个指向存放字符串内容的内存的指针

  - 一个长度

  - 一个容量

  上面这些东西放在 stack 上

  存放字符串内容的部分在 heap上

  长度len，就是存放字符串内容所需的字节数

  容量 capacity 是指 String 从操作系统总共获得内存的总字节数

  

- 当把 s1 赋给 s2，String 的数据被复制了一份

  - 在stack上复制了一份指针、长度、容量

  - 并没有复制指针所指向的 heap 上的数据

  当变量离开作用域时，Rust会自动调用drop 函数，并将变量使用的heap 内存释放。

  当s1、s2离开作用域时，它们都会尝试释放相同的内存: 

  - 二次释放(double free) bug

- 为了保证内存安全:

  - Rust 没有尝试复制被分配的内存

  - Rust 让 s1 失效。

    当s1离开作用域的时候，Rust不需要释放任何东西

  试试看当s2创建以后再使用s1是什么效果(例子)

  ```rust
  fn main() {
      let s1 = String::from("hello");
      let s2 = s1; // s1赋值给s2后 s1就失效了  值的移动
  
      // println!("{}", s1); // value borrowed here after move
  }
  
  ```
  
- 浅拷贝(shallow copy)

  深拷贝(deep copy)

  你也许会将复制指针、长度、容量视为浅拷贝，但由于Rust让s1失效了，所以我们用一个新的术语: 移动(Move)

  隐含的一个设计原则: Rust不会自动创建数据的深拷贝

  - 就运行时性能而言，任何自动赋值的操作都是廉价的

  

- 变量和数据交互的方式: 克隆(Clone)

  如果真想对 heap 上面的 String 数据进行深度拷贝，而不仅仅是 stack 上的数据可以使用 clone方法 (以后再细说，先看个例子)

  ```rust
  fn main() {
      let x = 5; // 整数类型 编译时确定大小 存stack
      let y = x; // 复制 快速 没有理由去阻止x保持有效 (深度拷贝和浅拷贝没区别)
      println!("{}, {}", x, y)
  }
  
  ```

- Stack上的数据: 复制

  (例子)

  Copy trait，可以用于像整数这样完全存放在 stack 上面的类型

  如果一个类型实现了 Copy 这个 trait，那么旧的变量在赋值后仍然可用如果一个类型或者该类型的一部分实现了Drop trait，那么Rust 不允许让它再去实现 Copy trait 了

- 一些拥有 Copy trait 的类型

  任何简单标量的组合类型都可以是 Copy 的

  任何需要分配内存或某种资源的都不是 Copy 的

  一些拥有 Copy trait 的类型:

  - 所有的整数类型，例如u32

  - bool

  - char

  - 所有的浮点类型，例如f64

  - Tuple(元组)，如果其所有的字段都是 Copy 的

    (i32,i32)是

    (i32, String)不是

  



#### 所有权与函数

- 所有权与函数

  在语义上，将值传递给函数和把值赋值给变量都是类似的

  - 将值传递给函数将发生移动或复制

  ```rust
  fn main() {
      let s = String::from("hello world");
      take_ownership(s);  // 移动 自此以后s不再有效
  
      let x = 5;
      makes_copy(x);  // i32实现copy 函数传入的是x的副本 x后面有效
      println!("x: {}", x)
  }
  
  fn take_ownership(some_string: String) {  // 移动
      println!("{}", some_string);
  }  // drop
  
  fn makes_copy(some_string: i32) {  // 拷贝的副本
      println!("{}", some_string);
  }
  
  ```

  

  返回值与作用域

  函数在返回值的过程中也会发生所有权的转移

  一个变量的所有权总是遵循同样的模式: 

  - 把一个值赋给其它变量时就会发生移动
  - 当一个包含 heap 数据的变量离开作用域时，它的值就会被 drop 函数清理，除非数据的所有权移动到另一个变量上了

  ```rust
  fn main() {
      let s1 = gives_ownership();
  
      let s2 = String::from("hello");
      let s3 = takes_and_gives_back(s2); // s2移动至函数里
  }
  
  fn gives_ownership() -> String {
      let some_string = String::from("yours");
      some_string // 返回值 移动至 main的s1
  }
  
  // 取得了string所有权、并将结果返回
  fn takes_and_gives_back(a_string: String) -> String {
      a_string // 返回值 移动至 main的s3
  }
  
  ```

  

  如何让函数使用某个值，但不获得所有权？

  麻烦的做法

  针对这一场景，rust有一特性，即引用reference

  ```rust
  fn main() {
      let s1 = String::from("hello");
  
      let (s2, len) = calculate_length(s1); // s1的值给该函数使用 所有权用完还回来
      println!("The length of '{}' is {}.", s2, len);
  }
  
  fn calculate_length(s: String) -> (String, usize) {
      let length = s.len();
      (s, length) // s所有权 原封不动回去
  }
  
  ```

  

#### 引用和借用

- 引用和借用

  `&` 表示**引用**：允许你引用某些值，而不取得其所有权

  ```rust
  fn main() {
      let s1 = String::from("hello");
      let len = calculate_length(&s1); // 没有移动s1的所有权 &s1传引用
  
      println!("The length of '{}' is {}.", s1, len);
  }
  
  fn calculate_length(s: &String) -> usize {
      s.len()
  } // 未拥有所有权 不执行销毁
  
  ```

  

  把引用作为函数参数的这个行为叫做**借用**

  是否可以修改借用的东西？NO

  和变量一样，引用默认也是不可变的

  ```rust
  fn main() {
      let s1 = String::from("hello");
      let len = calculate_length(&s1); 
  
      println!("The length of '{}' is {}.", s1, len);
  }
  
  fn calculate_length(s: &String) -> usize {
      // s.push_str(", world");  // cannot borrow `*s` as mutable, as it is behind a `&` reference
      s.len()
  }
  
  ```

  

  可变引用

  重要的限制：在特定作用域内，对某一块数据，只能有一个可变的引用

  - 好处：在编译时防止数据竞争

  ```rust
  fn main() {
      let mut s1 = String::from("hello"); // 可变变量
      let len = calculate_length(&mut s1); // 可变引用
  
      println!("The length of '{}' is {}.", s1, len);
  }
  
  fn calculate_length(s: &mut String) -> usize {
      s.push_str(", world");
      s.len()
  } 
  
  ```

  ```rust
  fn main() {
      let mut s = String::from("hello");
  
      let r1 = &mut s;
      let r2 = &mut s;  // cannot borrow `s` as mutable more than once at a time
  
      println!("{}, {}", r1, r2);
  }
  
  ```

  

  以下每种情况都会发生数据竞争：

  两个或多个指针同时访问同一个数据

  至少有一个指针用于写入数据

  没有使用任何机制来同步对数据的访问

  (运行时很难发现、rust在编译时就避免)

  

  可以通过创建新的作用域，来允许非同时的创建多个可变引用

  ```rust
  fn main() {
      let mut s = String::from("hello");
  
      {
          let r1 = &mut s;
      } // r1 在这里离开了作用域，所以我们完全可以创建一个新的引用
  
      let r2 = &mut s;
  }
  
  ```

  

  另外一个限制：不可以同时拥有一个可变引用和一个不可变引用 (可变引用改变值 不可变引用值不变 矛盾打架)

  多个不可变引用是可以的

  ```rust
  fn main() {
      let mut s = String::from("hello");
  
      let r1 = &s; // 没问题
      let r2 = &s; // 没问题
      let r3 = &mut s; // 大问题 cannot borrow `s` as mutable because it is also borrowed as immutable
  
      println!("{}, {}, and {}", r1, r2, r3);
  }
  
  ```

  

- 悬空引用 dangling references

  悬空指针(Dangling Pointer): 一个指针引用了内存中的某个地址，而这块内存可能已经释放并分配给其它人使用了。

  在Rust里，编译器可保证引用永远都不是悬空引用:-如果你引用了某些数据，编译器将保证在引用离开作用域之前数据不会离开作用域

  ```rust
  fn main() {
      let reference_to_nothing = dangle();  // s被销毁 返回值是s的引用 (&s指向已被释放的内存) - 过不了rust编译 missing lifetime specifier
  }
  
  fn dangle() -> &String {
      let s = String::from("hello");
      &s  // 返回s的引用
  }  // s出了作用域 被销毁
  
  ```

  

- 引用的规则

  在任何给定的时刻，只能满足下列条件之一: 

  - 一个可变的引用

  - 任意数量不可变的引用

  引用必须一直有效



#### 切片

- Rust的另外一种不持有所有权的数据类型: 切片(slice)

  一道题，编写一个函数:

  它接收字符串作为参数

  返回它在这个字符串里找到的第一个单词

  如果函数没找到任何空格，那么整个字符串就被返回

  ```rust
  fn main() {
      let mut s = String::from("hello world");
      let wordIndex = frist_word(&s);
  
      s.clear();  // 索引位置脱离字符串的上下文将毫无意义
      println!("{}", wordIndex);
  }
  
  fn frist_word(s: &String) -> usize {
      let bytes = s.as_bytes(); // 得到字节数组
      for (i, &item) in bytes.iter().enumerate() {
          if item == b' ' { // 空格字面值
              return i; 
          }
      }
      s.len() // 要是找不到 就返回字符串长度
  }
  
  ```

  

  索引位置脱离字符串的上下文将毫无意义

  必须随时关注wordIndex的有效性、wordIndex和s的同步性 (自己维护则繁琐且易错 rust有解决方案)

  

- 字符串切片：指向字符串中一部分内容的引用

  形式：`字符串引用[开始索引..结束索引]`

  包前不包后：开始索引是切片起始位置的索引值、结束索引是切片终止位置的下一个索引值

  ```rust
  fn main() {
      let s = String::from("hello world");
  
      let hello = &s[..5]; // 0可省略
      let world = &s[6..]; // s.len()可省略
      let hello_world = &s[..]; // 整个
  
      println!("{}, {}, {}", hello, world,hello_world)
  }
  
  ```

  

  字符串切片的范围索引必须发生在有效的 UTF-8字符边界内。

  如果尝试从一个多字节的字符中创建字符串切片，程序会报错并退出

  

  ```rust
  fn main() {
      let mut s = String::from("hello world");
      let wordIndex = frist_word(&s); // 不可变引用
  
      // s.clear();  // 清理 可变引用 cannot borrow `s` as mutable because it is also borrowed as immutable
      println!("{}", wordIndex);
  }
  
  
  fn frist_word(s: &String) -> &str {  // 返回值是字符串切片 &str
      let bytes = s.as_bytes(); 
      for (i, &item) in bytes.iter().enumerate() {
          if item == b' ' { 
              return &s[..i]; 
          }
      }
      &s[..]
  }
  
  ```

  

  字符串切面值就是切片

  字符串字面值被直接存储在二进制程序中

  `let s = "hello world";`

  变量s的类型是&str，它是一个指向二进制程序特定位置的切片

  - &str是不可变引用，所以字符串字面值也是不可变的

  ```rust
  fn main() {
      let s: &str = "hello world";
      println!("{}", s)
  }
  
  ```

  

  字符串切片作为参数传递

  `fn frist_word(s: &String) -> &str {`

  有经验的 Rust 开发者会采用 &str 作为参数类型，因为这样就可以同时接收string和 &str 类型的参数了:

  `fn frist_word(s: &str) -> &str {`

  - 使用字符串切片，直接调用该函数

  - 使用 String，可以创建一个完整的String 切片来调用该函数

  定义函数时使用字符串切片来代替字符串引用会使我们的API更加通用，且不会损失任何功能。

  ```rust
  fn main() {
      let my_string = String::from("hello world");
      let wordIndex = frist_word(&my_string[..]);
  
      let my_string_literal = "hello world";
      let wordIndex = frist_word(&my_string_literal);
  }
  
  fn frist_word(s: &str) -> &str {
      let bytes = s.as_bytes();
      for (i, &item) in bytes.iter().enumerate() {
          if item == b' ' {
              return &s[..i];
          }
      }
      &s[..]
  }
  
  ```

  

- 其他类型的切片

  ```rust
  fn main() {
      let a = [1, 2, 3, 4, 5];
      let slice: &[i32] = &a[1..3];
      println!("{}", slice[1])
  }
  
  ```

  



### struct

#### 定义和实例化struct

- struct结构体

  自定义的数据类型

  为相关联的值命名、打包 => 有意义的组合

  

  定义struct

  使用 `struct` 关键字，并为整个 struct 命名在花括号内，为所有`字段(Field)`定义名称和类型

  实例化struct

  为每个字段指定具体值、无需按声明的顺序进行指定

  一旦struct的实例是可变的，那么实例中所有的字段都是可变 (不允许单独几个字段可变)

  取得struct里面的某个值：点标记法

  ```rust
  struct User {
      username: String,
      email: String,
      sign_in_count: u64,
      activate: bool,
  }
  
  fn main() {
      println!("hello world");
      let mut user1 = User {
          email: String::from("plk@123.com"),
          username: String::from("Amy"),
          activate: true,
          sign_in_count: 556,
      };
      user1.email = String::from("time@example.com");
  }
  
  ```

  

  struct作为函数的返回值

  ```rust
  struct User {
      username: String,
      email: String,
      sign_in_count: u64,
      activate: bool,
  }
  
  fn build_user(email: String, username: String) -> User {  // 函数的最后一个表达式就是其返回值
      User {
          email: email,
          username: username,
          activate: true,
          sign_in_count: 1,
      }
  }
  ```

  字段初始化简写：当字段名与字段值对应变量名相同时简写

  ```rust
  fn build_user(email: String, username: String) -> User {
      User {
          email,
          username,
          activate: true,
          sign_in_count: 1,
      }
  }
  ```

  

  struct更新语法

  想基于某个struct实例来创建一个新实例

  ```rust
      let user2 = User {
          email: String::from("another@example.com"),
          username:String::from("Rocy"),
          activate:user1.activate,
          sign_in_count:user1,sign_in_count,
      };
  ```

  ```rust
      let user2 = User {
          email: String::from("another@example.com"),
          username:String::from("Rocy"),
          ..user1
      };
  ```

  

  Tuple struct

  可定义类似 tuple 的 struct，叫做 tuple struct

  - Tuple struct整体有个名，但里面的元素没有名

  - 适用: 想给整个 tuple起名，并让它不同于其它 tuple，而且又不需要给每个元素起名

  定义 tuple struct:使用 struct 关键字，后边是名字，以及里面元素的类型

  例子:

  ```rust
  struct Color(i32,i32,i32);
  struct Point(i32,i32,i32);
  
  let black= Color(0, 0, 0);
  let origin = Point(0, 0, 0);
  
  // black 和 origin 是不同的类型 是不同Tup;e struct的实例
  ```

  

  Unit-Like Struct 没有任何字段

  可以定义没有任何字段的 struct，叫做 Unit-Like struct(因为与()，单元类型类似)

  适用：需要在某个类型上实现某个 trait，但是在里面又没有想要存储的数据

  

  struct数据所有权

  ```
  struct User {
      username: String,
      email: String,
      sign_in_count: u64,
      active: bool,
  }
  
  // 这里的字段使用了 String 而不是 &str:
  // 该struct 实例拥有其所有的数据
  // 只要struct实例是有效的，那么里面的字段数据也是有效的
  
  // struct 里也可以存放引用，但这需要使用生命周期(以后讲)
  // 生命周期保证只要struct实例是有效的，那么里面的引用也是有效的。
  // 如果 struct 里面存储引用，而不使用生命周期，就会报错(例子)。
  ```

  ```rust
  struct User {
      username: &str,  // 需要生命周期 err
      email: &str,  // 需要生命周期 err
      sign_in_count: u64,
      activate: bool,
  }
  
  fn main() {
      println!("hello world");
      let user1 = User{
          email:"fefe@we.com",
          username:"zhou",
          activate:true,
          sign_in_count:34,
      };
  }
  
  ```

  ```rust
  struct User<'a> {
      username: &'a str,  // 指定生命周期
      email: &'a str,     // 指定生命周期
      sign_in_count: u64,
      activate: bool,
  }
  
  fn main() {
      let user_data = "zhou";
      let user_email = "fefe@we.com";
      let user1 = User {
          username: &user_data,
          email: &user_email,
          sign_in_count: 34,
          activate: true,
      };
      println!("{:?}", user1);
  }
  ```

  

#### struct例子

- 题目需求：计算长方形面积

  ```rust
  fn main() {
      let w = 30;
      let l = 50;
      println!("{}", area(w, l))；
  }
  
  fn area(width:u32,length:u32)->u32{
      width * length
  }
  ```

  

  长方形的长和宽应该是有关联的

  ```rust
  use std::u32;
  
  fn main() {
      let rect = (30, 50);
      println!("{}", area(rect));
  }
  
  fn area(dim: (u32, u32)) -> u32 {
      dim.0 * dim.1
  }
  
  ```

  

  可读性变差了，谁长谁宽

  ```rust
  #[derive(Debug)]
  struct Rectangle {
      width: u32,
      length: u32,
  }
  
  fn main() {
      let rect = Rectangle {
          width: 30,
          length: 50,
      };
      println!("{}", area(&rect)); // 传参 不可变借用  main函数保留所有权
  
      println!("{:#?}", rect); // 保留所有权 能够调用
  }
  
  fn area(rect: &Rectangle) -> u32 {
      rect.width * rect.length
  }
  
  ```

  

- 总结

  std::fmt::Display

  std::fmt::Debug

  #[derive(Debug)]

  {:?}

  {:#?}



#### struct的方法

- struct方法

  方法和函数类似：fn关键字、名称、参数、返回值

  方法与函数不同之处：

  - 方法是在struct(或enum、trait 对象)的上下文中定义

  - 第一个参数是self，表示方法被调用的struct实例

  

  area函数只计算长方形，把area和Rectangle关联：在struct上定义方法

  定义方法：

  在 impl 块里定义方法

  方法的第一个参数可以是&self，也可以获得其所有权或可变借用。和其他参数样。

  更良好的代码组织。

  

  ```rust
  #[derive(Debug)]
  struct Rectangle {
      width: u32,
      length: u32,
  }
  
  impl Rectangle {
      fn area(&self) -> u32 {  // 借用
          self.width * self.length
      }
  }
  
  fn main() {
      let rect = Rectangle {
          width: 30,
          length: 50,
      };
      // println!("{}", area(&rect)); // 函数调用
      println!("{}", rect.area()); // 实例.方法调用
  
      println!("{:#?}", rect);
  }
  
  ```

  

  方法调用的运算符

  C/C++: object->something()和(*object).something() 一样

  Rust 没有`->`运算符

  Rust会自动引用或解引用

  - 在调用方法时就会发生这种行为

  在调用方法时，Rust根据情况自动添加&、&mut或`*`，以便 obiect 可以匹配方法的签名。

  

  下面两行代码效果相同: 

  p1.distance(&p2);

  (&p1).distance(&p2);

  

- 方法参数

  多个参数

  

  判断一个长方形能否容下另一个长方形

  ```rust
  #[derive(Debug)]
  struct Rectangle {
      width: u32,
      length: u32,
  }
  
  impl Rectangle {
      fn area(&self) -> u32 {
          self.width * self.length
      }
  
      fn can_hold(&self, other: &Rectangle) -> bool {
          self.width >= other.width && self.length >= other.length
      }
  }
  
  fn main() {
      let rect1 = Rectangle {
          width: 30,
          length: 50,
      };
      let rect2: Rectangle = Rectangle {
          width: 10,
          length: 40,
      };
      let rect3: Rectangle = Rectangle {
          width: 35,
          length: 55,
      };
      println!("{}", rect1.can_hold(&rect2));
      println!("{}", rect1.can_hold(&rect3));
  }
  
  ```

  

- 关联函数

  在`impl`块中定义、不把self作为第一个参数的函数 (不是方法)

  应用：

  - 通常用于构造器，即创建被关联类型的实例，如`String::form()`

  - 模块创建的命名空间 (以后讲)

  

  特殊的长方形：正方形

  ```rust
  #[derive(Debug)]
  struct Rectangle {
      width: u32,
      length: u32,
  }
  
  impl Rectangle {
      // 方法
      fn area(&self) -> u32 {
          self.width * self.length
      }
  
      fn can_hold(&self, other: &Rectangle) -> bool {
          self.width >= other.width && self.length >= other.length
      }
  
      // 关联函数
      fn square(size: u32) -> Rectangle {
          Rectangle {
              width: size,
              length: size,
          }
      }
  }
  
  fn main() {
      let rect1 = Rectangle {
          width: 30,
          length: 50,
      };
      let rect2: Rectangle = Rectangle {
          width: 10,
          length: 40,
      };
      let rect3: Rectangle = Rectangle {
          width: 35,
          length: 55,
      };
      let s =Rectangle::square(20);
      
      println!("{}", rect1.can_hold(&rect2));
      println!("{}", rect1.can_hold(&rect3));
  }
  
  ```

  

  多个`impl`块

  每个struct允许拥有多个`impl`块

  

### 枚举与模式匹配

#### 定义枚举

- 枚举：允许我们列举所有可能的值来定义一个类型

  例如ip地址：ipv4、ipv6

  

  定义枚举、枚举值

  ```rust
  // 定义枚举
  enum IpAddrKind {
      V4,
      V6,
  }
  
  fn main() {
      // 枚举值
      let four = IpAddrKind::V4;
      let six = IpAddrKind::V6;
  
      route(four);
      route(six);
      route(IpAddrKind::V6);
  }
  
  fn route(ip_kind: IpAddrKind) {
  
  }
  
  ```

  

  将数据附加到枚举的变体中

  优点：

  不需要额外使用

  ```rust
  enum IpAddrKind {
      V4,
      V6,
  }
  
  struct IpAddr {
      kind: IpAddrKind,
      address: String,
  }
  
  fn main() {
      // 用结构体存储枚举相关数据
      let home = IpAddr {
          kind:IpAddrKind::V4,
          address:String::from("127.0.0.1"),
      };
  
      let loopback = IpAddr {
          kind:IpAddrKind::V6,
          address:String::from("::1"),
      };
  }
  
  fn route(ip_kind: IpAddrKind) {}
  
  ```

  

  1





#### option枚举







#### match





#### if let





### 包

#### package crate module

- 1

  ```
  touch src/lib.rs
  ```

  D:\code\hyz-code-rust\learning_grammar\my-project\src\lib.rs

  ```rust
  mod front_of_house {
      mod hosting {
          fn add_to_waitlist() {}
          fn seat_at_table() {}
      }
  
      mod serving {
          fn tabke_order() {}
          fn serve_order() {}
          fn take_payment() {}
      }
  }
  
  ```

  

  在同一个文件中的调用

  ```rust
  mod front_of_house {  // 同根级可以互相调用
      pub mod hosting { // pub
          pub fn add_to_waitlist() {} // pub
      }
  }
  
  pub fn eat_at_restaurant() {
      // eat_at_restaurant函数和front_of_house模块都在同一个crateRoot里(lib.rs)
      crate::front_of_house::hosting::add_to_waitlist(); // 绝对路径 从crate开始  (私有的)
      front_of_house::hosting::add_to_waitlist(); // 相对路径 (同一子目录)
  }
  
  ```

  

  

  

  

  

  









#### 路径





#### use关键字







#### 将模块放到其他文件





### vector









## 进阶语法

### 异步并发





## RustWeb全栈开发 (Actix)

### 背景

- 介绍：后端和前端都是rust

  web service

  服务器端 web app

  客户端 web app (webAssembly)

  web框架：Actix

  数据库：postgreSQL

  数据库连接：SQLx



#### 构建TCP Server

- 编写TCP Server和Client、且互相通信

  标准库的 `std::net` 模块，提供网络基本功能

  支持TCP和UDP通信

  TcpListener、TcpStream

  



- 新建项目

  ```
  cargo new s1 && cd s1  # 工作空间 多个rust项目作为一个单元管理
  cargo new tcpserver
  cargo new tcpclient
  code .
  ```

  D:\code\hyz-code-rust\rust_web\s1\Cargo.toml

  ```toml
  [workspace] 
  
  members = [ "tcpclient","tcpserver"] 
  ```

  ```toml
  workspace = { members = [ "tcpclient","tcpserver"] }
  [package]
  name = "s1"
  version = "0.1.0"
  edition = "2021"
  
  # See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
  
  [dependencies]
  
  ```

- 建立连接

  D:\code\hyz-code-rust\rust_web\s1\tcpserver\src\main.rs

  ```rust
  use std::net::TcpListener;
  
  fn main() {
      let listener = TcpListener::bind("127.0.0.1:3000").unwrap();
      println!("Running on port 3000 ...");
  
      // let result = listener.accept().unwrap(); // listener.accept() 只接受一次请求
      for stream in listener.incoming() {  // listener.incoming() 持续监听  (返回的是迭代器 每个连接是一个字节流)
          let _stream = stream.unwrap();
          println!("Connection established!")
      }
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\s1\tcpclient\src\main.rs

  ```rust
  use std::net::TcpStream;
  
  fn main() {
      let _stream = TcpStream::connect("localhost:3000").unwrap();
  }
  
  ```


  ```
  cargo run -p tcpserver
  cargo run -p tcpclient  # 新cmd
  ```

- 发送接收消息

  ```rust
  use std::io::{Read, Write};
  use std::net::TcpListener;
  
  fn main() {
      let listener = TcpListener::bind("127.0.0.1:3000").unwrap();
      println!("Running on port 3000 ...");
  
      for stream in listener.incoming() {
          let mut stream = stream.unwrap();
          println!("Connection established!")
  
          let mut buffer = [0; 1024];
          stream.read(&mut buffer).unwrap();
          stream.write(&mut buffer);
      }
  }
  
  ```

  ```rust
  use std::io::{Read, Write};
  use std::net::TcpStream;
  use std::str;
  
  fn main() {
      let mut stream = TcpStream::connect("localhost:3000").unwrap();
      stream.write("Hello".as_bytes()).unwrap(); //传输需要用原始字节
  
      let mut buffer = [0; 5]; // 服务器把发送数据原封不动返回
      stream.read(&mut buffer).unwrap();
      println!(
          "Response from server: {:?}",
          str::from_utf8(&buffer).unwrap()
      ); // 把原始字节转换成utf8字符串
  }
  
  ```

  ```
  cargo run -p tcpserver
  cargo run -p tcpclient  # 新cmd
  ```

  

#### 自建HTTP Server

- 请求和响应的结构

  ![](res/Snipaste_2024-03-04_21-20-40.png)

  

- HTTP Server

  web server的消息流动图

  rust没有内置的http支持

  ![](res/Snipaste_2024-03-04_16-03-04.png)

  

  **web server的组成**

  server：监听进来的tcp字节流

  router：接收http请求，并决定调用哪个handler

  handler：处理http请求，构建http响应

  http library：解释字节流，把它转化成为http请求；把http响应转化回字节流

  

  **构建步骤**

  1. 解析http请求消息：HttpRequest、Method、Version 

  - 都要实现的Trait：

    `From<&str>`  把传进来的字符串切片转化成HttpRequest

    `Debug`  打印调试信息

    `PartialEq`  用于解析和自动化测试脚本里作比较

  2. 构建http响应消息

  3. router与handler

  4. 测试web server

  

  ```
  cargo new httpserver
  cargo new --lib http
  ```

  ```toml
  [workspace] 
  
  members = [ "tcpclient","tcpserver","httpserver","http"] 
  ```

  D:\code\hyz-code-rust\rust_web\s1\http\src\lib.rs

  ```rust
  pub mod httprequest;
  pub mod httpresponse;
  ```

  

- http请求模块

  D:\code\hyz-code-rust\rust_web\s1\http\src\httprequest.rs

  ```rust
  use std::collections::HashMap;
  
  #[derive(Debug, PartialEq)]
  pub enum Method {
      Get,
      Post,
      Unintialized,
  }
  
  impl From<&str> for Method {
      fn from(s: &str) -> Method {
          match s {
              "GET" => Method::Get,
              "POST" => Method::Post,
              _ => Method::Unintialized,
          }
      }
  }
  
  #[derive(Debug, PartialEq)]
  pub enum Version {
      V1_1,
      V2_0,
      Unintialized,
  }
  
  impl From<&str> for Version {
      fn from(s: &str) -> Version {
          match s {
              "HTTP/1.1" => Version::V1_1,
              _ => Version::Unintialized,
          }
      }
  }
  
  #[derive(Debug, PartialEq)]
  pub enum Resource {
      Path(String), // 请求的资源路径
  }
  
  #[derive(Debug, PartialEq)]
  pub struct HttpRequest {
      pub method: Method,
      pub version: Version,
      pub resource: Resource,
      pub headers: HashMap<String, String>,
      pub msg_body: String,
  }
  
  impl From<String> for HttpRequest {
      fn from(req: String) -> Self {
          let mut parsed_method = Method::Unintialized;
          let mut parsed_version = Version::V1_1;
          let mut parsed_resource = Resource::Path("".to_string());
          let mut parsed_headers = HashMap::new();
          let mut parsed_msg_body = "";
  
          for line in req.lines() {
              if line.contains("HTTP") {
                  let (method, resource, version) = process_req_line(line);
                  parsed_method = method;
                  parsed_resource = resource;
                  parsed_version = version;
              } else if line.contains(":") {
                  let (key, value) = process_header_line(line);
                  parsed_headers.insert(key, value);
              } else if line.len() == 0 {
              } else {
                  parsed_msg_body = line;
              }
          }
  
          HttpRequest {
              method: parsed_method,
              version: parsed_version,
              resource: parsed_resource,
              headers: parsed_headers,
              msg_body: parsed_msg_body.to_string(),
          }
      }
  }
  
  fn process_req_line(s: &str) -> (Method, Resource, Version) {
      let mut words = s.split_whitespace();
      let method = words.next().unwrap();
      let resource = words.next().unwrap();
      let version = words.next().unwrap();
  
      (
          method.into(),
          Resource::Path(resource.to_string()),
          version.into(),
      )
  }
  
  fn process_header_line(s: &str) -> (String, String) {
      let mut header_items = s.split(":");
      let mut key = String::from("");
      let mut value = String::from("");
  
      if let Some(k) = header_items.next() {
          key = k.to_string();
      }
      if let Some(v) = header_items.next() {
          value = v.to_string();
      }
  
      (key, value)
  }
  
  #[cfg(test)]
  mod test {
      use super::*;
  
      #[test]
      fn test_method_into() {
          let m: Method = "GET".into(); // 把字符串转化为Method的枚举变体
          assert_eq!(m, Method::Get); // assert
      }
  
      #[test]
      fn test_version_into() {
          let v: Version = "HTTP/1.1".into();
          assert_eq!(v, Version::V1_1);
      }
  
      #[test]
      fn test_read_http() {
          let s:String = String::from("GET /greeting HTTP/1.1\r\nHost: localhost:3000\r\nUser-Agent: curl/7.71.1\r\nAccept: */*\r\n\r\n");
          let mut headers_expected = HashMap::new();
          headers_expected.insert("Host".into(), " localhost".into());
          headers_expected.insert("Accept".into(), " */*".into());
          headers_expected.insert("User-Agent".into(), " curl/7.71.1".into());
          let req: HttpRequest = s.into();
  
          assert_eq!(Method::Get, req.method);
          assert_eq!(Version::V1_1, req.version);
          assert_eq!(Resource::Path("/greeting".to_string()), req.resource);
          assert_eq!(headers_expected, req.headers);
      }
  }
  
  ```

  ```
  cargo test -p http
  ```

  

- HTTP响应模块

  **HttpResponse需要实现的方法**

  `Default trait`：指定成员的默认值

  `new()`：使用默认值创建一个新的结构体

  `send_response`：构建响应，将原始字节通过TCP传送

  `getter方法`：获得成员的值

  `From trait`：能够将HttpResponse转化为String

  

  D:\code\hyz-code-rust\rust_web\s1\http\src\httpresponse.rs

  ```rust
  use std::collections::HashMap;
  use std::io::{Result, Write};
  
  #[derive(Debug, PartialEq, Clone)]
  pub struct HttpResponse<'a> {
      version: &'a str,
      status_code: &'a str,
      status_text: &'a str,
      headers: Option<HashMap<&'a str, &'a str>>,
      body: Option<String>,
  }
  
  impl<'a> Default for HttpResponse<'a> {
      fn default() -> Self {
          Self {
              version: "HTTP/1.1".into(),
              status_code: "200".into(),
              status_text: "OK".into(),
              headers: None,
              body: None,
          }
      }
  }
  
  impl<'a> From<HttpResponse<'a>> for String {
      fn from(res: HttpResponse) -> String {
          let res1 = res.clone();
          format!(
              "{} {} {}\r\n{}Content-Length: {}\r\n\r\n{}",
              &res1.version(),
              &res1.status_code(),
              &res1.status_text(),
              &res1.headers(),
              &res.body.unwrap().len(),
              &res1.body()
          )
      }
  }
  
  impl<'a> HttpResponse<'a> {
      pub fn new(
          status_code: &'a str,
          headers: Option<HashMap<&'a str, &'a str>>,
          body: Option<String>,
      ) -> HttpResponse<'a> {
          let mut response: HttpResponse<'a> = HttpResponse::default();
          if status_code != "200" {
              response.status_code = status_code.into();
          };
          response.headers = match &headers {
              Some(_h) => headers,
              None => {
                  let mut h = HashMap::new();
                  h.insert("Content-Type", "text/html");
                  Some(h)
              }
          };
          response.status_text = match response.status_code {
              "200" => "OK".into(),
              "400" => "Bad Request".into(),
              "404" => "Not Found".into(),
              "500" => "Internal Server Error".into(),
              _ => "Not Found".into(),
          };
          response.body = body;
          response
      }
  
      pub fn send_response(&self, write_stream: &mut impl Write) -> Result<()> {
          let res = self.clone();
          let response_string: String = String::from(res);
          let _ = write!(write_stream, "{}", response_string);
  
          Ok(())
      }
  
      fn version(&self) -> &str {
          self.version
      }
  
      fn status_code(&self) -> &str {
          self.status_code
      }
  
      fn status_text(&self) -> &str {
          self.status_text
      }
  
      fn headers(&self) -> String {
          let map: HashMap<&str, &str> = self.headers.clone().unwrap();
          let mut header_string: String = "".into();
          for (k, v) in map.iter() {
              header_string = format!("{}{}:{}\r\n", header_string, k, v);
          }
          header_string
      }
  
      pub fn body(&self) -> &str {
          match &self.body {
              Some(b) => b.as_str(),
              None => "",
          }
      }
  }
  
  #[cfg(test)]
  mod tests {
      use super::*;
  
      #[test]
      fn test_response_struct_creation_200() {
          let response_actual = HttpResponse::new(
              "200", 
              None, 
              Some("xxxx".into()),
          );
          let response_expected = HttpResponse {
              version: "HTTP/1.1",
              status_code: "200",
              status_text: "OK",
              headers: {
                  let mut h = HashMap::new();
                  h.insert("Content-Type", "text/html");
                  Some(h)
              },
              body: Some("xxxx".into()),
          };
          assert_eq!(response_actual, response_expected);
      }
  
      #[test]
      fn test_response_struct_creation_404() {
          let response_actual = HttpResponse::new("404", None, Some("xxxx".into()));
          let response_expected = HttpResponse {
              version: "HTTP/1.1",
              status_code: "404",
              status_text: "Not Found",
              headers: {
                  let mut h = HashMap::new();
                  h.insert("Content-Type", "text/html");
                  Some(h)
              },
              body: Some("xxxx".into()),
          };
          assert_eq!(response_actual, response_expected);
      }
  
      #[test]
      fn test_http_response_creation() {
          let response_expected = HttpResponse {
              version: "HTTP/1.1",
              status_code: "404",
              status_text: "Not Found",
              headers: {
                  let mut h = HashMap::new();
                  h.insert("Content-Type", "text/html");
                  Some(h)
              },
              body: Some("xxxx".into()),
          };
          let http_string: String = response_expected.into();
          let actual_string =
              "HTTP/1.1 404 Not Found\r\nContent-Type:text/html\r\nContent-Length: 4\r\n\r\nxxxx";
          assert_eq!(http_string, actual_string);
      }
  }
  
  ```

  

- 构建server模块

  D:\code\hyz-code-rust\rust_web\s1\httpserver\Cargo.toml

  ```toml
  [dependencies]
  http = {path = "../http"}
  serde = {version="1.0.131", features=["derive"]}
  serde_json = "1.0.72"
  ```

  

  **main -> server -> router -> handler**

  D:\code\hyz-code-rust\rust_web\s1\httpserver\src\server.rs

  ```rust
  use super::router::Router;
  use http::httprequest::HttpRequest;
  use std::io::prelude::*;
  use std::net::TcpListener;
  use std::str;
  
  pub struct Server<'a> {
      socket_addr: &'a str,
  }
  
  impl<'a> Server<'a> {
      pub fn new(socket_addr: &'a str) -> Self {
          Server { socket_addr }
      }
  
      pub fn run(&self) {
          let connection_listener = TcpListener::bind(self.socket_addr).unwrap();
          println!("Running on {}", self.socket_addr);
  
          for stream in connection_listener.incoming() {
              let mut stream = stream.unwrap();
              println!("Connection established");
  
              let mut read_buffer = [0; 200];
              stream.read(&mut read_buffer).unwrap();
  
              let req: HttpRequest = String::from_utf8(read_buffer.to_vec()).unwrap().into();
              Router::route(req, &mut stream);  // 调用路由 分发给handler
          }
      }
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\s1\httpserver\src\main.rs

  ```rust
  mod handler;
  mod router;
  mod server;
  
  use server::Server;
  
  fn main() {
      let server = Server::new("localhost:3000");
      server.run();
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\s1\httpserver\src\router.rs

  ```rust
  use super::handler::{Handler, PageNotFoundHandler, StaticPageHandler, WebServiceHandler};
  use http::{httprequest, httprequest::HttpRequest, httpresponse::HttpResponse};
  use std::io::prelude::*;
  
  pub struct Router;
  
  impl Router {
      pub fn route(req: httprequest, stream: &mut impl Write) -> () {
          match req.method {
              httprequest::Method::Get => match &req.resource {
                  httprequest::Rescource::Path(s) => {
                      let route: Vec<&str> = s.split("/").collect();
                      match route[1] {
                          "api" => {
                              let resp: HttpResponse = WebServiceHandler::handler(&req);
                              let _ = resp.send_response(stream);
                          }
                          _ => {
                              let resp: HttpResponse = StaticPageHandler::Handler(&req);
                              let _ = resp.send_response(stream);
                          }
                      }
                  }
              },
              _ => {
                  let resp: HttpResponse = PageNotFoundHandler::handler(&req);
                  let _ = resp.send_response(stream);
              }
          }
      }
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\s1\httpserver\src\handler.rs

  ```rust
  use http::{httprequest::HttpRequest, httpresponse::HttpResponse};
  use serde::{Deserialize, Serialize};
  use std::collections::HashMap;
  use std::env;
  use std::fs;
  
  pub trait Handler {
      fn handle(req: &HttpRequest) -> HttpResponse;
      fn load_file(file_name: &str) -> Option<String> {
          let default_path = format!("{}/public", env!("CARGO_MANIFEST_DIR"));
          let public_path = env::var("PUBLIC_PATH").unwrap_or(default_path);
          let full_path = format!("{}/{}", public_path, file_name);
  
          let contents = fs::read_to_string(full_path);
          contents.ok()
      }
  }
  
  pub struct PageNotFoundHandler;
  pub struct StaticPageHandler;
  pub struct WebServiceHandler;
  
  #[derive(Serialize, Deserialize)]
  pub struct OrderStatus {
      order_id: i32,
      order_date: String,
      order_status: String,
  }
  
  impl Handler for PageNotFoundHandler {
      fn handle(_req: &HttpRequest) -> HttpResponse {
          HttpResponse::new("404", None, Self::load_file("404.html"))
      }
  }
  
  impl Handler for StaticPageHandler {
      fn handle(req: &HttpRequest) -> HttpResponse {
          let http::httprequest::Resource::Path(s) = &req.resource;
          let route: Vec<&str> = s.split("/").collect();
          match route[1] {
              "" => HttpResponse::new("200", None, Self::load_file("index.html")),
              "health" => HttpResponse::new("200", None, Self::load_file("health.html")),
              path => match Self::load_file(path) {
                  Some(contents) => {
                      let mut map: HashMap<&str, &str> = HashMap::new();
                      if path.ends_with(".css") {
                          map.insert("Content-Type", "text/css");
                      } else if path.ends_with(".js") {
                          map.insert("Content-Type", "text/javascript");
                      } else {
                          map.insert("Content-Type", "text/html");
                      }
                      HttpResponse::new("200", Some(map), Some(contents))
                  }
                  None => HttpResponse::new("404", None, Self::load_file("404.html")),
              },
          }
      }
  }
  
  impl WebServiceHandler {
      fn load_json() -> Vec<OrderStatus> {
          let default_path = format!("{}/data", env!("CARGO_MANIFEST_DIR"));
          let data_path = env::var("DATA_PATH").unwrap_or(default_path);
          let full_path = format!("{}/{}", data_path, "orders.json");
          let json_contents = fs::read_to_string(full_path);
          let orders: Vec<OrderStatus> =
              serde_json::from_str(json_contents.unwrap().as_str()).unwrap();
          orders
      }
  }
  
  impl Handler for WebServiceHandler {
      fn handle(req: &HttpRequest) -> HttpResponse {
          let http::httprequest::Resource::Path(s) = &req.resource;
          let route: Vec<&str> = s.split("/").collect();
  
          // localhost:3000/api/shipping/orders
          match route[2] {
              "shipping" if route.len() > 2 && route[3] == "orders" => {
                  let body = Some(serde_json::to_string(&Self::load_json()).unwrap());
                  let mut headers: HashMap<&str, &str> = HashMap::new();
                  headers.insert("Content-Type", "application/json");
                  HttpResponse::new("200", Some(headers), body)
              }
              _ => HttpResponse::new("404", None, Self::load_file("404.html")),
          }
      }
  }
  
  ```

  

- 数据和html

  D:\code\hyz-code-rust\rust_web\s1\httpserver\data\orders.json

  ```json
  [
      {
          "order_id": 1,
          "order_date": "21 Jan 2020",
          "order_status": "Delivered"
      },
      {
          "order_id": 2,
          "order_date": "2 Feb 2020",
          "order_status": "Pending"
      }
  ]
  ```

  D:\code\hyz-code-rust\rust_web\s1\httpserver\public\styles.css

  ```css
  h1 {
      color: red;
      margin-left: 25px;
  }
  ```

  D:\code\hyz-code-rust\rust_web\s1\httpserver\public\index.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <link rel="stylesheet" href="styles.css">
      <title>Index!</title>
  </head>
  <body>
      <h1>Hello, welcome to home page</h1>
      <p>This ih the index page for the web site</p>
  </body>
  </html>
  ```

  D:\code\hyz-code-rust\rust_web\s1\httpserver\public\404.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Not Found!</title>
  </head>
  <body>
      <h1>404 Error</h1>
      <p>Sorry the requested page does not exist</p>
  </body>
  </html>
  ```

  D:\code\hyz-code-rust\rust_web\s1\httpserver\public\health.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Health!</title>
  </head>
  <body>
      <h1>Hello, welcome to health page!</h1>
      <p>This site is perfectly fine</p>
  </body>
  </html>
  ```

  测试HTTP Server

  ```
  cargo run -p httpserver
  
  # http://localhost:3000/
  # http://localhost:3000/health
  # http://localhost:3000/api/shipping/orders
  # http://localhost:3000/bbb
  ```

  









































### Actix框架

#### 环境搭建

- 需要使用的crate

  actix-web v3

  actix-rt v1.1.1 (异步运行时)

  ```
  cargo new ws && cd ws  # 工作空间
  code .
  mkdir -p webservice/src/bin
  touch webservice/src/bin/sercer1.rs
  
  cargo build
  ```

  D:\code\hyz-code-rust\rust_web\ws\Cargo.toml

  ```toml
  [workspace]
  resolver = "1"
  members = ["webservice"]
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\Cargo.toml

  ```toml
  [dependencies]
  actix-web = "3"
  actix-rt = "1.1.1"
  
  [[bin]]
  name = "server1"  
  ```

  

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\bin\server1.rs

  ```rust
  use actix_web::{web, App, HttpResponse, HttpServer, Responder};
  use std::io;
  
  // 配置 route
  pub fn general_routes(cfg: &mut web::ServiceConfig) {
      cfg.route("/health", web::get().to(health_check_handler));
  }
  
  // 配置 handler
  pub async fn health_check_handler() -> impl Responder {
      HttpResponse::Ok().json("Actix Web Service is running!")
  }
  
  // 实例化 http server 并运行
  #[actix_rt::main]
  async fn main() -> io::Result<()> {
      // 构建app 配置route
      let app = move || App::new().configure(general_routes);
      // 运行http server
      HttpServer::new(app).bind("127.0.0.1:3000")?.run().await
  }
  
  ```

  ```
  # 项目根目录ws
  cargo run -p webservice --bin server1
  # http://localhost:3000/health
  
  # 在具体的项目中
  cd webservice/
  $ cargo run --bin server1  # 无需指定项目
  ```

  

- Actix基本组件

  ![](res/Snipaste_2024-03-06_13-25-52.png)

- Actix的并发(concurrency)

  Actix 支持两类并发：

  异步 I/O：给定的OS原生线程在等待 I/O时执行其他任务 (例如侦听网络连接)

  多线程并行：默认情况下启动OS原生线程的数量与系统逻辑CPU数量相同



#### 构建rustAPI：健康检查

- 需要使用的crate

  `serde v1` (序列化反序列化)

  `chrono v0.4` (时间相关的字段)

  

  api：添加一个、获取一个、获取全部

  POST：/courses

  GET：/coursesteacher_id/course_id

  GET：/courses/teacher_id

  ![](res/Snipaste_2024-03-06_13-47-53.png)

  

  ```
  # 新建文件
  cd webservice/src
  touch bin/teacher-service.rs models.rs state.rs routers.rs handlers.rs
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\Cargo.toml

  ```toml
  [package]
  name = "webservice"
  version = "0.1.0"
  edition = "2021"
  default-run = "teacher-service"
  
  # See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
  
  [dependencies]
  actix-web = "3"
  actix-rt = "1.1.1"
  
  [[bin]]
  name = "server1"
  
  [[bin]]
  name = "teacher-service"
  ```

  

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\state.rs (应用程序的状态)

  ```rust
  use std::sync::Mutex;
  
  pub struct AppState {
      pub health_check_response: String,
      pub visit_count: Mutex<u32>,
  }
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\routers.rs

  ```rust
  use super::handlers::*;
  use actix_web::web;
  
  pub fn general_routes(cfg: &mut web::ServiceConfig) {
      cfg.route("/health", web::get().to(health_check_handler));
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\handler.rs

  ```rust
  use super::state::AppState;
  use actix_web::{web, HttpResponse};
  
  pub async fn health_check_handler(app_state: web::Data<AppState>) -> HttpResponse {
      let health_check_response = &app_state.health_check_response;
      let mut visit_count = app_state.visit_count.lock().unwrap();
      let response = format!("{} {} times", health_check_response, visit_count);
      *visit_count += 1;
      HttpResponse::Ok().json(&response)
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\bin\teacher-service.rs

  ```rust
  use actix_web::{web, App, HttpServer};
  use std::io;
  use std::sync::Mutex;
  
  #[path = "../handlers.rs"]
  mod handlers;
  #[path = "../routers.rs"]
  mod routers;
  #[path = "../state.rs"]
  mod state;
  
  use routers::*;
  use state::AppState;
  
  #[actix_rt::main]
  async fn main() -> io::Result<()> {
      let shared_data = web::Data::new(AppState {
          health_check_response: "I'm OK.".to_string(),
          visit_count: Mutex::new(0),
      });
      let app = move || {
          App::new()
              .app_data(shared_data.clone())
              .configure(general_routes)
      };
      HttpServer::new(app).bind("127.0.0.1:3000")?.run().await
  }
  
  ```

  ```
  cd webservice
  cargo run
  curl localhost:3000/health
  ```

  

#### 构建rustAPI：post资源

- 配置文件

  D:\code\hyz-code-rust\rust_web\ws\webservice\Cargo.toml

  ```toml
  [dependencies]
  actix-web = "3"
  actix-rt = "1.1.1"
  serde = { version="1.0.132", features=["derive"] }
  chrono = { version="0.4.19", features=["serde"] }
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\models.rs

  ```rust
  use actix_web::web;
  use chrono::NaiveDateTime;
  use serde::{Deserialize, Serialize};
  
  #[derive(Deserialize, Serialize, Debug, Clone)]
  pub struct Course {
      pub teacher_id: usize,
      pub id: Option<usize>,
      pub name: String,
      pub time: Option<NaiveDateTime>,
  }
  
  impl From<web::Json<Course>> for Course {
      fn from(course: web::Json<Course>) -> Self {
          Course {
              teacher_id: course.teacher_id,
              id: course.id,
              name: course.name.clone(),
              time: course.time,
          }
      }
  }
  
  ```

  state

  ```rust
  use super::models::Course;
  use std::sync::Mutex; //
  
  pub struct AppState {
      pub health_check_response: String,
      pub visit_count: Mutex<u32>,
      pub courses: Mutex<Vec<Course>>, //
  }
  
  ```

  teacher-service

  ```rust
  use actix_web::{web, App, HttpServer};
  use std::sync::Mutex;
  use std::{io, path};
  
  #[path = "../handlers.rs"]
  mod handlers;
  #[path = "../models.rs"]
  mod models; // 模块声明
  #[path = "../routers.rs"]
  mod routers;
  #[path = "../state.rs"]
  mod state;
  
  use routers::*;
  use state::AppState;
  
  #[actix_rt::main]
  async fn main() -> io::Result<()> {
      let shared_data = web::Data::new(AppState {
          health_check_response: "I'm OK.".to_string(),
          visit_count: Mutex::new(0),
          courses: Mutex::new(vec![]), // 初始化
      });
      let app = move || {
          App::new()
              .app_data(shared_data.clone())
              .configure(general_routes)
              .configure(course_routes) // 注册路由
      };
      HttpServer::new(app).bind("127.0.0.1:3000")?.run().await
  }
  
  ```

  添加课程的功能

  routers

  ```rust
  use std::ops::Mul;
  
  use super::handlers::*;
  use actix_web::web;
  
  pub fn general_routes(cfg: &mut web::ServiceConfig) {
      cfg.route("/health", web::get().to(health_check_handler));
  }
  
  pub fn course_routes(cfg: &mut web::ServiceConfig) {
      cfg.service(
          web::scope("/courses") // 一系列资源的根路径
              .route("/", web::post().to(new_course))  // handler
      );
  }
  
  ```

  handler

  ```rust
  use super::state::AppState;
  use actix_web::{web, HttpResponse};
  
  pub async fn health_check_handler(app_state: web::Data<AppState>) -> HttpResponse {
      let health_check_response = &app_state.health_check_response;
      let mut visit_count = app_state.visit_count.lock().unwrap();
      let response = format!("{} {} times", health_check_response, visit_count);
      *visit_count += 1;
      HttpResponse::Ok().json(&response)
  }
  
  use super::models::Course;
  use chrono::Utc;
  
  pub async fn new_course(
      new_course: web::Json<Course>,
      app_state: web::Data<AppState>,
  ) -> HttpResponse {
      println!("Received new course");
      let course_count = app_state
          .courses
          .lock()
          .unwrap()
          .clone()
          .into_iter()
          .filter(|course| course.teacher_id == new_course.teacher_id)
          .collect::<Vec<Course>>()
          .len();
      let new_course = Course {
          teacher_id: new_course.teacher_id,
          id: Some(course_count + 1),
          name: new_course.name.clone(),
          time: Some(Utc::now().naive_utc()),
      };
      app_state.courses.lock().unwrap().push(new_course);
      HttpResponse::Ok().json("Course added")
  }
  
  
  #[cfg(test)]
  mod tests{
      use super::*;
      use actix_web::{http::StatusCode, web};
      use std::sync::Mutex;
  
      #[actix_rt::test]
      async fn post_course_test(){
          let course = web::Json(Course{
              teacher_id:1,
              name:"Test course".into(),
              id:None,
              time:None,
          });
          let app_state: web::Data<AppState> = web::Data::new(AppState{
              health_check_response:"".to_string(),
              visit_count:Mutex::new(0),
              courses:Mutex::new(vec![]),
          });
          let resp = new_course(course, app_state).await;
          assert_eq!(resp.status(),StatusCode::OK);
      }
  }
  ```

  ```
  cd webservice
  cargo test
  cargo run
  
  curl -X POST localhost:3000/courses/ -H "Content-Type: application/json" -d '{"teacher_id":1, "name":"First Course"}'  # 成功
  # postman 成功
  ```

  

#### 构建rustAPI：get资源

- 查询多笔数据、查询单笔数据

  routers

  ```rust
  use super::handlers::*;
  use actix_web::web::{self, route};
  
  pub fn general_routes(cfg: &mut web::ServiceConfig) {
      cfg.route("/health", web::get().to(health_check_handler));
  }
  
  pub fn course_routes(cfg: &mut web::ServiceConfig) {
      cfg.service(
          web::scope("/courses")
              .route("/", web::post().to(new_course))
              .route("/{user_id}", web::get().to(get_courses_for_teacher)) // handler
              .route("/{user_id}/{course_id}", web::get().to(get_course_detail)), // handler
      );
  }
  
  ```

  handlers

  ```rust
  use super::state::AppState;
  use actix_web::{web, HttpResponse};
  
  pub async fn health_check_handler(app_state: web::Data<AppState>) -> HttpResponse {
      let health_check_response = &app_state.health_check_response;
      let mut visit_count = app_state.visit_count.lock().unwrap();
      let response = format!("{} {} times", health_check_response, visit_count);
      *visit_count += 1;
      HttpResponse::Ok().json(&response)
  }
  
  use super::models::Course;
  use chrono::Utc;
  
  pub async fn new_course(
      new_course: web::Json<Course>,
      app_state: web::Data<AppState>,
  ) -> HttpResponse {
      println!("Received new course");
      let course_count = app_state
          .courses
          .lock()
          .unwrap()
          .clone()
          .into_iter()
          .filter(|course| course.teacher_id == new_course.teacher_id)
          .collect::<Vec<Course>>()
          .len();
      let new_course = Course {
          teacher_id: new_course.teacher_id,
          id: Some(course_count + 1),
          name: new_course.name.clone(),
          time: Some(Utc::now().naive_utc()),
      };
      app_state.courses.lock().unwrap().push(new_course);
      HttpResponse::Ok().json("Course added")
  }
  
  pub async fn get_courses_for_teacher(
      app_state: web::Data<AppState>,
      params: web::Path<(usize)>,
  ) -> HttpResponse {
      let teacher_id: usize = params.0;
  
      let filtered_courses = app_state
          .courses
          .lock()
          .unwrap()
          .clone()
          .into_iter()
          .filter(|course| course.teacher_id == teacher_id)
          .collect::<Vec<Course>>();
  
      if filtered_courses.len() > 0 {
          HttpResponse::Ok().json(filtered_courses)
      } else {
          HttpResponse::Ok().json("No course found for teacher".to_string())
      }
  }
  
  pub async fn get_course_detail(
      app_state: web::Data<AppState>,
      params: web::Path<(usize, usize)>,
  ) -> HttpResponse {
      let (teacher_id, course_id) = params.0;
      let selected_course = app_state
          .courses
          .lock()
          .unwrap()
          .clone()
          .into_iter()
          .find(|x| x.teacher_id == teacher_id && x.id == Some(course_id))
          .ok_or("Course not found");
  
      if let Ok(course) = selected_course {
          HttpResponse::Ok().json(course)
      } else {
          HttpResponse::Ok().json("Course not found".to_string())
      }
  }
  
  #[cfg(test)]
  mod tests {
      use super::*;
      use actix_web::{http::StatusCode, web, App};
      use std::sync::Mutex;
  
      #[actix_rt::test]
      async fn post_course_test() {
          let course = web::Json(Course {
              teacher_id: 1,
              name: "Test course".into(),
              id: None,
              time: None,
          });
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              courses: Mutex::new(vec![]),
          });
          let resp = new_course(course, app_state).await;
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_all_courses_success() {
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              courses: Mutex::new(vec![]),
          });
          let teacher_id: web::Path<(usize)> = web::Path::from((1));
          let resp = get_courses_for_teacher(app_state, teacher_id).await;
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_one_course_success() {
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              courses: Mutex::new(vec![]),
          });
          let params: web::Path<(usize, usize)> = web::Path::from((1, 1));
          let resp = get_course_detail(app_state, params).await;
          assert_eq!(resp.status(), StatusCode::OK);
      }
  }
  
  ```

  ```
  cd webservice/
  cargo test 
  cargo run 
  
  
  # 先添加几笔数据 
  curl -X POST localhost:3000/courses/ -H "Content-Type: application/json" -d '{"teacher_id":1, "name":"First Course"}' 
  curl -X POST localhost:3000/courses/ -H "Content-Type: application/json" -d '{"teacher_id":1, "name":"Second Course"}'  
  curl -X POST localhost:3000/courses/ -H "Content-Type: application/json" -d '{"teacher_id":1, "name":"Third Course"}'  
  
  # 再查询
  curl localhost:3000/courses/1
  
  
  # 先添加几笔数据 
  curl -X POST localhost:3000/courses/ -H "Content-Type: application/json" -d '{"teacher_id":1, "name":"First Course"}' 
  curl -X POST localhost:3000/courses/ -H "Content-Type: application/json" -d '{"teacher_id":1, "name":"Second Course"}'  
  curl -X POST localhost:3000/courses/ -H "Content-Type: application/json" -d '{"teacher_id":1, "name":"Third Course"}'  
  
  # 再查询
  curl localhost:3000/courses/1/1
  
  ```

  

#### 使用sqlx连接postgreSQL

- windocker中postgresql安装

  ```
  docker search postgres  # 检索
  docker pull postgres:16-alpine3.19  # 拉取镜像
  docker images  # 查看本地镜像
  
  # run 创建并运行一个容器
  docker run --name mypostgres \
  			-e POSTGRES_DB=database \
  			-e TZ=PRC \
  			-e POSTGRES_USER=root \
  			-e POSTGRES_PASSWORD=Root123 \
  			-p 5432:5432 \
  			-v D:\\systemEnvironment\\pastgresData:/var/lib/postgresql/data \
  			-d postgres:16-alpine3.19
  
  # 进入容器
  docker exec -it mypostgres bash
  psql -U root -d database
  
  create database hyzdb;  # 创建数据库
  \c hyzdb;  # 切换数据库
  
  select * from mytable;  # 查询表数据
  ```

  

- 数据存储：内存、数据库

  sqlx  v0.5.10 (连接数据库)

  PostgreSQL (数据库)

- 新建小项目

  ```
  cargo new db  && cd db
  code .
  
  touch db.sql
  touch .env
  ```

  D:\code\hyz-code-rust\rust_web\db\Cargo.toml

  ```toml
  [dependencies]
  actix-rt = "2.6.0"  # "1.1.1" 版本冲突
  actix-web = "3.3.3"
  chrono = {version = "0.4.19", features = ["serde"]}
  dotenv = "0.15.0"
  # openssl = {version = "0.10.38", features = ["vendored"]}
  serde = {version = "1.0.134", features = ["derive"]}
  sqlx = {version = "0.5.10", features= ["postgres", "runtime-tokio-rustls", "macros", "chrono",]}
  ```

  D:\code\hyz-code-rust\rust_web\db\db.sql

  ```sql
  drop table if exists course;
  
  create table course(
      id serial primary key,
      teacher_id int not null,
      name varchar(140) not null,
      time timestamp default now()
  );
  
  insert into
      course(id, teacher_id, name, time)
  values
      (1, 1, 'First course', '2022-01-17 05:40:00'),
      (2, 1, 'Second course', '2022-01-18 05:45:00');
  ```

  D:\code\hyz-code-rust\rust_web\db\.env

  ```
  DATABASE_URL=postgres://root:Root123@127.0.0.1:5432/hyzdb
  ```

  D:\code\hyz-code-rust\rust_web\db\src\main.rs

  ```rust
  use chrono::NaiveDateTime;
  use dotenv::dotenv;
  use sqlx::postgres::PgPoolOptions;
  use std::env;
  use std::io;
  
  #[derive(Debug)]
  pub struct Course {
      pub id: i32,
      pub teacher_id: i32,
      pub name: String,
      pub time: Option<NaiveDateTime>,
  }
  
  #[actix_rt::main]
  async fn main() -> io::Result<()> {
      dotenv().ok(); // 生产环境中 系统环境变量  (即使失败也忽略失败)
  
      let database_url = env::var("DATABASE_URL").expect("DATABASE_URL 没有再 .env 文件里设置");
      let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap();
      let course_rows = sqlx::query!(
          r#"select id, teacher_id, name, time from course where id = $1"#,
          1
      )
      .fetch_all(&db_pool)
      .await
      .unwrap();
  
      let mut courses_list = vec![];
      for row in course_rows {
          courses_list.push(Course {
              id: row.id,
              teacher_id: row.teacher_id,
              name: row.name,
              time: Some(chrono::NaiveDateTime::from(row.time.unwrap())),
          })
      }
      println!("Course = {:?}", courses_list);
      Ok(())
  }
  
  ```

  ```
  cargo run
  ```

  

#### 将数据库整合进项目

- 数据库代替内存存储 (连接数据库)

  D:\code\hyz-code-rust\rust_web\ws\webservice\Cargo.toml

  ```toml
  [dependencies]
  actix-rt = "2.6.0"
  actix-web = "4.0.0-rc.2"
  serde = { version="1.0.132", features=["derive"] }
  chrono = { version="0.4.19", features=["serde"] }
  dotenv = "0.15.0"
  # openssl = {version = "0.10.38", features = ["vendored"]}
  sqlx = {version = "0.5.10", default_features=false, features= ["postgres", "runtime-tokio-rustls", "macros", "chrono",]}
  ```

  ```
  cd rust_web/
  cp db/.env ws/src
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\state.rs

  ```rust
  // use super::models::Course;
  use sqlx::postgres::PgPool;
  use std::sync::Mutex;
  
  pub struct AppState {
      pub health_check_response: String,
      pub visit_count: Mutex<u32>,
      // pub courses: Mutex<Vec<Course>>,
      pub db: PgPool,  // 不用内存 用数据库存储 (连接池 多线程共享)
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\bin\teacher-service.rs

  ```rust
  use actix_web::{web, App, HttpServer};
  use std::io;
  use std::sync::Mutex;
  
  // 数据库连接
  use dotenv::dotenv;
  use sqlx::postgres::PgPoolOptions;
  use std::env;
  
  #[path = "../handlers.rs"]
  mod handlers;
  #[path = "../models.rs"]
  mod models;
  #[path = "../routers.rs"]
  mod routers;
  #[path = "../state.rs"]
  mod state;
  
  use routers::*;
  use state::AppState;
  
  #[actix_rt::main]
  async fn main() -> io::Result<()> {
      dotenv().ok();
      let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");  // 读取数据库连接信息
      let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap();  // 创建数据库连接池
      
      let shared_data = web::Data::new(AppState {
          health_check_response: "I'm OK.".to_string(),
          visit_count: Mutex::new(0),
          // courses: Mutex::new(vec![]),
          db: db_pool, // 数据库连接池
      });
      let app = move || {
          App::new()
              .app_data(shared_data.clone())
              .configure(general_routes)
              .configure(course_routes) 
      };
      HttpServer::new(app).bind("127.0.0.1:3000")?.run().await
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\handlers.rs (去掉内存储存)

  ```rust
  use super::state::AppState;
  use actix_web::{web, HttpResponse};
  
  pub async fn health_check_handler(app_state: web::Data<AppState>) -> HttpResponse {
      let health_check_response = &app_state.health_check_response;
      let mut visit_count = app_state.visit_count.lock().unwrap();
      let response = format!("{} {} times", health_check_response, visit_count);
      *visit_count += 1;
      HttpResponse::Ok().json(&response)
  }
  
  use super::models::Course;
  use chrono::Utc;
  
  pub async fn new_course(
      new_course: web::Json<Course>,
      app_state: web::Data<AppState>,
  ) -> HttpResponse {
      HttpResponse::Ok().json("Success")
  }
  
  pub async fn get_courses_for_teacher(
      app_state: web::Data<AppState>,
      params: web::Path<(usize, )>,
  ) -> HttpResponse {
      HttpResponse::Ok().json("Success")
  }
  
  pub async fn get_course_detail(
      app_state: web::Data<AppState>,
      params: web::Path<(usize, usize)>,
  ) -> HttpResponse {
      HttpResponse::Ok().json("Success")
  }
  
  #[cfg(test)]
  mod tests {
      use super::*;
      use actix_web::{http::StatusCode, web, App};
      use dotenv::dotenv;
      use sqlx::postgres::PgPoolOptions;
      use std::env;
      use std::sync::Mutex;
  
      #[actix_rt::test]
      async fn post_course_test() {
          dotenv().ok();
          let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
          let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap(); // 创建数据库连接池
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let course = web::Json(Course {
              teacher_id: 1,
              name: "Test course".into(),
              id: None,
              time: None,
          });
          let resp = new_course(course, app_state).await;
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_all_courses_success() {
          dotenv().ok();
          let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
          let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap(); // 创建数据库连接池
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let teacher_id: web::Path<(usize, )> = web::Path::from((1, ));
          let resp = get_courses_for_teacher(app_state, teacher_id).await;
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_one_course_success() {
          dotenv().ok();
          let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
          let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap(); // 创建数据库连接池
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
          
          let params: web::Path<(usize, usize)> = web::Path::from((1, 1));
          let resp = get_course_detail(app_state, params).await;
          assert_eq!(resp.status(), StatusCode::OK);
      }
  }
  
  ```

  ```
  cd ws
  cargo check --bin teacher-service  # 检查
  cargo test --bin teacher-service
  ```

  

- 操作数据库

  ```
  cd webservice/src/
  touch db_access.rs  # 操作数据库
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\db_access.rs


  ```rust
  use super::models::*;
  use chrono::NaiveDateTime;
  use sqlx::postgres::PgPool;
  
  pub async fn get_courses_for_teacher_db(pool: &PgPool, teacher_id: i32) -> Vec<Course> {
      let rows = sqlx::query!(
          r#"select id, teacher_id, name, time
          from course
          where teacher_id = $1"#,
          teacher_id
      )
      .fetch_all(pool)
      .await
      .unwrap();
  
      rows.iter()
          .map(|r| Course {
              id: Some(r.id),
              teacher_id: r.teacher_id,
              name: r.name.clone(),
              time: Some(NaiveDateTime::from(r.time.unwrap())),
          })
          .collect()
  }
  
  pub async fn get_course_details_db(pool: &PgPool, teacher_id: i32, course_id: i32) -> Course {
      let row = sqlx::query!(
          r#"select id, teacher_id, name, time
          from course
          where teacher_id = $1 and id = $2"#,
          teacher_id,
          course_id
      )
      .fetch_one(pool)
      .await
      .unwrap();
  
      Course {
          id: Some(row.id),
          teacher_id: row.teacher_id,
          name: row.name.clone(),
          time: Some(NaiveDateTime::from(row.time.unwrap())),
      }
  }
  
  pub async fn post_new_course_db(pool: &PgPool, new_course: Course) -> Course {
      let row = sqlx::query!(
          r#"insert into course (id, teacher_id, name) 
          values ($1, $2, $3)
          returning id, teacher_id, name, time"#,
          new_course.id,
          new_course.teacher_id,
          new_course.name,
      )
      .fetch_one(pool)
      .await
      .unwrap();
  
      Course {
          id: Some(row.id),
          teacher_id: row.teacher_id,
          name: row.name.clone(),
          time: Some(NaiveDateTime::from(row.time.unwrap())),
      }
  }
  
  ```

  models.rs

  ```rust
  pub struct Course {
      pub teacher_id: i32,
      pub id: Option<i32>,
      pub name: String,
      pub time: Option<NaiveDateTime>,
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\bin\teacher-service.rs

  ```rust
  #[path = "../db_access.rs"]
  mod db_access;
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\handlers.rs

  ```rust
  use super::db_access::*;
  use super::state::AppState;
  use actix_web::{web, HttpResponse};
  
  pub async fn health_check_handler(app_state: web::Data<AppState>) -> HttpResponse {
      let health_check_response = &app_state.health_check_response;
      let mut visit_count = app_state.visit_count.lock().unwrap();
      let response = format!("{} {} times", health_check_response, visit_count);
      *visit_count += 1;
      HttpResponse::Ok().json(&response)
  }
  
  use super::models::Course;
  
  pub async fn new_course(
      new_course: web::Json<Course>,
      app_state: web::Data<AppState>,
  ) -> HttpResponse {
      let course = post_new_course_db(&app_state.db, new_course.into()).await;
      HttpResponse::Ok().json(course)
  }
  
  pub async fn get_courses_for_teacher(
      app_state: web::Data<AppState>,
      params: web::Path<(usize,)>, // xxxx/{teacher_id}
  ) -> HttpResponse {
      let teacher_id = i32::try_from(params.0).unwrap();
      let courses = get_courses_for_teacher_db(&app_state.db, teacher_id).await;
      HttpResponse::Ok().json(courses)
  }
  
  pub async fn get_course_detail(
      app_state: web::Data<AppState>,
      params: web::Path<(usize, usize)>, // xxxx/{teacher_id}/{course_id}
  ) -> HttpResponse {
      let teacher_id = i32::try_from(params.0).unwrap();
      let course_id = i32::try_from(params.1).unwrap();
      let course = get_course_details_db(&app_state.db, teacher_id, course_id).await;
      HttpResponse::Ok().json(course)
  }
  
  #[cfg(test)]
  mod tests {
      use super::*;
      use actix_web::{http::StatusCode, web};
      use dotenv::dotenv;
      use sqlx::postgres::PgPoolOptions;
      use std::env;
      use std::sync::Mutex;
  
      #[actix_rt::test]
      async fn post_course_test() {
          dotenv().ok();
          let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
          let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap(); // 创建数据库连接池
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let course = web::Json(Course {
              teacher_id: 1,
              name: "Test course".into(),
              id: Some(3), // serial
              time: None,
          });
          let resp = new_course(course, app_state).await;
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_all_courses_success() {
          dotenv().ok();
          let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
          let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap(); // 创建数据库连接池
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let teacher_id: web::Path<(usize,)> = web::Path::from((1,));
          let resp = get_courses_for_teacher(app_state, teacher_id).await;
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_one_course_success() {
          dotenv().ok();
          let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
          let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap(); // 创建数据库连接池
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let params: web::Path<(usize, usize)> = web::Path::from((1, 1));
          let resp = get_course_detail(app_state, params).await;
          assert_eq!(resp.status(), StatusCode::OK);
      }
  }
  
  ```

  ```
  cd ws/
  cargo test --bin teacher-service
  
  mv webservice/.env ./
  cargo run
  
  # http://localhost:3000/health
  # http://localhost:3000/courses/1
  # http://localhost:3000/courses/1/2
  
  curl -X POST localhost:3000/courses/ -H "Content-Type: application/json" -d '{"teacher_id":2, "id":7, "name":"Calculus"}'  
  ```

  

### 扩展部分

#### 错误处理

- webSerice中的统一错误处理

  ![](res/Snipaste_2024-03-08_16-47-25.png)

  

  各类编程语言的错误处理方式有两种：

  异常：java

  返回值：rust、go

  

  Rust希望开发者显式的处理错误，因此，可能出错的函数返回Result 枚举类型，其定义如下

  `enum Result<T,E> {ok(T), Err(E),}`

  ```rust
  use std::num::ParseIntError;
  
  fn main() {
      let result = square("ZH"); // Err(ParseIntError { kind: InvalidDigit })
      println!("{:?}", result);
  }
  
  fn square(val: &str) -> Result<i32, ParseIntError> {
      match val.parse::<i32>() {
          Ok(num) => Ok(num.pow(2)),
          Err(e) => Err(e),
      }
  }
  
  ```

  在某函数中使用 `?` 运算符，该运算符尝试从Result 中获取值

  如果不成功，它就会接收Error，中止函数执行，并把错误传播到调用该函数的函数。

  ```rust
  use std::num::ParseIntError;
  
  fn main() {
      let result = square("ZH"); // Err(ParseIntError { kind: InvalidDigit })
      println!("{:?}", result);
  }
  
  fn square(val: &str) -> Result<i32, ParseIntError> {
      let num = val.parse::<i32>()?; // 可能出错的表达式 ?
      Ok(num ^ 2)
  }
  
  ```

  自定义错误类型：多种错误类型的抽象 (枚举enum)

  

  **Actix-Web 把错误转化为 HITP Response**

  Actix-Web定义了一个通用的错误类型(struct)：`actix web::error::Error`，它实现了 `std::error::Error`这个trait

  任何实现了标准库Errortrait的类型，都可以通过`?`运算符，转化为Actix的Error 类型

  Actix的 Error 类型会自动的转化为 HTTP Response，返回给客户端

  

  `ResponseError trait`：任何实现该trait的错误均可转化为HTTP Response 消息

  内置的实现：Actix-Web对于常见错误有内置的实现，例如：

  - Rust 标准 I/O 错误
  - Serde 错误
  - Web错误，例如:ProtocolError、Utf8Error、ParseErrgr等等

  其它错误类型：内置实现不可用时，需要自定义实现错误到 HTTPResponse的转换

  



- 代码实现

  创建自定义错误处理器

  1. 创建一个自定义错误类型

  2. 实现 From trait，用于把其它错误类型转化为该类型

  3. 为自定义错误类型实现 ResponseError trait

  4. 在 handler 里返回自定义错误类型
  5. Actix 会把错误转化为 HTTP 响应

  

  ```
  cd ws/
  touch webservice/src/errors.rs
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\errors.rs

  ```rust
  use actix_web::{error, http::StatusCode, HttpResponse, Result};
  use serde::Serialize;
  use sqlx::error::Error as SQLxError;
  use std::fmt;
  
  #[derive(Debug, Serialize)]
  pub enum MyError {
      DBError(String),
      ActixError(String),
      NotFound(String),
  }
  
  #[derive(Debug, Serialize)]
  pub struct MyErrorResponse {
      error_message: String,
  }
  
  impl MyError {
      fn error_response(&self) -> String {
          match self {
              MyError::DBError(msg) => {
                  println!("Database error occurred: {:?}", msg);
                  "Database error".into()
              }
              MyError::ActixError(msg) => {
                  println!("Server error occurred: {:?}", msg);
                  "Internal server error".into()
              }
              MyError::NotFound(msg) => {
                  println!("Not found error occurred:{:?}", msg);
                  msg.into()
              }
          }
      }
  }
  
  impl error::ResponseError for MyError {
      fn status_code(&self) -> StatusCode {
          match self {
              MyError::DBError(_msg) | MyError::ActixError(_msg) => StatusCode::INTERNAL_SERVER_ERROR,
              MyError::NotFound(_msg) => StatusCode::NOT_FOUND,
          }
      }
      fn error_response(&self) -> HttpResponse {
          HttpResponse::build(self.status_code()).json(MyErrorResponse {
              error_message: self.error_response(),
          })
      }
  }
  
  impl fmt::Display for MyError {
      fn fmt(&self, f: &mut fmt::Formatter) -> Result<(), fmt::Error> {
          write!(f, "{}", self)
      }
  }
  
  impl From<actix_web::error::Error> for MyError {
      fn from(err: actix_web::error::Error) -> Self {
          MyError::ActixError(err.to_string())
      }
  }
  
  impl From<SQLxError> for MyError {
      fn from(err: SQLxError) -> Self {
          MyError::DBError(err.to_string())
      }
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\bin\teacher-service.rs

  ```rust
  #[path = "../errors.rs"]
  mod errors;
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\db_access.rs (三个都要改)

  ```rust
  use super::errors::MyError;
  use super::models::*;
  use chrono::NaiveDateTime;
  use sqlx::postgres::PgPool;
  
  pub async fn get_courses_for_teacher_db(
      pool: &PgPool,
      teacher_id: i32,
  ) -> Result<Vec<Course>, MyError> {
      let rows = sqlx::query!(
          r#"select id, teacher_id, name, time
          from course
          where teacher_id = $1"#,
          teacher_id
      )
      .fetch_all(pool)
      .await?;
  
      let courses: Vec<Course> = rows
          .iter()
          .map(|r| Course {
              id: Some(r.id),
              teacher_id: r.teacher_id,
              name: r.name.clone(),
              time: Some(NaiveDateTime::from(r.time.unwrap())),
          })
          .collect();
      match courses.len() {
          0 => Err(MyError::NotFound("Courses not found for teacher".into())),
          _ => Ok(courses),
      }
  }
  
  pub async fn get_course_details_db(
      pool: &PgPool,
      teacher_id: i32,
      course_id: i32,
  ) -> Result<Course, MyError> {
      let row = sqlx::query!(
          r#"select id, teacher_id, name, time
          from course
          where teacher_id = $1 and id = $2"#,
          teacher_id,
          course_id
      )
      .fetch_one(pool)
      .await;
  
      if let Ok(row) = row {
          Ok(Course {
              id: Some(row.id),
              teacher_id: row.teacher_id,
              name: row.name.clone(),
              time: Some(NaiveDateTime::from(row.time.unwrap())),
          })
      } else {
          Err(MyError::NotFound("Course ID not found".into()))
      }
  }
  
  pub async fn post_new_course_db(pool: &PgPool, new_course: Course) -> Result<Course, MyError> {
      let row = sqlx::query!(
          r#"insert into course (id, teacher_id, name) 
          values ($1, $2, $3)
          returning id, teacher_id, name, time"#,
          new_course.id,
          new_course.teacher_id,
          new_course.name,
      )
      .fetch_one(pool)
      .await?;
  
      Ok(Course {
          id: Some(row.id),
          teacher_id: row.teacher_id,
          name: row.name.clone(),
          time: Some(NaiveDateTime::from(row.time.unwrap())),
      })
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\handlers.rs (三个都要改)

  ```rust
  use super::db_access::*;
  use super::errors::MyError;
  use super::state::AppState;
  use actix_web::{web, HttpResponse};
  
  pub async fn health_check_handler(app_state: web::Data<AppState>) -> HttpResponse {
      let health_check_response = &app_state.health_check_response;
      let mut visit_count = app_state.visit_count.lock().unwrap();
      let response = format!("{} {} times", health_check_response, visit_count);
      *visit_count += 1;
      HttpResponse::Ok().json(&response)
  }
  
  use super::models::Course;
  
  pub async fn new_course(
      new_course: web::Json<Course>,
      app_state: web::Data<AppState>,
  ) -> Result<HttpResponse, MyError> {
      post_new_course_db(&app_state.db, new_course.into())
          .await
          .map(|course| HttpResponse::Ok().json(course))
  }
  
  pub async fn get_courses_for_teacher(
      app_state: web::Data<AppState>,
      params: web::Path<(usize,)>, // xxxx/{teacher_id}
  ) -> Result<HttpResponse, MyError> {
      let teacher_id = i32::try_from(params.0).unwrap();
      get_courses_for_teacher_db(&app_state.db, teacher_id)
          .await
          .map(|courses| HttpResponse::Ok().json(courses))
  }
  
  pub async fn get_course_detail(
      app_state: web::Data<AppState>,
      params: web::Path<(usize, usize)>, // xxxx/{teacher_id}/{course_id}
  ) -> Result<HttpResponse, MyError> {
      let teacher_id = i32::try_from(params.0).unwrap();
      let course_id = i32::try_from(params.1).unwrap();
      get_course_details_db(&app_state.db, teacher_id, course_id)
          .await
          .map(|course| HttpResponse::Ok().json(course))
  }
  
  #[cfg(test)]
  mod tests {
      use super::*;
      use actix_web::{http::StatusCode, web};
      use dotenv::dotenv;
      use sqlx::postgres::PgPoolOptions;
      use std::env;
      use std::sync::Mutex;
  
      #[ignore]
      #[actix_rt::test]
      async fn post_course_test() {
          dotenv().ok();
          let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
          let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap(); // 创建数据库连接池
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let course = web::Json(Course {
              teacher_id: 1,
              name: "Test course".into(),
              id: Some(7), // serial
              time: None,
          });
          let resp = new_course(course, app_state).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_all_courses_success() {
          dotenv().ok();
          let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
          let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap(); // 创建数据库连接池
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let teacher_id: web::Path<(usize,)> = web::Path::from((1,));
          let resp = get_courses_for_teacher(app_state, teacher_id)
              .await
              .unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_one_course_success() {
          dotenv().ok();
          let database_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
          let db_pool = PgPoolOptions::new().connect(&database_url).await.unwrap(); // 创建数据库连接池
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let params: web::Path<(usize, usize)> = web::Path::from((1, 1));
          let resp = get_course_detail(app_state, params).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  }
  
  ```

  

  ```
  cd ws
  cargo test --bin teacher-service get_all_courses_success
  cargo test --bin teacher-service
  ```

  

#### 添加功能并重构

- 项目现状

  ![](res/Snipaste_2024-03-08_18-56-53.png)

  

  项目结构重构：一个文件变成一个文件夹

  ```
  cd ws/
  mkdir webservice/src/models
  mv webservice/src/models.rs webservice/src/models/course.rs
  touch webservice/src/models/mod.rs  
  # pub mod course;  // use crate::models::course::Course;
  
  mkdir webservice/src/handlers
  mv webservice/src/handlers.rs webservice/src/handlers/course.rs
  touch webservice/src/handlers/general.rs  # 健康检查
  touch webservice/src/handlers/mod.rs
  
  mkdir webservice/src/dbaccess
  mv webservice/src/db_access.rs webservice/src/dbaccess/course.rs
  touch webservice/src/dbaccess/mod.rs
  
  
  rm -rf webservice/src/bin/server1.rs  // Cargo.toml 也删去server1
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\bin\teacher-service.rs

  ```rust
  #[path = "../dbaccess/mod.rs"]
  mod dbaccess;
  #[path = "../errors.rs"]
  mod errors;
  #[path = "../handlers/mod.rs"]
  mod handlers;
  #[path = "../models/mod.rs"]
  mod models;
  #[path = "../routers.rs"]
  mod routers;
  #[path = "../state.rs"]
  mod state;
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\handlers\general.rs

  ```rust
  use actix_web::{HttpResponse, web};
  
  use crate::errors::MyError;  // 改绝对引用
  use crate::state::AppState;
  
  
  pub async fn health_check_handler(app_state: web::Data<AppState>) -> HttpResponse {
      let health_check_response = &app_state.health_check_response;
      let mut visit_count = app_state.visit_count.lock().unwrap();
      let response = format!("{} {} times", health_check_response, visit_count);
      *visit_count += 1;
      HttpResponse::Ok().json(&response)
  }
  ```

  

- 添加新字段

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\models\course.rs

  ```rust
  use std::convert::TryFrom;
  
  use actix_web::web;
  use chrono::NaiveDateTime;
  use serde::{Deserialize, Serialize};
  
  use crate::errors::MyError;
  
  
  // 仅作从数据库读取 不需要逆序列化  (sqlx::FromRow 自动映射 不需要实现From)
  #[derive(Serialize, Deserialize, Debug, Clone, sqlx::FromRow)]
  pub struct Course {
      pub teacher_id: i32,
      pub id: i32,
      pub name: String,
      pub time: Option<NaiveDateTime>,
      pub description: Option<String>,
      pub format: Option<String>,
      pub structure: Option<String>,
      pub duration: Option<String>,
      pub price: Option<i32>,
      pub language: Option<String>,
      pub level: Option<String>,
  }
  
  // 新增课程
  #[derive(Deserialize, Debug, Clone)]
  pub struct CreateCourse {
      pub teacher_id: i32,
      pub name: String,
      pub description: Option<String>,
      pub format: Option<String>,
      pub structure: Option<String>,
      pub duration: Option<String>,
      pub price: Option<i32>,
      pub language: Option<String>,
      pub level: Option<String>,
  }
  
  /*impl From<web::Json<CreateCourse>> for CreateCourse {
      fn from(course: web::Json<CreateCourse>) -> Self {
          CreateCourse {
              teacher_id: course.teacher_id,
              name: course.name.clone(),
              description: course.description.clone(),
              format: course.format.clone(),
              structure: course.structure.clone(),
              duration: course.duration.clone(),
              price: course.price,
              language: course.language.clone(),
              level: course.level.clone(),
          }
      }
  }*/
  
  impl TryFrom<web::Json<CreateCourse>> for CreateCourse {
      type Error = MyError;
  
      fn try_from(course: web::Json<CreateCourse>) -> Result<Self, Self::Error> {
          Ok(CreateCourse {
              teacher_id: course.teacher_id,
              name: course.name.clone(),
              description: course.description.clone(),
              format: course.format.clone(),
              structure: course.structure.clone(),
              duration: course.duration.clone(),
              price: course.price,
              language: course.language.clone(),
              level: course.level.clone(),
          })
      }
  }
  
  // 修改课程
  #[derive(Deserialize, Debug, Clone)]
  pub struct UpdateCourse {
      pub name: Option<String>,
      pub description: Option<String>,
      pub format: Option<String>,
      pub structure: Option<String>,
      pub duration: Option<String>,
      pub price: Option<i32>,
      pub language: Option<String>,
      pub level: Option<String>,
  }
  
  impl From<web::Json<UpdateCourse>> for UpdateCourse {
      fn from(course: web::Json<UpdateCourse>) -> Self {
          UpdateCourse {
              name: course.name.clone(),
              description: course.description.clone(),
              format: course.format.clone(),
              structure: course.structure.clone(),
              duration: course.duration.clone(),
              price: course.price,
              language: course.language.clone(),
              level: course.level.clone(),
          }
      }
  }
  
  ```

  修改数据库结构添加字段

  ```sql
  drop table if exists course;
  
  create table course(
      id serial primary key,
      teacher_id int not null,
      name varchar(140) not null,
      time timestamp default now(),
      description varchar(2000),
      format varchar(30),
      structure varchar(200),
      duration varchar(30),
      price int,
      language varchar(30),
      level varchar(30)
  );
  
  insert into
      course(id, teacher_id, name, time)
  values
      (1, 1, 'First course', '2022-01-17 05:40:00'),
      (2, 1, 'Second course', '2022-01-18 05:45:00');
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\dbaccess\course.rs

  ```rust
  use crate::errors::MyError;
  use crate::models::course::{Course, CreateCourse, UpdateCourse};
  use sqlx::postgres::PgPool;
  
  pub async fn get_courses_for_teacher_db(
      pool: &PgPool,
      teacher_id: i32,
  ) -> Result<Vec<Course>, MyError> {
      let rows: Vec<Course> = sqlx::query_as!(
          Course,
          r#"select * from course where teacher_id = $1"#,
          teacher_id
      ).fetch_all(pool).await?;
  
      Ok(rows)
  }
  
  pub async fn get_course_details_db(
      pool: &PgPool,
      teacher_id: i32, course_id: i32,
  ) -> Result<Course, MyError> {
      let row = sqlx::query_as!(
          Course,
          r#"select * from course
          where teacher_id = $1 and id = $2"#,
          teacher_id,
          course_id
      ).fetch_optional(pool).await?;
  
      if let Some(course) = row {
          Ok(course)
      } else {
          Err(MyError::NotFound("Course ID not found".into()))
      }
  }
  
  pub async fn post_new_course_db(
      pool: &PgPool,
      new_course: CreateCourse,
  ) -> Result<Course, MyError> {
      let row = sqlx::query_as!(
          Course,
          r#"insert into course (teacher_id, name, description, format, structure, duration, price, language, level)
          values ($1, $2, $3, $4, $5, $6, $7, $8, $9)
          returning *"#,
          new_course.teacher_id, new_course.name, new_course.description,
          new_course.format, new_course.structure, new_course.duration,
          new_course.price, new_course.language, new_course.level,
      ).fetch_one(pool).await?;
  
      Ok(row)
  }
  
  pub async fn delete_course_db(
      pool: &PgPool,
      teacher_id: i32, id: i32,
  ) -> Result<String, MyError> {
      let course_row = sqlx::query!(
          "delete from course where teacher_id = $1 and id = $2",
          teacher_id,
          id,
      ).execute(pool).await?;
  
      Ok(format!("Delete {:?} record", course_row))
  }
  
  pub async fn update_course_details_db(
      pool: &PgPool,
      teacher_id: i32, id: i32, update_course: UpdateCourse,
  ) -> Result<Course, MyError> {
      let current_course_row = sqlx::query_as!(
          Course,
          "select * from course where teacher_id = $1 and id = $2",
          teacher_id,
          id
      ).fetch_one(pool).await.map_err(|_err| MyError::NotFound("Course ID not found".into()))?;
  
      let name: String = if let Some(name) = update_course.name { name } else { current_course_row.name };
      let description: String = if let Some(desc) = update_course.description { desc } else { current_course_row.description.unwrap_or_default() };
      let format: String = if let Some(format) = update_course.format { format } else { current_course_row.format.unwrap_or_default() };
      let structure: String = if let Some(structure) = update_course.structure { structure } else { current_course_row.structure.unwrap_or_default() };
      let duration: String = if let Some(duration) = update_course.duration { duration } else { current_course_row.duration.unwrap_or_default() };
      let price: i32 = if let Some(price) = update_course.price { price } else { current_course_row.price.unwrap_or_default() };
      let language: String = if let Some(language) = update_course.language { language } else { current_course_row.language.unwrap_or_default() };
      let level: String = if let Some(level) = update_course.level { level } else { current_course_row.level.unwrap_or_default() };
  
      let course_row = sqlx::query_as!(
          Course,
          r#"update course set name = $1, description = $2, format = $3, structure = $4, duration = $5, price = $6, language = $7, level = $8
          where teacher_id = $9 and id = $10
          returning id, teacher_id, name, time, description, format, structure, duration, price, language, level"#,
          name, description, format, structure, duration, price, language, level,
          teacher_id, id
      ).fetch_one(pool).await;
  
      if let Ok(course) = course_row {
          Ok(course)
      } else {
          Err(MyError::NotFound("Course ID not found".into()))
      }
  }
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\routers.rs

  ```rust
  use actix_web::web::{self};
  
  use crate::handlers::{course::*, general::*};
  
  
  pub fn general_routes(cfg: &mut web::ServiceConfig) {
      cfg.route("/health", web::get().to(health_check_handler));
  }
  
  pub fn course_routes(cfg: &mut web::ServiceConfig) {
      cfg.service(web::scope("/courses")
                      .route("/", web::post().to(post_new_course))
                      .route("/{teacher_id}", web::get().to(get_courses_for_teacher))
                      .route("/{teacher_id}/{course_id}", web::get().to(get_course_detail))
                      .route("/{teacher_id}/{course_id}", web::delete().to(delete_course))
                      .route("/{teacher_id}/{course_id}", web::put().to(update_course_details)),
      );
  }
  
  ```

  D:\code\hyz-code-rust\rust_web\ws\webservice\src\handlers\course.rs

  ```rust
  use crate::state::AppState;
  use crate::dbaccess::course::*;
  use crate::errors::MyError;
  use crate::models::course::{CreateCourse, UpdateCourse};
  use actix_web::{web, HttpResponse};
  
  
  pub async fn post_new_course(
      app_state: web::Data<AppState>,
      new_course: web::Json<CreateCourse>,
  ) -> Result<HttpResponse, MyError> {
      post_new_course_db(&app_state.db, new_course.try_into()?)
          .await
          .map(|course| HttpResponse::Ok().json(course))
  }
  
  pub async fn get_courses_for_teacher(
      app_state: web::Data<AppState>,
      params: web::Path<i32>,
  ) -> Result<HttpResponse, MyError> {
      let teacher_id = params.into_inner();
      get_courses_for_teacher_db(&app_state.db, teacher_id)
          .await
          .map(|courses| HttpResponse::Ok().json(courses))
  }
  
  pub async fn get_course_detail(
      app_state: web::Data<AppState>,
      params: web::Path<(i32, i32)>,
  ) -> Result<HttpResponse, MyError> {
      let (teacher_id, course_id) = params.into_inner();
      get_course_details_db(&app_state.db, teacher_id, course_id)
          .await
          .map(|course| HttpResponse::Ok().json(course))
  }
  
  pub async fn delete_course(
      app_state: web::Data<AppState>,
      params: web::Path<(i32, i32)>,
  ) -> Result<HttpResponse, MyError> {
      let (teacher_id, course_id) = params.into_inner();
      delete_course_db(&app_state.db, teacher_id, course_id)
          .await
          .map(|resp| HttpResponse::Ok().json(resp))
  }
  
  pub async fn update_course_details(
      app_state: web::Data<AppState>,
      update_course: web::Json<UpdateCourse>,
      params: web::Path<(i32, i32)>,
  ) -> Result<HttpResponse, MyError> {
      let (teacher_id, course_id) = params.into_inner();
      update_course_details_db(&app_state.db, teacher_id, course_id, update_course.into())
          .await
          .map(|course| HttpResponse::Ok().json(course))
  }
  
  #[cfg(test)]
  mod tests {
      use super::*;
      use actix_web::{http::StatusCode, web, ResponseError};
      use dotenv::dotenv;
      use sqlx::postgres::PgPoolOptions;
      use std::env;
      use std::sync::Mutex;
  
      #[actix_rt::test]
      async fn post_course_test() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let course = web::Json(CreateCourse {
              teacher_id: 1,
              name: "Test course".into(),
              description: Some("This is a course".into()),
              format: None,
              structure: None,
              duration: None,
              price: None,
              language: Some("English".into()),
              level: Some("Beginner".into()),
          });
          let resp = post_new_course(app_state, course).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_all_courses_success() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let teacher_id: web::Path<i32> = web::Path::from(1);
          let resp = get_courses_for_teacher(app_state, teacher_id).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_one_course_success() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let params: web::Path<(i32, i32)> = web::Path::from((1, 1));
          let resp = get_course_detail(app_state, params).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_one_course_failure() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let params: web::Path<(i32, i32)> = web::Path::from((1, 100));
          let resp = get_course_detail(app_state, params).await;
          match resp {
              Ok(_) => println!("Something wrong ..."),
              Err(err) => assert_eq!(err.status_code(), StatusCode::NOT_FOUND),
          }
      }
  
      #[actix_rt::test]
      async fn update_one_course_success() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let update_course = UpdateCourse {
              name: Some("Course name changed".into()),
              description: Some("This is anther test course".into()),
              format: None,
              level: Some("Intermediate".into()),
              price: None,
              duration: None,
              language: Some("Chinese".into()),
              structure: None,
          };
          let params: web::Path<(i32, i32)> = web::Path::from((1, 2));
          let update_param = web::Json(update_course);
          let resp = update_course_details(app_state, update_param, params).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      // [ignore]
      #[actix_rt::test]
      async fn delete_course_success() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let params: web::Path<(i32, i32)> = web::Path::from((1, 3));
          let resp = delete_course(app_state, params).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn delete_course_failure() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let params: web::Path<(i32, i32)> = web::Path::from((1, 101));
          let resp = delete_course(app_state, params).await;
          match resp {
              Ok(_) => println!("Something wrong ..."),
              Err(err) => assert_eq!(err.status_code(), StatusCode::NOT_FOUND),
          }
      }
  }
  
  ```

  ```
  cargo check
  cargo test
  cargo run  # 注释#[ignore]
  
  # http://localhost:3000/health
  # http://localhost:3000/courses/1
  # http://localhost:3000/courses/1/2 
  ```

  

#### 添加教师管理功能 (练习)

- 项目目标

  ![](res/Snipaste_2024-03-09_11-52-52.png)

  

  

  ```
  cd ws/
  touch webservice/src/models/teacher.rs  
  touch webservice/src/handlers/teacher.rs
  touch webservice/src/dbaccess/teacher.rs
  
  # 添加新mod  pub mod teacher;
  ```

  models\teacher.rs

  ```rust
  use actix_web::web;
  use serde::{Deserialize, Serialize};
  
  #[derive(Deserialize, Serialize, Debug, Clone)]
  pub struct Teacher {
      pub id: i32,
      pub name: String,
      pub picture_url: String,
      pub profile: String,
  }
  
  #[derive(Deserialize, Debug, Clone)]
  pub struct CreateTeacher {
      pub name: String,
      pub picture_url: String,
      pub profile: String,
  }
  
  #[derive(Deserialize, Debug, Clone)]
  pub struct UpdateTeacher {
      pub name: Option<String>,
      pub picture_url: Option<String>,
      pub profile: Option<String>,
  }
  
  impl From<web::Json<CreateTeacher>> for CreateTeacher {
      fn from(new_teacher: web::Json<CreateTeacher>) -> Self {
          CreateTeacher {
              name: new_teacher.name.clone(),
              picture_url: new_teacher.picture_url.clone(),
              profile: new_teacher.profile.clone(),
          }
      }
  }
  
  impl From<web::Json<UpdateTeacher>> for UpdateTeacher {
      fn from(update_teacher: web::Json<UpdateTeacher>) -> Self {
          UpdateTeacher {
              name: update_teacher.name.clone(),
              picture_url: update_teacher.picture_url.clone(),
              profile: update_teacher.profile.clone(),
          }
      }
  }
  ```

  数据库

  ```sql
  drop table if exists teacher;
  
  create table teacher(
  	id serial primary key,
      name varchar(100),
      picture_url varchar(200),
      profile varchar(2000)
  );
  
  
  ```

  dbaccess\teacher.rs

  ```rust
  use sqlx::postgres::PgPool;
  use crate::errors::MyError;
  use crate::models::teacher::{Teacher, CreateTeacher, UpdateTeacher};
  
  pub async fn get_all_teachers_db(pool: &PgPool) -> Result<Vec<Teacher>, MyError> {
      let rows = sqlx::query!(
          r#"select id, name, picture_url, profile
          from teacher"#
      ).fetch_all(pool).await?;
  
      let teachers: Vec<Teacher> = rows
          .iter()
          .map(|r| Teacher {
              id: r.id,
              name: r.name.clone().unwrap(),
              picture_url: r.picture_url.clone().unwrap(),
              profile: r.profile.clone().unwrap(),
          })
          .collect();
  
      match teachers.len() {
          0 => Err(MyError::NotFound("No teachers found".into())),
          _ => Ok(teachers),
      }
  }
  
  pub async fn get_teacher_details_db(
      pool: &PgPool,
      teacher_id: i32,
  ) -> Result<Teacher, MyError> {
      let row = sqlx::query!(
          r#"select id, name, picture_url, profile
          from teacher
          where id = $1"#,
          teacher_id
      ).fetch_one(pool).await.map(|r| Teacher {
          id: r.id,
          name: r.name.unwrap(),
          picture_url: r.picture_url.unwrap(),
          profile: r.profile.unwrap(),
      }).map_err(|_err| MyError::NotFound("Teacher ID not found".into()))?;
  
      Ok(row)
  }
  
  pub async fn post_new_teacher_db(
      pool: &PgPool,
      new_teacher: CreateTeacher,
  ) -> Result<Teacher, MyError> {
      let row = sqlx::query!(
          r#"insert into teacher (name, picture_url, profile)
          values ($1, $2, $3) returning id, name, picture_url, profile"#,
          new_teacher.name,
          new_teacher.picture_url,
          new_teacher.profile
      ).fetch_one(pool).await?;
  
      Ok(Teacher {
          id: row.id,
          name: row.name.unwrap(),
          picture_url: row.picture_url.unwrap(),
          profile: row.profile.unwrap(),
      })
  }
  
  pub async fn update_teacher_details_db(
      pool: &PgPool,
      teacher_id: i32, update_teacher: UpdateTeacher,
  ) -> Result<Teacher, MyError> {
      let row = sqlx::query!(
          r#"select id, name, picture_url, profile
          from teacher where id = $1 "#,
          teacher_id
      ).fetch_one(pool).await.map_err(|_err| MyError::NotFound("Teacher ID not found".into()))?;
  
      let temp = Teacher {
          id: row.id,
          name: if let Some(name) = update_teacher.name { name } else { row.name.unwrap() },
          picture_url: if let Some(pic) = update_teacher.picture_url { pic } else { row.picture_url.unwrap() },
          profile: if let Some(profile) = update_teacher.profile { profile } else { row.profile.unwrap() },
      };
  
      let updated_row = sqlx::query!(
          r#"update teacher set name = $1, picture_url = $2, profile = $3
          where id = $4
          returning *"#,
          temp.name, temp.picture_url, temp.profile,
          teacher_id
      ).fetch_one(pool).await.map(|r| Teacher {
          id: r.id,
          name: r.name.unwrap(),
          picture_url: r.picture_url.unwrap(),
          profile: r.profile.unwrap(),
      }).map_err(|_err| MyError::NotFound("Teacher ID not found".into()))?;
  
      Ok(updated_row)
  }
  
  pub async fn delete_teacher_db(
      pool: &PgPool,
      teacher_id: i32,
  ) -> Result<String, MyError> {
      let row = sqlx::query(&format!("delete from teacher where id = {}",teacher_id)).execute(pool).await
          .map_err(|_err| MyError::DBError("Unable to delete teacher".into()));
  
      Ok(format!("Delete {:?} record", row))
  }
  ```

  handlers\teacher.rs

  ```rust
  use crate::dbaccess::teacher::*;
  use crate::errors::MyError;
  use crate::models::teacher::{CreateTeacher, UpdateTeacher};
  use crate::state::AppState;
  use actix_web::{web, HttpResponse};
  
  pub async fn get_all_teachers(
      app_state: web::Data<AppState>
  ) -> Result<HttpResponse, MyError> {
      get_all_teachers_db(&app_state.db)
          .await
          .map(|teachers| HttpResponse::Ok().json(teachers))
  }
  
  pub async fn get_teacher_details(
      app_state: web::Data<AppState>,
      params: web::Path<i32>,
  ) -> Result<HttpResponse, MyError> {
      let teacher_id = params.into_inner();
      get_teacher_details_db(&app_state.db, teacher_id)
          .await
          .map(|teacher| HttpResponse::Ok().json(teacher))
  }
  
  pub async fn post_new_teacher(
      app_state: web::Data<AppState>,
      new_teacher: web::Json<CreateTeacher>,
  ) -> Result<HttpResponse, MyError> {
      post_new_teacher_db(&app_state.db, CreateTeacher::from(new_teacher))
          .await
          .map(|teacher| HttpResponse::Ok().json(teacher))
  }
  
  pub async fn update_teacher_details(
      app_state: web::Data<AppState>,
      params: web::Path<i32>,
      update_teacher: web::Json<UpdateTeacher>,
  ) -> Result<HttpResponse, MyError> {
      let teacher_id = params.into_inner();
      update_teacher_details_db(&app_state.db, teacher_id, UpdateTeacher::from(update_teacher))
          .await
          .map(|teacher| HttpResponse::Ok().json(teacher))
  }
  
  pub async fn delete_teacher(
      app_state: web::Data<AppState>,
      params: web::Path<i32>,
  ) -> Result<HttpResponse, MyError> {
      let teacher_id = params.into_inner();
      delete_teacher_db(&app_state.db, teacher_id)
          .await
          .map(|teacher| HttpResponse::Ok().json(teacher))
  }
  
  #[cfg(test)]
  mod tests {
      use super::*;
      use actix_web::http::StatusCode;
      use dotenv::dotenv;
      use sqlx::postgres::PgPoolOptions;
      use std::env;
      use std::sync::Mutex;
  
      #[actix_rt::test]
      async fn get_all_teachers_success_test() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let resp = get_all_teachers(app_state).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn get_tutor_detail_success_test() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let params: web::Path<i32> = web::Path::from(2);
          let resp = get_teacher_details(app_state, params).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      // #[ignore]
      #[actix_rt::test]
      async fn post_teacher_success_test() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let new_teacher = CreateTeacher {
              name: "Third Teacher".into(),
              picture_url: "http:yangxu/pro".into(),
              profile: "A teacher in Machine Learning".into(),
          };
          let teacher_param = web::Json(new_teacher);
          let resp = post_new_teacher(app_state, teacher_param).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK);
      }
  
      #[actix_rt::test]
      async fn delete_teacher_success_test() {
          dotenv().ok();
          let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set.");
          let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap();
          let app_state: web::Data<AppState> = web::Data::new(AppState {
              health_check_response: "".to_string(),
              visit_count: Mutex::new(0),
              db: db_pool,
          });
  
          let params: web::Path<i32> = web::Path::from(3);
          let resp = delete_teacher(app_state, params).await.unwrap();
          assert_eq!(resp.status(), StatusCode::OK)
      }
  }
  ```

  routers.rs

  ```rust
  use actix_web::web::{self};
  
  use crate::handlers::{course::*, general::*, teacher::*};
  
  
  pub fn general_routes(cfg: &mut web::ServiceConfig) {
      cfg.route("/health", web::get().to(health_check_handler));
  }
  
  pub fn course_routes(cfg: &mut web::ServiceConfig) {
      cfg.service(web::scope("/courses")
                      .route("/", web::post().to(post_new_course))
                      .route("/{teacher_id}", web::get().to(get_courses_for_teacher))
                      .route("/{teacher_id}/{course_id}", web::get().to(get_course_details))
                      .route("/{teacher_id}/{course_id}", web::delete().to(delete_course))
                      .route("/{teacher_id}/{course_id}", web::put().to(update_course_details)),
      );
  }
  
  pub fn teacher_routes(cfg: &mut web::ServiceConfig) {
      cfg.service(web::scope("/teachers")
                      .route("/", web::post().to(post_new_teacher))
                      .route("/", web::get().to(get_all_teachers))
                      .route("/{teacher_id}", web::get().to(get_teacher_details))
                      .route("/{teacher_id}", web::delete().to(delete_teacher))
                      .route("/{teacher_id}", web::put().to(update_teacher_details)),
      );
  }
  ```

  bin\teacher-service.rs

  ```rust
  use actix_web::{web, App, HttpServer};
  use std::io;
  use std::sync::Mutex;
  
  use dotenv::dotenv;
  use sqlx::postgres::PgPoolOptions;
  use std::env;
  
  #[path = "../dbaccess/mod.rs"]
  mod dbaccess;
  #[path = "../errors.rs"]
  mod errors;
  #[path = "../handlers/mod.rs"]
  mod handlers;
  #[path = "../models/mod.rs"]
  mod models;
  #[path = "../routers.rs"]
  mod routers;
  #[path = "../state.rs"]
  mod state;
  
  use routers::*;
  use state::AppState;
  use crate::errors::MyError;
  
  #[actix_rt::main]
  async fn main() -> io::Result<()> {
      dotenv().ok();
      let db_url = env::var("DATABASE_URL").expect("DATABASE_URL is not set."); // 读取数据库连接信息
      let db_pool = PgPoolOptions::new().connect(&db_url).await.unwrap(); // 创建数据库连接池
  
      let shared_data = web::Data::new(AppState {
          health_check_response: "I'm OK.".to_string(),
          visit_count: Mutex::new(0),
          // courses: Mutex::new(vec![]),
          db: db_pool, // 数据库连接池
      });
      let app = move || {
          App::new()
              .app_data(shared_data.clone())
              .app_data(web::JsonConfig::default().error_handler(|_err, _req| {
                  MyError::InvalidInput("Please provide valid Json input".to_string()).into()
              }))
              .configure(general_routes)
              .configure(course_routes)
              .configure(teacher_routes)
      };
      HttpServer::new(app).bind("127.0.0.1:3000")?.run().await
  }
  ```

  errors.rs

  ```rust
  use actix_web::{error, http::StatusCode, HttpResponse, Result};
  use serde::Serialize;
  use sqlx::error::Error as SQLxError;
  use std::fmt;
  
  #[derive(Debug, Serialize)]
  pub enum MyError {
      DBError(String),
      ActixError(String),
      NotFound(String),
      InvalidInput(String),  // 用户的非法输入
  }
  
  #[derive(Debug, Serialize)]
  pub struct MyErrorResponse {
      error_message: String,
  }
  
  impl MyError {
      fn error_response(&self) -> String {
          match self {
              MyError::DBError(msg) => {
                  println!("Database error occurred: {:?}", msg);
                  "Database error".into()
              }
              MyError::ActixError(msg) => {
                  println!("Server error occurred: {:?}", msg);
                  "Internal server error".into()
              }
              MyError::NotFound(msg) => {
                  println!("Not found error occurred:{:?}", msg);
                  msg.into()
              }
              MyError::InvalidInput(msg) => {
                  println!("Invalid parameters received: {:?}", msg);
                  msg.into()
              }
          }
      }
  }
  
  impl error::ResponseError for MyError {
      fn status_code(&self) -> StatusCode {
          match self {
              MyError::DBError(_msg) | MyError::ActixError(_msg) => StatusCode::INTERNAL_SERVER_ERROR,
              MyError::NotFound(_msg) => StatusCode::NOT_FOUND,
              MyError::InvalidInput(_msg) => StatusCode::BAD_REQUEST,
          }
      }
      fn error_response(&self) -> HttpResponse {
          HttpResponse::build(self.status_code()).json(MyErrorResponse {
              error_message: self.error_response(),
          })
      }
  }
  
  impl fmt::Display for MyError {
      fn fmt(&self, f: &mut fmt::Formatter) -> Result<(), fmt::Error> {
          write!(f, "{}", self)
      }
  }
  
  impl From<actix_web::error::Error> for MyError {
      fn from(err: actix_web::error::Error) -> Self {
          MyError::ActixError(err.to_string())
      }
  }
  
  impl From<SQLxError> for MyError {
      fn from(err: SQLxError) -> Self {
          MyError::DBError(err.to_string())
      }
  }
  ```

  

  ```
  cargo test teacher
  cargo run
  ```

  

#### 服务端webapp应用

- 在服务端把页面渲染好、把数据传给客户端

  技术实现：模板引擎Tera

  ```
  cd ws
  cargo new webapp && cd webapp
  touch .env
  HOST_PORT=127.0.0.1:8080  # 服务器的ip和端口
  
  
  rm -rf ./src/main.rs
  mkdir ./static ./src/bin 
  cd src/ && touch errors.rs handlers.rs mod.rs models.rs routers.rs bin/svr.rs
  cd ../../static && mkdir css && touch register.html teachers.html css/register.css
  ```

  D:\code\hyz-code-rust\rust_web\ws\Cargo.toml

  ```toml
  [workspace]
  resolver = "1"
  members = [ "webapp","webservice"]
  ```

  D:\code\hyz-code-rust\rust_web\ws\webapp\Cargo.toml

  ```toml
  [package]
  name = "webapp"
  version = "0.1.0"
  edition = "2021"
  default-run = "svr"
  
  # See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
  
  [dependencies]
  actix-files = "0.6.0-beta.16"
  actix-web = "4.0.0-rc.2"
  awc = "3.0.0-beta.21"
  dotenv = "0.15.0"
  serde = { version = "1.0.136", features = ["derive"] }
  serde_json = "1.0.79"
  tera = "1.15.0"
  
  [[bin]]
  name = "svr"
  
  ```

  

  列出所有老师、注册一个老师

  \src\bin\models.rs (给页面用的view model)

  ```rust
  use serde::{Deserialize, Serialize};
  
  #[derive(Serialize, Deserialize, Debug)]
  pub struct TeacherRegisterForm {
      pub name: String,
      pub picture_url: String,
      pub profile: String,
  }
  
  #[derive(Serialize, Deserialize, Debug)]
  pub struct TeacherResponse {
      pub id: i32,
      pub name: String,
      pub picture_url: String,
      pub profile: String,
  }
  ```

  \src\bin\routers.rs

  ```rust
  use crate::handlers::{get_all_teachers, show_register_form, handle_register};
  use actix_files as fs;
  use actix_web::web;
  
  pub fn app_config(config: &mut web::ServiceConfig) {
      config.service(
          web::scope("")
              .service(fs::Files::new("/static", "./static").show_files_listing())
              .service(web::resource("/").route(web::get().to(get_all_teachers)))
              .service(web::resource("/register").route(web::get().to(show_register_form)))
              .service(web::resource("/register-post").route(web::post().to(handle_register))),
      );
  }
  ```

  \src\handlers.rs

  ```rust
  use crate::errors::MyError;
  use crate::models::{TeacherRegisterForm, TeacherResponse};
  use actix_web::{web, Error, HttpResponse, Result};
  use serde_json::json;
  
  
  pub async fn get_all_teachers(
      tmpl: web::Data<tera::Tera>
  ) -> Result<HttpResponse, Error> {
      let awc_client = awc::Client::default();
  
      let res = awc_client
          .get("http://localhost:3000/teachers/").send().await.unwrap()
          .json::<Vec<TeacherRegisterForm>>().await.unwrap();
  
      let mut ctx = tera::Context::new();
      ctx.insert("error", "");
      ctx.insert("teachers", &res);
  
      let s = tmpl.render("teachers.html", &ctx)
          .map_err(|_| MyError::TeraError("Template error".to_string()))?;
      Ok(HttpResponse::Ok().content_type("text/html").body(s))
  }
  
  pub async fn show_register_form(
      tmpl: web::Data<tera::Tera>
  ) -> Result<HttpResponse, Error> {
      let mut ctx = tera::Context::new();
      ctx.insert("error", "");
      ctx.insert("current_name", "");
      ctx.insert("current_imageurl", "");
      ctx.insert("current_profile", "");
  
      let s = tmpl.render("register.html", &ctx)
          .map_err(|_| MyError::TeraError("Template error".to_string()))?;
      Ok(HttpResponse::Ok().content_type("text/html").body(s))
  }
  
  pub async fn handle_register(
      tmpl: web::Data<tera::Tera>,
      params: web::Form<TeacherRegisterForm>,
  ) -> Result<HttpResponse, Error> {
      let mut ctx = tera::Context::new();
      let s;
      if params.name == "Dave" {
          ctx.insert("error", "Dave is already exists!");
          ctx.insert("current_name", &params.name);
          ctx.insert("current_picture_url", &params.picture_url);
          ctx.insert("current_profile", &params.profile);
          s = tmpl.render("register.html", &ctx)
              .map_err(|err| MyError::TeraError(err.to_string()))?;
      } else {
          let new_teacher = json!({
              "name": &params.name,
              "picture_url": &params.picture_url,
              "profile": &params.profile,
          });
          let awc_client = awc::Client::default();
          let res = awc_client
              .post("http://localhost:3000/teachers/").send_json(&new_teacher).await.unwrap()
              .body().await?;
          let teacher_response: TeacherResponse = serde_json::from_str(&std::str::from_utf8(&res)?)?;
          s = format!("Congratulations! Your Id is: {}", teacher_response.id);
      }
  
      Ok(HttpResponse::Ok().content_type("text/html").body(s))
  }
  ```

  \src\errors.rs

  ```rust
  use actix_web::{error, http::StatusCode, HttpResponse, Result};
  use serde::Serialize;
  use std::fmt;
  
  #[allow(dead_code)]
  #[derive(Debug, Serialize)]
  pub enum MyError {
      ActixError(String),
      NotFound(String),
      TeraError(String),
  }
  
  #[derive(Debug, Serialize)]
  pub struct MyErrorResponse {
      error_message: String,
  }
  
  impl std::error::Error for MyError {}
  
  impl MyError {
      fn error_response(&self) -> String {
          match self {
              MyError::ActixError(msg) => {
                  println!("Server error occurred: {:?}", msg);
                  "Internal server error".into()
              }
              MyError::NotFound(msg) => {
                  println!("Not found error occurred:{:?}", msg);
                  msg.into()
              }
              MyError::TeraError(msg) => {
                  println!("Error in rendering th template: {:?}", msg);
                  msg.into()
              }
          }
      }
  }
  
  impl error::ResponseError for MyError {
      fn status_code(&self) -> StatusCode {
          match self {
              MyError::ActixError(_msg) | MyError::TeraError(_msg) => StatusCode::INTERNAL_SERVER_ERROR,
              MyError::NotFound(_msg) => StatusCode::NOT_FOUND,
          }
      }
  
      fn error_response(&self) -> HttpResponse {
          HttpResponse::build(self.status_code()).json(MyErrorResponse {
              error_message: self.error_response(),
          })
      }
  }
  
  impl fmt::Display for MyError {
      fn fmt(&self, f: &mut fmt::Formatter) -> Result<(), fmt::Error> {
          write!(f, "{:?}", self)
      }
  }
  
  impl From<actix_web::error::Error> for MyError {
      fn from(err: actix_web::error::Error) -> Self {
          MyError::ActixError(err.to_string())
      }
  }
  ```

  \src\mod.rs

  ```rust
  pub mod errors;
  pub mod handlers;
  pub mod models;
  pub mod routers;
  ```

  \src\bin\svr.rs

  ```rust
  #[path = "../mod.rs"]
  mod wa;
  
  use wa::{errors, handlers, models, routers};
  use routers::app_config;
  use std::env;
  use actix_web::{App, HttpServer, web};
  use dotenv::dotenv;
  use tera::Tera;
  
  
  #[actix_web::main]
  async fn main() -> std::io::Result<()> {
      dotenv().ok();
      let host_port = env::var("HOST_PORT").expect("HOST:PORT address is not exist");
      println!("Listening on: {}", &host_port);
  
      HttpServer::new(move || {
          let tera = Tera::new(concat!(env!("CARGO_MANIFEST_DIR"), "/static/**/*")).unwrap();
          App::new().app_data(web::Data::new(tera)).configure(app_config)
      }).bind(&host_port)?.run().await
  }
  ```

  ```
  cd webapp
  cargo run
  
  cd webservice
  cargo run
  
  # 127.0.0.1:8080
  ```

  D:\code\hyz-code-rust\rust_web\ws\webapp\static\teachers.html

  D:\code\hyz-code-rust\rust_web\ws\webapp\static\register.html

  

#### webAssembly

- 项目全局

  ![](res/Snipaste_2024-03-09_22-04-01.png)

  

  `WebAssembly`是一种新的编码方式，可以在现代浏览器中运行

  它是一种低级的类汇编语言

  具有紧凑的二进制格式

  可以接近原生的性能运行

  并为 C/C ++、C#、Rust 等语言提供一个编译目标，以便它们可以在Web上运

  它也被设计为可以与 JavaScript 共存，允许两者一起工作

  

  机器码：计算机可直接执行的语言

  汇编语言：比较接近机器码

  不同的CPU架构需要不同的机器码和汇编 (x86 x64 arm)

  高级语言可以“翻译”成机器码，以便在CPU上运行

  

  WebAssembly 是**中间编译器目标**

  WebAssembly 其实不是汇编语言，它不针对特定的机器，而是针对浏览器的。

  文本格式：`.wat`、二进制格式：`.wasm`

  

  1







## Rocket

- 参考

  [rocket 官网](https://rocket.rs/)、[rocket 0.5 guide](https://rocket.rs/guide/v0.5/)、[rocket 0.5 API doc](https://api.rocket.rs/v0.5/rocket/)



### 简易学习

- rocket 0.5之前

  支持nightly 不支持stable

  不支持 async await

- rocket 0.5

  实现支持：具体实现 (hyper + tokio)

  和flask风格相似 (热插拔 扩展性)

  



#### hello-world

- 新建项目

  ```bash
  cargo new hello-rocket --bin
  cd hello-rocket
  ```

- 引入依赖 (feature)

  ```toml
  [dependencies]
  rocket = "0.5.0"
  ```

- launching的两种方式

  launch的方式 (官方推荐?)

  ```rust
  #[launch]
  fn rocket() -> _ {...}
  ```

  `rocket::build` (推荐)

  ```rust
  #[rocket::main]
  async fn main() ...
  ```

  

- main.rs (官方推荐?)

  ```rust
  //! 官网文档：https://rocket.rs/v0.5-rc/guide/getting-started/
  //!
  //! 入口主函数是 `rocket()`，它返回一个 `Rocket` 对象，该对象包含了配置和路由信息。
  //!
  //! `Rocket` 对象可以通过 `rocket::build()` 函数来创建，该函数接受一系列配置选项，包括：
  //!
  //! - `address`：监听地址，默认为 `127.0.0.1:8000`
  //! - `workers`：工作线程数，默认为 `num_cpus::get()`
  //! - `log`：日志配置，默认为 `Rocket` 日志格式
  //! - `secret_key`：用于加密 session 和其他敏感数据
  //! - `state`：用于存储全局状态的 `HashMap`
  //! - `limits`：用于配置请求限制，包括上传大小、请求大小、响应大小等
  //! - `tls`：用于配置 TLS/SSL 支持
  //! - `fairings`：用于配置插件
  //! - `mounts`：用于配置路由
  //! - `catchers`：用于配置错误处理器
  //! - `custom`：用于配置自定义配置项
  //!
  //! 路由信息可以通过 `mount()` 方法来添加，该方法接受两个参数：
  //!
  //! - `mount_point`：路由的 URL 前缀
  //! - `routes`：路由函数列表
  //!
  //! 路由函数可以用 `#[get("/path")]`、`#[post("/path")]`、`#[put("/path")]`、`#[delete("/path")]`、`#[patch("/path")]`、`#[options("/path")]`、`#[head("/path")]`、`#[trace("/path")]` 等装饰器来定义，这些装饰器可以将路由映射到指定的路径上。
  //!
  //! 路由函数的返回值可以是以下类型：
  //!
  //! - `String`：返回字符串作为响应
  //! - `&str`：返回字符串切片作为响应
  //! - `() -> T`：返回一个 `Future` 对象，该对象在完成时返回 `T` 类型的值
  //! - `Result<T, E>`：返回一个 `Result` 对象，该对象包含 `T` 类型的值或 `E` 类型的值
  //! - `Response`：返回 `Response` 对象
  //! - `Option<T>`：返回 `Some(T)` 或 `None`
  //! - `T`：返回 `T` 类型的值
  //!
  //! 路由函数也可以返回 `Option<Response>` 来自定义响应，例如，可以根据请求头返回不同的响应。
  
  #[macro_use] extern crate rocket;
  
  #[get("/")]
  fn index() -> &'static str {
      "Hello, rocket!"
  }
  
  #[launch]
  fn rocket() -> _ {
      rocket::build().mount("/", routes![index])
  }
  ```

- main.rs (推荐)

  ```rust
  use rocket::{get, routes};
  
  #[get("/")]
  async fn index() -> &'static str {
      "Hello, rocket!"
  }
  
  #[rocket::main]
  async fn main() -> Result<(), Box<dyn std::error::Error>> {
      rocket::build()
          .mount("/", routes![index])
          .launch().await?;
      Ok(())
  }
  ```



#### restful 和 rocket

- 【案例】user-center 简易版



- restful web api

  `get`：获取 list、single

  `post`：创建未存在

  `put`：修改已存在

  `delete`：删除已存在

  (有的只需要用 `post` 来完成 `put` 和 `delete` 的语义)

- 获取url的参数

  ```rust
  #[get("/user/<id>")]
  fn user_info(id: usize) ...
  ```

- rocket的json模块

  ```rust
  // 引入rocket的json模块
  use rocket::serde::{Serialize, Deserialize};
  use rocket::serde::json::{Json, Value};
  ```

- catchers 报错捕获



- main.ts

  ```rust
  use rocket::{delete, get, post, put, routes};
  
  /// GET  http://127.0.0.1:8000/
  #[get("/")]
  async fn index() -> String {
      "Hello, rocket!".to_string()
  }
  
  /// GET  http://127.0.0.1:8000/user/list
  #[get("/list")]
  async fn user_list() -> String {
      "List of users".to_string()
  }
  
  /// GET  http://127.0.0.1:8000/user/info/123
  #[get("/info/<_id>")]
  async fn user_info(_id: usize) -> String {
      "User info".to_string()
  }
  
  /// POST  http://127.0.0.1:8000/user/add
  #[post("/add")]
  async fn add_user() -> String {
      "User added".to_string()
  }
  
  /// PUT  http://127.0.0.1:8000/user/update/123
  #[put("/update/<_id>")]
  async fn update_user(_id: usize) -> String {
      "User updated".to_string()
  }
  
  /// DELETE  http://127.0.0.1:8000/user/delete/123
  #[delete("/delete/<_id>")]
  async fn delete_user(_id: i32) -> String {
      "User deleted".to_string()
  }
  
  
  #[rocket::main]
  async fn main() -> Result<(), Box<dyn std::error::Error>> {
      rocket::build()
          .mount("/", routes![index])
          .mount("/user", routes![user_list,user_info, add_user, update_user, delete_user])
          .launch().await?;
      Ok(())
  }
  ```

  



### 案例学习











## 基于rust语言的小项目





























## 50 Rust Projects (akhil)

#### compression with rust

- 环境

  ```
  cd akhil
  cargo new compress_rust
  
  ```

- 依赖 Cargo.toml

  ```toml
  [dependencies]
  flate2 = "1.0.24" # for compression
  ```
  
  flate2：压缩库、提供了对DEFLATE压缩算法的高效实现
  
  > 主要特性
  >
  > 1. **高性能**：`flate2`使用了Rust语言的内存安全特性和现代CPU的优化指令，提供了非常高效的压缩和解压缩性能。
  > 2. **灵活性**：库提供了多种压缩级别，从无压缩（级别0）到最大压缩（级别9），用户可以根据需要选择适当的压缩级别。
  > 3. **读写流**：`flate2`支持读写流（`Read`和`Write` trait的实现），这使得它可以很容易地与Rust的标准I/O库集成，用于压缩和解压缩文件或网络数据。
  > 4. **支持多线程**：`flate2`可以在多线程环境中使用，允许压缩和解压缩任务并行执行，进一步提高性能。
  > 5. **内存管理**：由于Rust的所有权和借用机制，`flate2`能够有效地管理内存，避免内存泄漏和不必要的内存分配。
  >
  > 常见用途
  >
  > 1. **文件压缩**：`flate2`可以用来压缩文件，减少存储空间的占用。例如，可以将大型文件压缩成ZIP或GZIP格式。
  > 2. **网络数据传输**：在网络上传输数据时，使用`flate2`压缩数据可以减少传输的带宽需求，提高传输效率。
  > 3. **数据序列化**：在序列化和反序列化数据时，可以先对数据进行压缩，以减少数据的大小，特别是在处理大型数据集时非常有用。
  
  main.rs
  
  ```rust
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
  
  ```
  
  



#### extract zip file

- 环境

  ```
  cd akhil
  cargo new decompress_rust
  
  ```

- 需求

  正确的目录结构

- 依赖 Cargo.toml

  [zipfile官方文档](https://docs.rs/zip/0.5.13/zip/read/struct.ZipFile.html)
  
  ```toml
  [dependencies]
  zip = "0.6.2"
  ```
  
  main.rs
  
  ```rust
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
  
  ```
  
  



#### read csv file

- 环境

  ```
  cd akhil
  cargo new csv-rust
  
  ```

  





#### read json



#### write json











#### get request



#### async await







#### making api calls







#### very basic authentication





#### download images







#### extract links 







#### connect rust and sqlite







#### the best way to connect rust with MongoDB





#### rust Postgres connection





#### rust Postgres operations (create and read)





#### actix web, rhai script + rust





#### blockchain projects that use rust







#### I automated my git workflow with rust











## Tsinghua 程序设计训练 (Rust)

- tsinghua课程安排 (部分)

  [韩文弢](https://pacman.cs.tsinghua.edu.cn/~hanwentao/)、[李国良](https://dbgroup.cs.tsinghua.edu.cn/ligl/index_cn.html)、[刘海龙](http://www.arch.tsinghua.edu.cn/info/rw_fjly/1443)

  1. 程序设计基础（ FOP）：初步掌握一门编程语言（ C++），实现简单算法，体会计算思维——入门
  2. 面向对象程序设计基础（ OOP）：学习面向对象编程的语言特性，学习体会设计思想——提高
  3. 程序设计训练（ P&T）：学习一门新的编程语言（ Rust、 Java 或 Python），体会编程语言的设计理念，锻炼解决问题的能力——融会贯通
  4. 软件工程（ SE）：系统设计，项目管理，团队合作
  5. 操作系统（ OS）：结合计算机系统结构的设计与实现，抽象概念  

- 教学目标  

  语法、语言特性、库

  现代的设计理念 (与c++比较)

  自主解决问题的能力





### 课程介绍与基本语法

- rust：构建可靠且高效的软件  

  **高效 (performance)**：没有运行时和垃圾收集器，代码的运行速度快，内存使用效率高，可用来开发对性能要求高的服务。

  - 运行时：python 解释器、java JVM
  - GC：java方便、但不可控且额外开销 (android java 有时卡)

  **可靠 (reliability)**：用`类型系统`和`所有权模型`来确保内存安全性和线程安全性，在编译时消除各种潜在的问题。

  - c++ 空指针... (埋患 自己追踪)
  - rust：尽可能在编译时消灭

  **好用 (productivity)**：有`丰富的文档`、`友好的编译器`（提供有用的错误信息）和`一流的工具集`，包括集成的包管理器和构建工具、支持各种编辑器的代码自动补全和类型查看功能、代码自动格式化工具等。

  - 关系不大：程序运行1s > 0.1s 
  - 关系很大：开发时间10min > 1day

- 使用场景：命令行工具、网页应用、网络服务、嵌入式开发  

- Rust 编写的软件

  Rust 语言工具链

  Servo 浏览器引擎

  Redox 操作系统

  Linux 内核正在加入用 Rust 语言写驱动和模块的支持

  exa、 bat、 fd 等命令行工具

  rCore 教学操作系统

  MadFS 文件系统  





- Hello World

  ```rust
  //! 知识点：
  //! 函数定义、main 函数、输出（宏调用）、字符串、编译与运行  
  //! 
  //! 编译：rustc main.rs  
  //! 运行：./main  
  
  fn main() {
      println!("Hello, world!");
  }
  ```

  宏 *Macros*：编译之前做的、tooken符号令牌





- 猜数字游戏

  > 通过一个简单的项目演示 Rust 的一些常见功能。项目要求：
  >
  > 程序随机产生一个 1–100 之间的秘密整数 n，让用户来猜。
  >
  > 提示用户，输入一个想猜的数 x。
  >
  > 如果 x = n，则猜数成功，打印祝贺信息并退出程序。
  >
  > 否则，根据 x 和 n 的大小关系输出提示信息，继续让用户来猜。 

   

- `rustc` 编译工具：简单

- `cargo` 构建管理：复杂 (多文件、依赖第三方)

  ```
  cargo new guessing_game
  
  ```

  Cargo.toml 

  项目元信息：`[package]`  项目名称、版本号、作者、许可证

  依赖管理：`[dependencies]`  依赖的外部库(ceate)及其版本
  
  main.rs
  
  ```rust
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
          io::stdin().read_line(&mut guess).expect("Failed to read line");  // 和外界有交流的必须显式处理错误 (防止待定工作)
  
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
  
  ```
  
  







### 所有权与结构化数据









### 标准库







### 泛型、特型与生命周期







### 项目管理与常用库







### 输入输出与网络通信





### 并发编程







### 高级特性与编程语言综述  





















### 【lab】Tsinghua Wordle









### 【lab】Tsinghua OJ









## Tsinghua os rcore













# 【项目】xdiff

- 定位

  命令行工具







# 虚幻5 (c++)

- 安装：

  虚幻引擎、管理器























