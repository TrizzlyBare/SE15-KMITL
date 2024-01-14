fn main() {
    let args: Vec<String> = std::env::args().collect();
    let input = if args.len() < 2 { "0" } else { &args[1] };

    match input.trim().parse::<usize>() {
        Ok(size) => {
            for i in 1..=size * 2 - 1 {
                let line_size = if i <= size { i } else { size * 2 - i };
                for _ in 0..line_size {
                    print!("*");
                }
                println!();
            }
        }
        Err(_) => {
            println!("Invalid input");
        }
    }
}