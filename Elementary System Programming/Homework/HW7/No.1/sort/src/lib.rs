fn sort() {
    let mut args: Vec<String> = std::env::args().collect();
    args.remove(0);
    let mut numbers: Vec<i32> = args.iter().map(|x| x.parse::<i32>().unwrap()).collect();
    numbers.sort_by(|a, b| a.cmp(b));
    println!("Ascending order: {:?}", numbers);
    numbers.sort_by(|a, b| b.cmp(a));
    println!("Descending order: {:?}", numbers);
}

#[test]
fn test_sort() {
    let mut numbers = vec![3, 2, 1, 4, 5];
    numbers.sort_by(|a, b| a.cmp(b));
    assert_eq!(numbers, vec![1, 2, 3, 4, 5]);
    numbers.sort_by(|a, b| b.cmp(a));
    assert_eq!(numbers, vec![5, 4, 3, 2, 1]);
}

//====================================================================================================

fn bubble_sort() {
    let mut args: Vec<String> = std::env::args().collect();
    args.remove(0);
    let mut numbers: Vec<i32> = args.iter().map(|x| x.parse::<i32>().unwrap()).collect();
    let mut swapped = true;
    while swapped {
        swapped = false;
        for i in 1..numbers.len() {
            if numbers[i - 1] > numbers[i] {
                numbers.swap(i - 1, i);
                swapped = true;
            }
        }
    }   
    println!("Ascending order: {:?}", numbers);
    numbers.reverse();
    println!("Descending order: {:?}", numbers);
}

#[test]
fn test_bubble_sort() {
    let mut numbers = vec![3, 2, 1, 4, 5];
    let mut swapped = true;
    while swapped {
        swapped = false;
        for i in 1..numbers.len() {
            if numbers[i - 1] > numbers[i] {
                numbers.swap(i - 1, i);
                swapped = true;
            }
        }
    } 
    
    assert_eq!(numbers, vec![1, 2, 3, 4, 5]);
    numbers.reverse();
    assert_eq!(numbers, vec![5, 4, 3, 2, 1]);
}