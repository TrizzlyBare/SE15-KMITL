fn make_arrow2(size: i32) -> String {
    let mut result = String::new();

    match size {
        s if s > 0 => {
            for i in 1..=size * 2 - 1 {
                let line_size = if i <= size { i } else { size * 2 - i };
                let spaces = size - line_size;

                for _ in 0..spaces {
                    result.push(' ');
                }

                for _ in 0..line_size {
                    result.push('*');
                }

                result.push('\n');
            }
        }
        _ => {
            result = String::from("Invalid input\n");
        }
    }
    result
}

fn main() {
    print!("{}", make_arrow2(5));
}
