fn p_bubble_sort_x(list: &mut Vec<(f64, f64)>) {
    let mut swapped = true;
    while swapped {
        swapped = false;
        for i in 1..list.len() {
            if list[i - 1].0 > list[i].0 {
                list.swap(i - 1, i);
                swapped = true;
            }
        }
    }
}

fn p_bubble_sort_y(list: &mut Vec<(f64, f64)>) {
    let mut swapped = true;
    while swapped {
        swapped = false;
        for i in 1..list.len() {
            if list[i - 1].1 < list[i].1 {
                list.swap(i - 1, i);
                swapped = true;
            }
        }
    }
}

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

    p_bubble_sort_x(&mut list);
    println!("{:?}", list);

    p_bubble_sort_y(&mut list);
    println!("{:?}", list);
}
