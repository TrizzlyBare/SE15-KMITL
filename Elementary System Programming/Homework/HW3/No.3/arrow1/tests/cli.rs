use assert_cmd::Command;

#[test]
fn arrow() {
 let mut cmd = Command::cargo_bin("arrow").unwrap();
 cmd.arg("5").assert().success()
 .stdout("*\n**\n***\n****\n*****\n****\n***\n**\n*\n");
}

#[test]
fn re_arrow() {
 let mut cmd = Command::cargo_bin("r_arrow").unwrap();
 cmd.arg("5").assert().success()
 .stdout("    *\n   **\n  ***\n ****\n*****\n ****\n  ***\n   **\n    *\n");
}

