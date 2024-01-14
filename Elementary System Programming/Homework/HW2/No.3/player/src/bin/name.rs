fn main() {
    let args: Vec<String> = std::env::args().collect(); 

    if args.len() < 2 {
        print!("Player 1 : N/A\n");
        print!("Player 2 : N/A\n");
    }
    
    else if args.len() <= 2 {
        print!("Player 1 : {}\n", args[1]);
        print!("Player 2 : N/A\n");
    }
    
    else {
        print!("Player 1 : {}\n", args[1]);
        print!("Player 2 : {}\n", args[2]);
    
    }
      
}



