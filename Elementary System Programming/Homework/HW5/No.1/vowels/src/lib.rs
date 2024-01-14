//No.1.1

fn count_vowels(c: &str) -> i32 {
    let mut count = 0;
    let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

    for i in c.chars() {
        if vowels.contains(&i) {
            count += 1;
        }
    }
    count
}

#[test]
fn test_vowels_count1() {
    assert_eq!(count_vowels(""), 0);
    assert_eq!(count_vowels("abEcd"), 2);
    assert_eq!(count_vowels("ab12Exey5 7x8U3y5z"), 4);
    assert_eq!(count_vowels("aeiouAEIOU"), 10);
}

//===========================================================================================================================

//No.1.2

fn count_vowels_recursive(c: &str) -> i32 {
    if c.len() == 0 {
        return 0;
    }

    let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    let ch = c.chars().next().unwrap();

    if vowels.contains(&ch) {
        return 1 + count_vowels_recursive(&c[1..]);
    } else {
        return count_vowels_recursive(&c[1..]);
    }
}

#[test]
fn test_vowels_count_recur() {
    assert_eq!(count_vowels_recursive(""), 0);
    assert_eq!(count_vowels_recursive("abEcd"), 2);
    assert_eq!(count_vowels_recursive("ab12Exey5 7x8U3y5z"), 4);
    assert_eq!(count_vowels_recursive("aeiouAEIOU"), 10);
}

//===========================================================================================================================

//No.1.3

fn count_vowels_v2(c: &str) -> Vec<(&str, i32)> {
    let word = c.split_whitespace();
    let mut v = Vec::new();
    let vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];

    for i in word {
        let mut count = 0;
        for j in i.chars() {
            if vowels.contains(&j) {
                count += 1;
            }
        }
        let t = (i, count);
        v.push(t);
    }
    v
}

#[test]
fn test_vowels_count2() {
    assert_eq!(count_vowels_v2(""), []);
    assert_eq!(
        count_vowels_v2("ab12Exey5 7x8U3y5z"),
        [
            ("ab12Exey5", 3),
            ("7x8U3y5z", 1)
        ] 
    );
    assert_eq!(
        count_vowels_v2("aeiou AEIOU"),
        [
            ("aeiou", 5),
            ("AEIOU", 5)
        ]
    );
}