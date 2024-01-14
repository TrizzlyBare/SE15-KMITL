fn main() {

    let args: Vec<String> = std::env::args().collect(); 
    let score = if args.len() < 2 { "0" } else { &args[1] };
    let score: i32 = score.trim().parse().expect("invalid");

    if score < 0 {
        print!("Invalid Score\n");
    } else if 0 <= score && score <= 49 {
        print!("Failed with F\n");
    } else if 50 <= score && score <= 60 {
        print!("D\n");
    } else if 61 <= score && score <= 70 {
        print!("C\n");
    } else if 71 <= score && score <= 80 {
        print!("B\n");
    } else if 81 <= score && score <= 94 {
        print!("A\n");
    } else if 95 <= score && score <= 100{
        print!("Excellent with A+\n");
    } else {
        print!("Invalid Score")
    }
}
