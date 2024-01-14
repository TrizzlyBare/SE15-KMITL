
use std::env;
use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();
    let args : Vec<String>  = std::env::args().collect();
    let n: usize = args[1].parse().unwrap_or(0);
 
    let mut count = 0;
    for _ in 0..n {
        let x: f32 = rng.gen_range(-1.0..=1.0);
        let y: f32 = rng.gen_range(-1.0..=1.0);
        let d = (x.powi(2) + y.powi(2)).sqrt();
        if d <= 1.0 {
            count += 1;
        }
    }
    let prob = count as f64 / n as f64;

    let result = prob * 4.0;
    println!("Probability P: {}", result);
}
