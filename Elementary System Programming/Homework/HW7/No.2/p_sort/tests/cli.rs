use assert_cmd::Command;
use std::fs;

type TestResult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn test_p_sort() -> TestResult {
    let mut cmd = Command::cargo_bin("point_sort")?;
    let expected = fs::read_to_string("tests/expected/out_point_sort.txt")?;
    cmd.args(vec!["2", "3", "1", "4", "5"]).assert().success().stdout(expected);
    Ok(())
}

#[test]
fn test_bubble_sort() -> TestResult {
    let mut cmd = Command::cargo_bin("bubble_point")?;
    let expected = fs::read_to_string("tests/expected/bubble_test.txt")?;
    cmd.args(vec!["2", "1", "5", "3", "4"]).assert().success().stdout(expected);
    Ok(())
}