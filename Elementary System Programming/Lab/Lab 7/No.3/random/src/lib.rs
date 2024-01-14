use rand::Rng;

fn filter_numbers(num_list: Vec<f64>) -> Vec<f64> {
    let mut result: Vec<f64> = Vec::new();
    for num in num_list {
        if num >= -1.0 && num <= 1.0 {
            result.push(num);
        }
    }
    result
}

#[test]
fn test_filter_numbers() {
    assert_eq!(
        filter_numbers(vec![0.0, 1.0, 2.0, 3.0, 4.0, 5.0]),
        vec![0.0, 1.0]
    );
    assert_eq!(
        filter_numbers(vec![-1.0, -2.0, -3.0, -4.0, -5.0]),
        vec![-1.0]
    );
    assert_eq!(
        filter_numbers(vec![0.0, 1.0, 2.0, 3.0, 4.0, 5.0]),
        vec![0.0, 1.0]
    );
}

//============================================================================

fn gen_numbers(rng: &mut rand::rngs::ThreadRng, n: usize) -> Vec<f64> {
    let mut result: Vec<f64> = Vec::new();
    for _ in 0..n {
        result.push(rng.gen_range(-10.0..=10.0));
    }
    result
}

#[test]
fn test_gen_numbers() {
    let mut rng = rand::thread_rng();
    assert_eq!(gen_numbers(&mut rng, 0).len(), 0);
    assert_eq!(gen_numbers(&mut rng, 10).len(), 10);
}

//============================================================================
