use clap::{App, Arg};
use std::error::Error;
use std::fs::File;
use std::io::{self, BufRead, BufReader};

#[derive(Debug)]
pub struct Config {
    files: Vec<String>,
    number_lines: bool,
    number_nonblank_lines: bool,
}

type MyResult<T> = Result<T, Box<dyn Error>>;

// pub fn run(config: Config) -> MyResult<()> {
//     for filename in config.files {
//         match open(&filename) {
//             Err(err) => eprintln!("{}: {}", filename, err),
//             Ok(file) => {
//                 for line_result in file.lines() {
//                     let line = line_result?;
//                     println!("{}", line);
//                     if config.number_lines{
//                         println!("-n {}", line)
//                     };
//                     if config.number_nonblank_lines {  
//                         println!("-n {}", line)
//                     };
//                 }
//             }

//         }
//     }

//     Ok(())
// }

pub fn run(config: Config) -> MyResult<()> {
    for filename in config.files {
        match open(&filename) {
            Err(e) => eprintln!("{}: {}", filename, e),
            Ok(file) => {
                let mut last_num = 0;
                for (line_num, line_result) in file.lines().enumerate() {
                    let line = line_result?;
                    if config.number_lines {
                        println!("{:6}\t{}", line_num + 1, line);
                    } else if config.number_nonblank_lines {
                        if !line.is_empty() {
                            last_num += 1;
                            println!("{:6}\t{}", last_num, line);
                        } else {
                            println!();
                        }
                    } else {
                        println!("{}", line);
                    }
                }
            }
        }
    }
    Ok(())
}


pub fn get_args() -> MyResult<Config> {
    let matches = App::new("catr")
        .version("0.1.0")
        .author("SE15 <se15@kmitl.ac.th>")
        .about("Rust cat")
        .arg(
            Arg::with_name("text")
                .value_name("text")
                .multiple(true)
                .help("Input text"),
        )
        .arg(
            Arg::with_name("omit_newline")
                .short("n")
                .help("Do not print newline"),
        )
        .arg(
            Arg::with_name("omit_newline2")
                .short("b")
                .help("Do not print newline"),
        )
        .get_matches();

    Ok(Config {
        files: matches
            .values_of("text")
            .unwrap_or_default()
            .map(|x| x.to_string())
            .collect(),
        number_lines: matches.is_present("omit_newline"),
        number_nonblank_lines: matches.is_present("omit_newline2"),
    })
}

fn open(filename: &str) -> MyResult<Box<dyn BufRead>> {
    match filename {
        "-" => Ok(Box::new(BufReader::new(io::stdin()))),
        _ => Ok(Box::new(BufReader::new(File::open(filename)?))),
    }
}
