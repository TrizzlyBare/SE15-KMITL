fn main() {
    let mut args = std::env::args().collect::<Vec<String>>();
    let mut list = Vec::new();

    let input: Vec<f64> = args.iter().skip(1)
        .map(|x| x.parse::<f64>().unwrap())
        .collect();

    for i in (0..input.len()).step_by(2) {
        if i + 1 < input.len() {
            list.push((input[i], input[i + 1]));
        }
    }

    let mut list_x = list.clone();
    list_x.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap().then_with(|| a.1.partial_cmp(&b.1).unwrap()));
    println!("{:?}", list_x);

    let mut list_y = list.clone();
    list_y.sort_by(|a, b| b.0.partial_cmp(&a.0).unwrap().then_with(|| b.1.partial_cmp(&a.1).unwrap()));
    println!("{:?}", list_y);
}

