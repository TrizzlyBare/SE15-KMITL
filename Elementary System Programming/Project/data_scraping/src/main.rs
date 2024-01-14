mod ht_to_csv;
mod ht_to_json;
mod ht_to_msgpack;
mod ht_to_toml;
mod ht_to_xml;
mod ht_to_yaml;
mod utilities;

use ht_to_csv::*;
use ht_to_json::*;
use ht_to_msgpack::*;
use ht_to_toml::*;
use ht_to_xml::*;
use ht_to_yaml::*;
use utilities::*;

use std::error::Error;

const OUTPUT_JSON_PATH: &str = "output.json";

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    let link = get_user_input_link()?;
    let html = get_html_data(&link).await?;

    let file_type = file_type_selection()?;
    match file_type.as_str() {
        "1" => {
            let json = html_to_json(&html)?;
            save_data_to_file(&serde_json::to_string_pretty(&json)?, OUTPUT_JSON_PATH, "JSON")?;
        }
        "2" => {
            html_to_csv(&html)?;
        }
        "3" => {
            html_to_xml(&html)?;
        }
        "4" => {
            html_to_toml(&html)?;
        }
        "5" => {
            html_to_yaml(&html)?;
        }
        "6" => {
            html_to_msgpack(&html)?;
        }
        "q" => {
            println!("Quitting...");
            std::process::exit(0);
        }
        _ => {
            println!("Invalid file type");
        }
    }
    Ok(())
}
