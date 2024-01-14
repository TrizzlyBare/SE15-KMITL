fn arrow2_recursive(v: &[usize]) -> String {
    if v.is_empty() {
        return String::new();
    } else {
        let mut s = String::new();
        let n = v[v.len() - 1];

        for i in 1..=n {
            s.push_str(&" ".repeat(n - i));
            s.push_str(&"*".repeat(2 * i - 1));
            s.push('\n');
        }

        for i in (1..n).rev() {
            s.push_str(&" ".repeat(n - i));
            s.push_str(&"*".repeat(2 * i - 1));
            s.push('\n');
        }

        s
    }
}

#[test]
fn test_arrow2_recursive() {
    assert_eq!(arrow2_recursive(&[]), "");
    assert_eq!(arrow2_recursive(&[1]), "*\n");
    assert_eq!(arrow2_recursive(&[2]), " *\n***\n *\n");
    assert_eq!(arrow2_recursive(&[3]), "  *\n ***\n*****\n ***\n  *\n");
    assert_eq!(arrow2_recursive(&[4]), "   *\n  ***\n *****\n*******\n *****\n  ***\n   *\n");
    assert_eq!(arrow2_recursive(&[5]), "    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n   ***\n    *\n");
}