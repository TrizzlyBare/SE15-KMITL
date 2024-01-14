use assert_cmd::Command;

type TestResult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn no_input() -> TestResult {
    let expected = "Player 1 : N/A\nPlayer 2 : N/A\n";
    let mut cmd = Command::cargo_bin("name").unwrap();
    cmd.assert().success().stdout(expected);
Ok(())
}

#[test]
fn one_arg() -> TestResult {
    let expected = "Player 1 : Mike\nPlayer 2 : N/A\n";
    let mut cmd = Command::cargo_bin("name").unwrap();
    cmd.args(vec!["Mike"]).assert().success().stdout(expected);
Ok(())
}

#[test]
fn two_arg() -> TestResult {
    let expected = "Player 1 : Mike\nPlayer 2 : Leo\n";
    let mut cmd = Command::cargo_bin("name").unwrap();
    cmd.args(vec!["Mike","Leo"]).assert().success().stdout(expected);
Ok(())
}

#[test]
fn three_arg() -> TestResult {
    let expected = "Player 1 : Mike\nPlayer 2 : Leo\n";
    let mut cmd = Command::cargo_bin("name").unwrap();
    cmd.args(vec!["Mike","Leo","Ralph"]).assert().success().stdout(expected);
Ok(())
}

