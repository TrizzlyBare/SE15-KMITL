fn main() {
    let args: Vec<String> = std::env::args().collect();
    let x: usize = args[1].parse().unwrap_or(0);
    for i in 1..=x{
        println!("{}", "*".repeat(i))
    }
}
