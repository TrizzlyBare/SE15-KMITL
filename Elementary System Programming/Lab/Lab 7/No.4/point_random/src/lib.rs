use rand::Rng;

fn filter_points(pt_list: Vec<(f64, f64)>) -> Vec<(f64, f64)> {
    let mut result = Vec::new();
    
    for &(x, y) in &pt_list {
        let d = (x.powi(2) + y.powi(2)).sqrt();
        if d <= 1.0 {
            result.push((x, y));
        }
    }
    result
}
#[test]
fn test_filter_points() {
    assert_eq!(
        filter_points(vec![(0.0, 0.0), (1.0, 1.0), (2.0, 2.0), (3.0, 3.0), (4.0, 4.0), (5.0, 5.0)]),
        vec![(0.0, 0.0)]
    );
    assert_eq!(
        filter_points(vec![(-1.0, 0.0), (-2.0, -2.0), (-3.0, -3.0), (-4.0, -4.0), (-5.0, -5.0)]),
        vec![(-1.0, 0.0)]
    );
}

//============================================================================

fn gen_points(rng: &mut rand::rngs::ThreadRng, n: usize) -> Vec<(f64, f64)> {
    let mut result: Vec<(f64, f64)> = Vec::new();
    for _ in 0..n {
        result.push((rng.gen_range(-1.0..=1.0), rng.gen_range(-1.0..=1.0)));
    }
    result
}

#[test]
fn test_gen_points() {
    let mut rng = rand::thread_rng();
    assert_eq!(gen_points(&mut rng, 0).len(), 0);
    assert_eq!(gen_points(&mut rng, 1).len(), 1);
}

//============================================================================