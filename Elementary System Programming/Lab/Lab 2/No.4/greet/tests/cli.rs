use assert_cmd::Command;

type TestResult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn greet() -> TestResult {
    let expected = "Greeting, Bobby!\n";
    let mut cmd = Command::cargo_bin("greet").unwrap();
    cmd.args(vec!["Bobby"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}