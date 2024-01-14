use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io;
use std::fs;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();

    let fahr1: f64 = match args.get(1).and_then(|s| s.parse().ok()) {
        Some(value) => value,
        None => {
            eprintln!("Invalid input");
            return Ok(());
        }
    };

    let fahr2: f64 = match args.get(2).and_then(|s| s.parse().ok()) {
        Some(value) => value,
        None => {
            eprintln!("Invalid input");
            return Ok(());
        }
    };

    let fahr3: f64 = match args.get(3).and_then(|s| s.parse().ok()) {
        Some(value) => value,
        None => {
            eprintln!("Invalid input");
            return Ok(());
        }
    };

    let template = match fs::read_to_string("column.html") {
        Ok(content) => content,
        Err(_) => {
            eprintln!("Error reading HTML template");
            return Ok(());
        }
    };

    let mut table_content = String::new();

    if fahr2 >= fahr1 {
        let mut fahr = fahr1;
        while fahr <= fahr2 {
            let c = (5.0 / 9.0) * (fahr - 32.0);
            let formatted_c = format!("{:.1}", c);
            table_content.push_str(&format!("<tr><td>{}</td><td>{}</td></tr>", fahr, formatted_c));
            fahr += fahr3;
            if fahr3 == 0.0 {
                break;
            }
        }
    } else {
        let mut fahr = fahr1;
        while fahr >= fahr2 {
            let c = (5.0 / 9.0) * (fahr - 32.0);
            let formatted_c = format!("{:.1}", c);
            table_content.push_str(&format!("<tr><td>{}</td><td>{}</td></tr>", fahr, formatted_c));
            fahr -= fahr3;
            if fahr3 == 0.0 {
                break;
            }
        }
    }

    let result = template.replace("<!-- Content will be inserted here -->", &table_content);

    let mut file = File::create("output.html")?;
    file.write_all(result.as_bytes())?;

    Ok(())
}
