//No.2.1

fn split_grades(c: Vec<&str>) -> (Vec<&str>, Vec<&str>) {
    let mut grades = Vec::new();
    let mut lower_grades = Vec::new();
    let grade1 = ["A+", "A", "B", "C"];
    let grade2 = ["D", "F"];

    for i in c {
        if grade1.contains(&i) {
            grades.push(i);
        } else if grade2.contains(&i) {
            lower_grades.push(i);
        }
    }

    (grades, lower_grades)
}

#[test]
fn test_split_grades() {
    let grades = vec!["B", "F", "A+", "D", "C"];
    let expected = vec!["B", "A+", "C"];
    let expected_lower = vec!["F", "D"];
    let (result, result_lower) = split_grades(grades.clone());

    assert_eq!(result, expected);
    assert_eq!(result_lower, expected_lower);
}

//----------------------------------------------------------------------------------------------------

//No.2.2

fn split_scores(list: Vec<&i32>) -> (Vec<(&str, &i32)>, Vec<(&str, &i32)>) {
    let mut grades = Vec::new();
    let mut fail = Vec::new();

    for score in list {
        if &95 <= score && score <= &100 {
            grades.push(("Excellent with A+", score));
        } else if &81 <= score && score <= &94 {
            grades.push(("A", score));
        } else if &71 <= score && score <= &80 {
            grades.push(("B", score));
        } else if &61 <= score && score <= &70 {
            grades.push(("C", score));
        } else if &50 <= score && score <= &60 {
            fail.push(("D", score));
        } else if &0 <= score && score <= &49 {
            fail.push(("Failed with F", score));
        } else {
            panic!("Invalid score: {}", score);
        }
    }
    (grades, fail)
}

#[test]
fn test_split_scores() {
    assert_eq!(split_scores(Vec::new()), (vec![], vec![]));
    assert_eq!(
        split_scores(vec![&100, &94, &80, &70, &60, &49]),
        (
            vec![("Excellent with A+", &100), ("A", &94), ("B", &80), ("C", &70)],
            vec![("D", &60), ("Failed with F", &49)]
        )
    );
}
