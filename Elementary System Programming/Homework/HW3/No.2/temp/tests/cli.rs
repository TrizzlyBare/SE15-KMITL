use assert_cmd::Command;

#[test]
fn fah() {
 let mut cmd = Command::cargo_bin("fah").unwrap();
 cmd.arg("0").arg("40").arg("20").assert().success().stdout("Fahr\tCelcius\n0\t-17.8\n20\t-6.7\n40\t4.4\n");
}

