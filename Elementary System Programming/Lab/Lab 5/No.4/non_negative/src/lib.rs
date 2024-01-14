fn extract_non_negatives(c: Vec<f64>) -> Vec<f64> {
    let mut v = Vec::new();

    for i in c {
        if i >= 0.0 {
            v.push(i);
        }
    }
    v
}

#[test]
fn test_extract_non_negatives() {
    assert_eq!(extract_non_negatives(vec![]), []);
    assert_eq!(extract_non_negatives(vec![0.8, -5.1, 1.6, -6.5, 10.5]), [0.8, 1.6, 10.5]);
}

fn extract_non_negatives_recursive(c: Vec<f64>) -> Vec<f64> {
    if c.is_empty() {
        return Vec::new();
    } else {
        let mut result = extract_non_negatives_recursive((&c[..c.len() - 1]).to_vec());
        if c[c.len() - 1] >= 0.0 {
            result.push(c[c.len() - 1]);
        }
        result
    }
}

#[test]
fn test_extract_non_negatives_recursive() {
    assert_eq!(extract_non_negatives_recursive(vec![]), []);
    assert_eq!(extract_non_negatives_recursive(vec![0.8, -5.1, 1.6, -6.5, 10.5]), [0.8, 1.6, 10.5]);
}

fn split_non_negatives(c: Vec<f64>) -> (Vec<f64>, Vec<f64>) {
    let mut v = Vec::new();
    let mut q = Vec::new();

    for i in c {
        if i >= 0.0 {
            v.push(i);
        } else {
            q.push(i);
        }
    }
    return (v, q);
}

#[test]
fn test_split_non_negatives() {
    assert_eq!(split_non_negatives(vec![]), (vec![], vec![]));
    assert_eq!(split_non_negatives(vec![0.8, -5.1, 1.6, -6.5, 10.5]), (vec![0.8, 1.6, 10.5], vec![-5.1, -6.5]));
}
