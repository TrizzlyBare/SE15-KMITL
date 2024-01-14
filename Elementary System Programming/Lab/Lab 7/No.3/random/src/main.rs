use std::env;
use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();
    let args : Vec<String>  = std::env::args().collect();
    let n: usize = args[1].parse().unwrap_or(0);
 
    let mut count = 0;
    for _ in 0..n {
        let x = rng.gen_range(-10.0..=10.0);
        if x >= -1.0 && x <= 1.0 {
            count += 1;
        }
    }
    let prob = count as f64 / n as f64;

    println!("N = {}", n);
    println!("prob = {}", prob);
}