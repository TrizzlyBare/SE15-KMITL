use assert_cmd::Command;

type TestResult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn celsius() -> TestResult {
    let expected = "Celsius is: -12.222223\n";
    let mut cmd = Command::cargo_bin("celsius").unwrap();
    cmd.args(vec!["10"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}

#[test]
fn fahrenheit() -> TestResult {
    let expected = "Fahrenheit is: 50\n";
    let mut cmd = Command::cargo_bin("fahrenheit").unwrap();
    cmd.args(vec!["10"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}


