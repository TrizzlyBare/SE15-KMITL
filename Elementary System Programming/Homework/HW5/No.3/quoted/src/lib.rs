//No.3.1

fn extract_quoted_words(c: &str) -> Vec<String> {
    let mut result = Vec::new();

    for i in c.split_whitespace() {
        if i.starts_with('*') && i.ends_with('*') {
            result.push((&i[1..i.len() - 1]).to_string());
        }
    }
    return result;
}

#[test]
fn test_extract_quoted_words() {
    assert_eq!(extract_quoted_words(""), Vec::<String>::new());
    assert_eq!(
        extract_quoted_words("C ** *C++* *Java *Python* Rust*"),
        ["", "C++", "Python"]
    );
}

//================================================================================================================================

//No.3.2

fn extract_quoted_words_recursive(c: &[&str]) -> Vec<String> {
    if c.is_empty() {
        return Vec::new();
    } else {
        let mut result = extract_quoted_words_recursive(&c[..c.len() - 1]).to_vec();
        let last_element = c[c.len() - 1];

        if last_element.starts_with('*') && last_element.ends_with('*') {
            let quoted_word = &last_element[1..last_element.len() - 1];

            result.push(quoted_word.to_string());
        }

        return result;
    }
}

#[test]
fn test_extract_quoted_words_recursive() {
    assert_eq!(extract_quoted_words_recursive(&[""]), Vec::<String>::new());
    assert_eq!(
        extract_quoted_words_recursive(&["C", "**", "*C++*", "*Java", "*Python*", "Rust*"]),
        vec!["", "C++", "Python"]
    );
}


