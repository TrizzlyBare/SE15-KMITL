use assert_cmd::Command;

type TestResult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn area() -> TestResult {
    let expected = "Area: 314.16 \n";
    let mut cmd = Command::cargo_bin("circumference").unwrap();
    cmd.args(vec!["10"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}