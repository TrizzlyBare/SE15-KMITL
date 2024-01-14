fn count_digits(c: &str) -> i32 {
    let mut count = 0;

    for i in c.chars() {
        if i.is_digit(10) {
            count += 1;
        }
    }
    count
}

#[test]
fn test_digits_count1() {
    assert_eq!(count_digits(""), 0);
    assert_eq!(count_digits("abcd"), 0);
    assert_eq!(count_digits("ab12xy5 7x83y5z"), 7);
    assert_eq!(count_digits("12345"), 5);
}

fn count_digits_recursive(c: &str) -> i32 {
    if c.len() == 0 {
        return 0;
    } else {
        let mut result = count_digits_recursive(&c[..c.len() - 1]);
        if c.chars().last().expect("LAST").is_digit(10) {
            result += 1;
        }
        result
    }
}

#[test]
fn test_digits_count_recursive() {
    assert_eq!(count_digits(""), 0);
    assert_eq!(count_digits("abcd"), 0);
    assert_eq!(count_digits("ab12xy5 7x83y5z"), 7);
    assert_eq!(count_digits("12345"), 5);
}

fn count_digits_v2(c: &str) -> Vec<(&str, i64)> {
    let word = c.split_whitespace();
    let mut v = Vec::new();

    for i in word {
        let mut count = 0;
        for j in i.chars() {
            if j.is_digit(10) {
                count += 1;
            }
        }
        let mut t = (i, count);
        v.push(t);
    }
    v
}

#[test]
fn test_digits_count2() {
    assert_eq!(count_digits_v2(""), []);
    assert_eq!(
        count_digits_v2("ab12xy5 7x83y5z"),
        [
            ("ab12xy5", 3), // '1', '2', '5'
            ("7x83y5z", 4)  // '7', '8', '3', '5'
        ]
    );
}

