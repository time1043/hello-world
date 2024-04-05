fn main() {
    println!("hello world");
    another_function(5, 4); // arguments
}

fn another_function(x: i32, y: i32) { // parameters
    println!("the value of x is: {}", x);
    println!("the value of y is: {}", y);
}
