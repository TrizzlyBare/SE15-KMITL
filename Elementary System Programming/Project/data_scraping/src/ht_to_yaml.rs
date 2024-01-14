use scraper::{Html, Selector};
use std::error::Error;
use std::fs;

pub fn html_to_yaml(html: &str) -> Result<(), Box<dyn Error>> {
    let document = Html::parse_document(html);
    let selector = Selector::parse("table").unwrap();
    let table = document
        .select(&selector)
        .next()
        .ok_or("No table found in the HTML")?;

    let mut output = String::new();

    for row in table.select(&Selector::parse("tr").unwrap()) {
        output.push_str("-\n");

        let mut book_data = String::new();
        for cell in row.select(&Selector::parse("th, td").unwrap()) {
            let name = cell.value().name();
            let content = cell.text().collect::<String>();
            book_data.push_str(&format!("{}: \"{}\"\n", name, content));
        }

        output.push_str(&book_data);
    }

    fs::write("output.yaml", output)?;

    Ok(())
}