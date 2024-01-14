fn make_arrow2_recursive(size: i32, current_line: i32) -> String {
    if current_line > size * 2 - 1 {
        return String::new();
    }

    let line_size = if current_line <= size {
        current_line
    } else {
        size * 2 - current_line
    };
    let spaces = size - line_size;

    let mut line = vec![' '; spaces as usize];
    line.extend(vec!['*'; line_size as usize]);
    line.push('\n');

    line.iter().collect::<String>() + &make_arrow2_recursive(size, current_line + 1)
}

fn main() {
    print!("{}", make_arrow2_recursive(5, 1));
}
