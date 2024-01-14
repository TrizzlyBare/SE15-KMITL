fn main() {
    let args: Vec<String> = std::env::args().collect(); 
    let x_arg = if args.len() < 2 { "" } else { &args[1] };
   
    let x: f32 = x_arg.parse().unwrap_or(0.0);
    let fahrenheit = x * (9.0 / 5.0) + 32.0;
    println!("Fahrenheit is: {}", fahrenheit);
} 
