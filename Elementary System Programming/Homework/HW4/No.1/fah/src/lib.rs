fn fahr_to_cel_v(v: &[f64]) -> Vec<f64> {
    let mut result = Vec::new();
    for &fahr in v {
        let c = (5.0 / 9.0) * (fahr - 32.0);
        result.push(c);
    }
    result
}

#[test]
fn test_double() {
    assert_eq!(fahr_to_cel_v(&[]), vec![]);
    assert_eq!(fahr_to_cel_v(&[0.0, 32.0]), vec![-17.77777777777778, 0.0]);
}

fn fahr_to_cel_v_recursive(v: &[f64]) -> Vec<f64> {
    if v.len() == 0 {
        return Vec::new();
    } else {
        let mut result = fahr_to_cel_v_recursive(&v[..v.len() - 1]).to_vec();
        result.push((5.0 / 9.0) * (v[v.len()-1] - 32.0));
        return result
    }
}

#[test]
fn test_double_recursive() {
    assert_eq!(fahr_to_cel_v_recursive(&[]), vec![]);
    assert_eq!(fahr_to_cel_v_recursive(&[0.0, 32.0]), vec![-17.77777777777778, 0.0]);
}