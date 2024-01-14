// fn make_arrow1_recursive(size: i32, current: i32) -> String {
//     let mut result = String::new();

//     if current <= size * 2 - 1 {
//         let line_size = if current <= size {
//             current
//         } else {
//             size * 2 - current
//         };

//         for _ in 0..line_size {
//             result.push('*');
//         }

//         result.push('\n');
//         result += &make_arrow1_recursive(size, current + 1);
//     } else if size <= 0 {
//         result = String::from("Invalid input\n");
//     }

//     result
// }

// fn main() {
//     print!("{}", make_arrow1_recursive(4, 1));
// }

fn make_arrow_recursive(size: i32, current: i32, is_increasing: bool) -> String {
    let mut result = String::new();

    if current >= 1 && current <= size * 2 - 1 {
        let line_size = if current <= size {
            current
        } else {
            size * 2 - current
        };

        for _ in 0..line_size {
            result.push('*');
        }

        result.push('\n');

        let next_current = if is_increasing {
            current + 1
        } else {
            current - 1
        };
        result += &make_arrow_recursive(size, next_current, is_increasing);
    } else if size <= 0 {
        result = String::from("Invalid input\n");
    }
    result
}

fn main() {
    print!("{}", make_arrow_recursive(5, 1, true));
}
