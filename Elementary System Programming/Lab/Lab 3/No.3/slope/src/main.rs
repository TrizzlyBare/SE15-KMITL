fn main() {
    let args: Vec<String> = std::env::args().collect();

    let x1 = args[1].parse().unwrap_or(0.0);
    let x2 = args[2].parse().unwrap_or(0.0);
    let y1 = args[3].parse().unwrap_or(0.0);
    let y2 = args[4].parse().unwrap_or(0.0);

    println!("The slope is {}", (y2 - y1) / (x2 - x1))
}
r