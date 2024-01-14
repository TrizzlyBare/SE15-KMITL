//No.2.1
fn pack_number_tuples3(num1: Vec<i32>, num2: Vec<i32>, num3: Vec<i32>) -> Vec<(i32, i32, i32)> {
    let mut result = Vec::new();

    let max_len = num1.len().max(num2.len()).max(num3.len());

    for i in 0..max_len {
        let value1 = if i < num1.len() { num1[i] } else { 0 };
        let value2 = if i < num2.len() { num2[i] } else { 0 };
        let value3 = if i < num3.len() { num3[i] } else { 0 };

        result.push((value1, value2, value3));
    }
    result
}

#[test]
fn pack_number_tuples3_tests() {
    assert_eq!(
        pack_number_tuples3(vec![1, 2], vec![4, 3], vec![5]),
        vec![(1, 4, 5), (2, 3, 0)]
    );
}

//==================================================================================================
//No.2.2
fn pack_number_tuples_s3(num1: Vec<i32>, num2: Vec<i32>, num3: Vec<i32>) -> Vec<(i32, i32, i32)> {
    let mut result = Vec::new();

    let min_len = num1.len().min(num2.len()).min(num3.len());

    for i in 0..min_len {
        let value1 = num1[i];
        let value2 = num2[i];
        let value3 = num3[i];

        result.push((value1, value2, value3));
    }

    result

}

#[test]
fn test_join_strings() {
    assert_eq!(
        pack_number_tuples_s3(vec![1, 2], vec![4, 3], vec![5]), 
        vec![(1, 4, 5)]
    );
}

//==================================================================================================