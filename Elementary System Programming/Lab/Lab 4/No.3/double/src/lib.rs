fn count_negative(v: &[i64]) -> usize {
    let mut c = 0;
    for i in c..v.len(){
        if v[i] < 0 {c+=1}
    }
    c 
}


#[test]
fn test_counting() {
    assert_eq!(count_negative(&[]), 0);
    assert_eq!(count_negative(&[1, 2, -3, 4, -6, 7]), 2);
}

fn doubles(v: &[i64]) -> Vec<i64> {
    // v.iter().map(|x| x * 2).collect()
    let mut x = v.clone().to_vec();
    for i in 0..x.len(){
        x[i] *= 2;
    }
    x
}

// fn doubles_recursive(v: &[i64], i: usize) -> Vec<i64> {
//     if index >= v.len() {
//         return Vec::new();
//     }

//     let mut result = doubles_recursive(v, index + 1);
//     result.insert(0, v[index] * 2);
//     result
// }

// fn doubles(v: &[i64]) -> Vec<i64> {
//     doubles_recursive(v, 0)
// }

#[test]
fn test_double() {
    assert_eq!(doubles(&[0]), vec![0]);
    assert_eq!(doubles(&[1, 2, -3, 4, -6, 7]), vec![2, 4, -6, 8, -12, 14]);
}
