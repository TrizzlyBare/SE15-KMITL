use assert_cmd::Command;
use predicates::prelude::*;
use std::fs;

type Testresult = Result<(), Box<dyn std::error::Error>>;

#[test]
fn dies_no_args() -> Testresult { 
    Command::cargo_bin("echor")?
        .assert()
        .failure() 
        .stderr(predicate::str::contains("USAGE"));
Ok(())
}

fn run(args: &[&str], expected_file: &str) -> Testresult { 
    let expected = fs::read_to_string(expected_file)?; 
    Command::cargo_bin("echor")?
        .args(args) 
        .assert() 
        .success() 
        .stdout(expected);
Ok(()) 
}

#[test]
fn hello1() -> Testresult {
    run(&["Hello there"], "tests/expected/hello1.txt") 
}

#[test]
fn hello2() -> Testresult {
    run(&["Hello", "there"], "tests/expected/hello2.txt") 
}

#[test]
fn hello1_no_newline() -> Testresult {
    run(&["Hello  there", "-n"], "tests/expected/hello1.n.txt")
}

#[test]
fn hello2_no_newline() -> Testresult {
    run(&["-n", "Hello", "there"], "tests/expected/hello2.n.txt")
}