fn main() {
    let args: Vec<String> = std::env::args().collect(); 
    let x_arg = if args.len() < 2 { "" } else { &args[1] };
   
    let x: f32 = x_arg.parse().unwrap_or(0.0);
    let celsius = (5.0 / 9.0) * (x - 32.0);
    println!("Celsius is: {}", celsius);
} 