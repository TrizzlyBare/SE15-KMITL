fn quote(s: &str, c: char) -> String {
    format!("{}{}{}", c, s, c)
}

// 4.1
fn quote_list(v: &[&str], c: char) -> Vec<String> {
    let mut x = Vec::new(); 
    for i in 0..v.len() {
       x.push(format!("{}{}{}", c , v[i], c)) 
    }
    x
}

#[test]
fn test_quotes() {
    assert_eq!(quote("abcd", '*'), "*abcd*");
    assert_eq!(quote_list(&[""; 0], '*'), &[""; 0]);
    assert_eq!(quote_list(&["abcd", "xyz"], '*'), ["*abcd*", "*xyz*"]);
}

//4.2

fn quote_list_recursive(v: &[&str], c: char) -> Vec<String> {
    if v.len() == 0 {
        return Vec::new();
    } else {
        let mut k = quote_list_recursive(&v[..v.len()-1], c).to_vec();
        k.push(format!("{}{}{}", c , v[v.len()-1], c));
        return k
    }
}

#[test]
fn test_quotes() {
    assert_eq!(quote("abcd", '*'), "*abcd*");
    assert_eq!(quote_list_recursive(&[""; 0], '*'), &[""; 0]);
    assert_eq!(quote_list_recursive(&["abcd", "xyz"], '*'), ["*abcd*", "*xyz*"]);
}
 