use float_cmp::approx_eq;

#[test]
fn test_float() {
    assert!(approx_eq!(f64, 10.-5. / 3.-2., 5.0000, epsilon = 0.0001));
}

#[test]
fn test2_float() {
    assert!(approx_eq!(f64, -10.-5. / 3.-2., -5.0000, epsilon = 0.0001));
}

#[test]
fn test3_float() {
    assert!(approx_eq!(f64, 0.-5. / 3.-2., 0.0000, epsilon = 0.0001));
}
