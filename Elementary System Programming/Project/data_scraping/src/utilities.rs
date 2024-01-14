use regex::Regex;

const OUTPUT_HTML_PATH: &str = "output.html";

use reqwest;
use std::error::Error;
use std::fs;
use std::io;
use std::io::Write;

pub fn get_user_input_link() -> Result<String, io::Error> {
    loop {
        print!("Enter the link to the website you want to scrape / Press 'q' for quitting: ");
        io::stdout().flush()?;
        let mut link = String::new();
        io::stdin().read_line(&mut link)?;

        let trimmed_link = link.trim();
        if trimmed_link.is_empty() {
            println!("Please provide a valid link.");
        } else if trimmed_link == "q" {
            println!("Quitting...");
            std::process::exit(0);
        } else {
            return Ok(trimmed_link.to_string());
        }
    
    }
}

pub async fn get_html_data(link: &str) -> Result<String, Box<dyn Error>> {
    let file_exists = fs::metadata(OUTPUT_HTML_PATH).is_ok();

    if file_exists {
        fs::remove_file(OUTPUT_HTML_PATH)?;
    }

    let res = request(link).await?;

    if res.status().is_success() {
        println!("Status code: {}", res.status());

        let body = res.text().await?;
        let cleaned_html = remove_unuseful_chars(&body);
        save_data_to_file(&cleaned_html, OUTPUT_HTML_PATH, "HTML")?;

        Ok(cleaned_html)
    } else {
        println!("Request was not successful: {}", res.status());
        Ok("".to_string())
    }
}

pub fn file_type_selection() -> Result<String, io::Error> {
    loop {
        print!("Enter the file type you want to save the data to (JSON (1) / CSV (2) / XML (3) / TOML (4) / YAML (5) / MessagePack (6) / Quit the Program (q)): ");
        io::stdout().flush()?;
        let mut file_type = String::new();
        io::stdin().read_line(&mut file_type)?;

        let trimmed_file_type = file_type.trim();
        if !(1..=6).any(|x| trimmed_file_type == x.to_string()) {
            println!("Please enter a valid file type (1-6).");
        } else if trimmed_file_type == "q" {
            println!("Quitting...");
            std::process::exit(0);
        } else {
            return Ok(trimmed_file_type.to_string());
        }
    }
}

pub fn save_data_to_file(data: &str, file_path: &str, file_type: &str) -> Result<(), io::Error> {
    fs::write(file_path, data)?;
    println!("Data saved to {}: {}", file_path, file_type);
    Ok(())
}


pub async fn request(link: &str) -> Result<reqwest::Response, reqwest::Error> {
    let client = reqwest::Client::new();
    let res = client.get(link).send().await?;
    Ok(res)
}

pub fn remove_unuseful_chars(text: &str) -> String {
    let mut cleaned_text = text
        .replace("\n", " ")
        .replace("\t", " ")
        .replace("\r", " ");

    let re1 = Regex::new(r"\{[^{}]*\}").unwrap();
    cleaned_text = re1.replace_all(&cleaned_text, " ").to_string();

    let re2 = Regex::new(r"css[^{}]*hover").unwrap();
    cleaned_text = re2.replace_all(&cleaned_text, " ").to_string();

    cleaned_text = Regex::new(r" +")
        .unwrap()
        .replace_all(&cleaned_text, " ")
        .to_string();

    cleaned_text
}