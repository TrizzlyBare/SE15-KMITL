fn vflip(mut img: Vec<String>) -> Vec<String> {
    img.reverse();
    img
}

fn hflip(img: Vec<String>) -> Vec<String> {
    let mut result = Vec::new();
    let max_len = img.iter().map(|line| line.len()).max().unwrap_or(0);

    for line in img.iter() {
        let mut chars: Vec<char> = line.chars().collect();
        chars.reverse();
        let reversed_line: String = chars.iter().collect();
        let padding = " ".repeat(max_len - line.len());
        result.push(format!("{}{}", padding, reversed_line));
    }
    result
}

#[test]
fn test_img_flip() {
    let emp: Vec<String> = vec![];
    assert_eq!(vflip(emp.clone()), emp);
    assert_eq!(hflip(emp.clone()), emp);

    let data: Vec<String> = vec!["<--".to_string(), "#####".to_string(), "<==".to_string()];

    assert_eq!(
        vflip(data.clone()),
        vec!["<==".to_string(), "#####".to_string(), "<--".to_string(),]
    );

    assert_eq!(
        hflip(data.clone()),
        vec![
            "  --<".to_string(),
            "#####".to_string(),
            "  ==<".to_string(),
        ]
    );
}

//Write functions that concatenate lines of text horizontally and vertically.å
fn vcat(img1: &[String], img2: &[String]) -> Vec<String> {
    let mut vcat_data = img1.to_vec();
    vcat_data.extend_from_slice(img2);
    vcat_data
}

fn hcat(img1: &[String], img2: &[String]) -> Vec<String> {
    let mut hcat_data = Vec::new();
    let max_len = img1.iter().map(|line| line.len()).max().unwrap_or(0);

    for (line1, line2) in img1.iter().zip(img2.iter()) {
        let padding = " ".repeat(max_len - line1.len());
        hcat_data.push(format!("{}{}{}", line1, padding, line2));
    }

    for line in img2.iter().skip(img1.len()) {
        let padding = " ".repeat(max_len);
        hcat_data.push(format!("{}{}", padding, line));
    }

    for line in img1.iter().skip(img2.len()) {
        hcat_data.push(format!("{}", line));
    }   
    hcat_data
}

#[test]
fn test_img_cat() {
    let emp = ["".to_string(); 0];
    assert_eq!(vcat(&emp, &emp), [""; 0]);
    assert_eq!(hcat(&emp, &emp), [""; 0]);

    let data = ["<--", "#####", "<=="].map(|v| v.to_string());
    assert_eq!(vcat(&emp, &data), data);
    assert_eq!(vcat(&data, &emp), data);

    assert_eq!(
        vcat(&data, &data),
        ["<--", "#####", "<==", "<--", "#####", "<=="]
    );
    assert_eq!(
        hcat(&data, &data[..2]),
        [
            "<--  <--",
            "##########",
            "<=="
        ]
    );
    assert_eq!(
        hcat(&data[..2], &data),
        [
            "<--  <--",
            "##########",
            "     <=="
        ]
    );
}
