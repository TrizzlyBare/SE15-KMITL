//No.1.1
fn min_max_avg(c: Vec<f64>) -> (f64, f64, f64) {
    if c.len() == 0 {
        return (0.0, 0.0, 0.0);
    }

    let mut min = c[0];
    let mut max = c[0];
    let mut sum = 0.0;

    for i in &c {
        if *i < min {
            min = *i;
        }
        if *i > max {
            max = *i;
        }
        sum += *i;
    }

    let avg = sum as f64 / c.len() as f64;
    (min as f64, max as f64, avg as f64)
}


#[test]
fn test_min_max_avg_empty() {
    let c: Vec<f64> = Vec::new();
    assert_eq!(min_max_avg(c), (0.0, 0.0, 0.0)); 

    let v = vec![10.0, 5.0, 15.0, 8.0, 20.0];
    assert_eq!(min_max_avg(v), (5.0, 20.0, 11.6));

    let b = vec![-10.0, -5.0, -15.0, -8.0, -20.0];
    assert_eq!(min_max_avg(b), (-20.0, -5.0, -11.6));
}

//==================================================================================================

//No.1.2
fn cal_partial_sums(c: &[isize]) -> Vec<isize> {
    let mut sum = 0;
    let mut result = Vec::new();

    for i in c {
        sum += *i;
        result.push(sum);
    }
    result
}

#[test]
fn test_cal_partial_sums() {
    assert_eq!(cal_partial_sums(&[2, 11, 3, 4, 7]), vec![2, 13, 16, 20, 27]);
} 

//==================================================================================================

fn rep_string(st: &[&str]) -> String {
    let mut result = String::new();
    for &i in st {
        for c in i.chars() {
            if c.is_digit(10) {
                result.push('*');
            } else {
                result.push(c);
            }
        }
    }
    result
}

#[test]
fn test_rep_string() {
    let input = &["abc", "123", "def"];
    let expected = "abc***def".to_string();
    assert_eq!(rep_string(input), expected);

    let input = &["1", "2", "3"];
    let expected = "***".to_string();
    assert_eq!(rep_string(input), expected);

    let input = &["abc", "def", "ghi"];
    let expected = "abcdefghi".to_string();
    assert_eq!(rep_string(input), expected);

    let input: &[&str] = &[];
    let expected = "".to_string();
    assert_eq!(rep_string(input), expected);
}
