use assert_cmd::Command;

type TestResult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn grade_aa() -> TestResult {
    let expected = "Excellent with A+\n";
    let mut cmd = Command::cargo_bin("grade").unwrap();
    cmd.args(vec!["96"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}

#[test]
fn grade_a() -> TestResult {
    let expected = "A\n";
    let mut cmd = Command::cargo_bin("grade").unwrap();
    cmd.args(vec!["82"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}

#[test]
fn grade_b() -> TestResult {
    let expected = "B\n";
    let mut cmd = Command::cargo_bin("grade").unwrap();
    cmd.args(vec!["72"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}

#[test]
fn grade_c() -> TestResult {
    let expected = "C\n";
    let mut cmd = Command::cargo_bin("grade").unwrap();
    cmd.args(vec!["62"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}

#[test]
fn grade_d() -> TestResult {
    let expected = "D\n";
    let mut cmd = Command::cargo_bin("grade").unwrap();
    cmd.args(vec!["52"]) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(())
}

#[test]
fn grade_f() {
    let mut cmd = Command::cargo_bin("grade").unwrap();
    cmd.arg("20").assert().success().stdout("Failed with F\n");
}

