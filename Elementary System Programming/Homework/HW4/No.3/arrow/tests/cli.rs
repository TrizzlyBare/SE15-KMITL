use assert_cmd::Command;
use std::fs;

type TestResult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn make_arrow1_test() -> TestResult {
    let expected = fs::read_to_string("tests/expected/arrow1.txt")?;
    Command::cargo_bin("make_arrow")?
        .assert()
        .success()
        .stdout(expected);
    Ok(())
}

#[test]
fn make_arrow2_test() -> TestResult {
    let expected = fs::read_to_string("tests/expected/arrow2.txt")?;
    Command::cargo_bin("make_arrow2")?
        .assert()
        .success()
        .stdout(expected);
    Ok(())
}

#[test]
fn make_arrow1_recursive_test() -> TestResult {
    let expected = fs::read_to_string("tests/expected/arrow1.txt")?;
    Command::cargo_bin("make_arrow_recursive")?
        .assert()
        .success()
        .stdout(expected);
    Ok(())
}

#[test]
fn make_arrow2_recursive_test() -> TestResult {
    let expected = fs::read_to_string("tests/expected/arrow2.txt")?;
    Command::cargo_bin("make_arrow2_recursive")?
        .assert()
        .success()
        .stdout(expected);
    Ok(())
}
