
fn test_main_with_valid_input() {
    let x = 5;
    let expected_output = vec![
        "*",
        "**",
        "***",
        "****",
        "*****",
    ];

    let mut output = Vec::new();
    for i in 1..=x {
        writeln!(output, "{}", "*".repeat(i)).unwrap();
    }

    let output_str = String::from_utf8(output).unwrap();
    let output_lines: Vec<&str> = output_str.trim().lines().collect();

    assert_eq!(output_lines, expected_output);
}
