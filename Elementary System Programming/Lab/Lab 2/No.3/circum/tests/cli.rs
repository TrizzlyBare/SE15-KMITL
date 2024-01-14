use assert_cmd::Command;

type TestResult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn circum() -> TestResult {
    let expected = "Celsius is: -12.222223\n";
    let mut cmd = Command::cargo_bin("celsius").unwrap();
    cmd.args(vec!["10"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}