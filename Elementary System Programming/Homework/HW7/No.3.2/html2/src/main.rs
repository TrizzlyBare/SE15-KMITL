use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io;
use std::fs;

fn main() -> io::Result<()> {
    let args = env::args().collect::<Vec<String>>();

    let x1: f64 = match args.get(1).and_then(|s| s.parse().ok()) {
        Some(value) => value,
        None => {
            eprintln!("Invalid input");
            return Ok(());
        }
    };
    
    let x2: f64 = match args.get(2).and_then(|s| s.parse().ok()) {
        Some(value) => value,
        None => {
            eprintln!("Invalid input");
            return Ok(());
        }
    };

    let x3: f64 = match args.get(3).and_then(|s| s.parse().ok()) {
        Some(value) => value,
        None => {
            eprintln!("Invalid input");
            return Ok(());
        }
    };

    let template = match fs::read_to_string("xpower.html") {
        Ok(content) => content,
        Err(_) => {
            eprintln!("Error reading HTML template");
            return Ok(());
        }
    };

    let mut table_content = String::new();

    if x2 >= x1 {
        let mut x = x1;
        while x <= x2 {
            let x2_val = x * x;
            let x3_val = x * x * x;
            let formatted_x2 = format!("{:.1}", x2_val);
            let formatted_x3 = format!("{:.1}", x3_val);
            table_content.push_str(&format!("<tr><td>{}</td><td>{}</td><td>{}</td></tr>", x, formatted_x2, formatted_x3));
            x += x3;
            if x3 == 0.0 {
                break;
            }
        }
    } else {
        let mut x = x1;
        while x >= x2 {
            let x2_val = x * x;
            let x3_val = x * x * x;
            let formatted_x2 = format!("{:.1}", x2_val);
            let formatted_x3 = format!("{:.1}", x3_val);
            table_content.push_str(&format!("<tr><td>{}</td><td>{}</td><td>{}</td></tr>", x, formatted_x2, formatted_x3));
            x -= x3;
            if x3 == 0.0 {
                break;
            }
        }
    }

    let result = template.replace("<!-- Content will be inserted here -->", &table_content);
    let mut file = File::create("output.html")?;
    file.write_all(result.as_bytes())?;
    
    Ok(())
}
