fn calculate_grade(list: &[i32]) -> Vec<String> {
    let mut result: Vec<String> = Vec::new();

    for i in 0..list.len() {
        if list[i] < 0 {
            result.push("Invalid Score".to_string())
        } else if 0 <= list[i] && list[i] <= 49 {
            result.push("Failed with F".to_string())
        } else if 50 <= list[i] && list[i] <= 60 {
            result.push("D".to_string())
        } else if 61 <= list[i] && list[i] <= 70 {
            result.push("C".to_string())
        } else if 71 <= list[i] && list[i] <= 80 {
            result.push("B".to_string())
        } else if 81 <= list[i] && list[i] <= 94 {
            result.push("A".to_string())
        } else if 95 <= list[i] && list[i] <= 100 {
            result.push("Excellent with A+".to_string())
        } 
    }
    return result;
}

// fn calculate_grade(s: &[i32]) -> Vec<String> {
//     let mut result = Vec::new();

//     for i in 0..s.len(){
//         match s{
//             0..=49 => result.push(("Failed with F").to_string()),
//             50..=60 => result.push(("D").to_string()),
//             61..=70 => result.push(("C").to_string()),
//             71..=80 => result.push(("B").to_string()),
//             81..=94 => result.push(("A").to_string()),
//             95..=100 => result.push(("Excellent with A+").to_string()),
//             _ => result.push(("Invalid Incput").to_string())
//         }
//     }
//     result
// }

#[test]
fn test_calculate_grade() {
    assert_eq!(calculate_grade(&[-1]), &["Invalid Score"]);
    assert_eq!(calculate_grade(&[25]), &["Failed with F"]);
    assert_eq!(calculate_grade(&[55]), &["D"]);
    assert_eq!(calculate_grade(&[65]), &["C"]);
    assert_eq!(calculate_grade(&[75]), &["B"]);
    assert_eq!(calculate_grade(&[85]), &["A"]);
    assert_eq!(calculate_grade(&[98]), &["Excellent with A+"]);
}

fn calculate_grade_recursion(list: &[i32]) -> Vec<String> {
    if list.is_empty() {
        return Vec::new();
    } else {
        let mut result = calculate_grade_recursion(&list[..list.len() - 1]).to_vec();
        let score = list[list.len() - 1];
        
        if score < 0 {
            result.push("Invalid Score".to_string());
        } else if score <= 49 {
            result.push("Failed with F".to_string());
        } else if score <= 60 {
            result.push("D".to_string());
        } else if score <= 70 {
            result.push("C".to_string());
        } else if score <= 80 {
            result.push("B".to_string());
        } else if score <= 94 {
            result.push("A".to_string());
        } else if score <= 100 {
            result.push("Excellent with A+".to_string());
        }
        return result;
    }
}

#[test]

fn test_calculate_grade_recursion() {
    assert_eq!(calculate_grade_recursion(&[-1]), vec!["Invalid Score"]);
    assert_eq!(calculate_grade_recursion(&[25]), vec!["Failed with F"]);
    assert_eq!(calculate_grade_recursion(&[55]), vec!["D"]);
    assert_eq!(calculate_grade_recursion(&[65]), vec!["C"]);
    assert_eq!(calculate_grade_recursion(&[75]), vec!["B"]);
    assert_eq!(calculate_grade_recursion(&[85]), vec!["A"]);
    assert_eq!(calculate_grade_recursion(&[98]), vec!["Excellent with A+"]);
}
