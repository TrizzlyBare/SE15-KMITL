//No.4.1

fn pack_number_tuples(num1: Vec<i32>, num2: Vec<i32>) -> Vec<(i32, i32)> {
    let mut result = Vec::new();

    let max_len = num1.len().max(num2.len());

    for i in 0..max_len {
        let value1 = if i < num1.len() { num1[i] } else { 0 };
        let value2 = if i < num2.len() { num2[i] } else { 0 };

        result.push((value1, value2));
    }

    result
}

#[test]
fn test_pack_number_tuples() {
    assert_eq!(pack_number_tuples(vec![], vec![]), vec![]);
    assert_eq!(pack_number_tuples(vec![1], vec![]), vec![(1, 0)]);
    assert_eq!(pack_number_tuples(vec![], vec![2, 3]), vec![(0, 2), (0, 3)]);
    assert_eq!(
        pack_number_tuples(vec![5, 1, 4], vec![2, 3]),
        vec![(5, 2), (1, 3), (4, 0)]
    );
}

//======================================================
//No.4.2

fn pack_number_tuples_s(num1: Vec<i32>, num2: Vec<i32>) -> Vec<(i32, i32)> {
    let mut result = Vec::new();

    let min_len = num1.len().min(num2.len());

    for i in 0..min_len {
        let value1 = num1[i];
        let value2 = num2[i];

        result.push((value1, value2));
    }

    result

}

#[test]
fn test_join_strings() {
    assert_eq!(pack_number_tuples_s(vec![], vec![]), vec![]);
    assert_eq!(pack_number_tuples_s(vec![1], vec![]), vec![]);
    assert_eq!(pack_number_tuples_s(vec![], vec![2, 3]), vec![]);
    assert_eq!(pack_number_tuples_s(vec![5, 1, 4], vec![2, 3]), vec![(5, 2), (1, 3)]);
}
