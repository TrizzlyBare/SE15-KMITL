//No.3.1

fn join_strings(strings: &[&str], sep: &st) -> String {
    let mut result = String::new();

    for (i, s) in strings.iter().enumerate() {
        if i > 0 {
            result.push_str(sep);
        }
        result.push_str(s);
    }
    result
}

#[test]
fn test_join_strings() {
    assert_eq!(join_strings(&[], ","), "");
    assert_eq!(join_strings(&["C"], ","), "C");

    let patterns = ["C", "Rust", "C++", "Python"];

    assert_eq!(join_strings(&patterns, ", "), "C, Rust, C++, Python");
    assert_eq!(join_strings(&patterns, ";;"), "C;;Rust;;C++;;Python");
}

//======================================================

//No.3.2

fn join_numbers(numbers: &[i32], sep: &str) -> String {
    let mut result = String::new();

    for (i, s) in numbers.iter().enumerate() {
        if i > 0 {
            result.push_str(sep);
        }
        result.push_str(&s.to_string());
    }
    result
}

#[test]
fn test_join_numbers() {
    assert_eq!(join_numbers(&[], ","), "");
    assert_eq!(join_numbers(&[25], ","), "25");
    
    let patterns = [5, 10, -1, 2];
    
    assert_eq!(join_numbers(&patterns, ", "), "5, 10, -1, 2");
    assert_eq!(join_numbers(&patterns, ";;"), "5;;10;;-1;;2");
}
