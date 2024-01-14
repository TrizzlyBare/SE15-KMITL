//No.3.1
fn unpack_number_tuples(t: Vec<(i32, i32)>) -> (Vec<i32>, Vec<i32>) {
    let mut num1 = Vec::new();
    let mut num2 = Vec::new();

    for (value1, value2) in t {
        num1.push(value1);
        num2.push(value2);
    }

    (num1, num2)
}

#[test]
fn unpack_number_tuples_tests() {
    assert_eq!(
        unpack_number_tuples(vec![(1, 4), (3, 2), (2, 1)]),
        (vec![1, 3, 2], vec![4, 2, 1])
    );
}

//==================================================================================================

//No.3.2
fn unpack_number_tuples3(t: Vec<(i32, i32, i32)>) -> (Vec<i32>, Vec<i32>, Vec<i32>) {
    let mut num1 = Vec::new();
    let mut num2 = Vec::new();
    let mut num3 = Vec::new();

    for (value1, value2, value3) in t {
        num1.push(value1);
        num2.push(value2);
        num3.push(value3);
    }

    (num1, num2, num3)
}

#[test]
fn unpack_number_tuples3_tests() {
    assert_eq!(
        unpack_number_tuples3(vec![(1, 4, 5), (2, 2, 1)]),
        (vec![1, 2], vec![4, 2], vec![5, 1])
    );
}

//=====================================================v=============================================