use csv::Writer;
use scraper::{Html, Selector};
use std::error::Error;

pub fn html_to_csv(html: &str) -> Result<(), Box<dyn Error>> {
    let document = Html::parse_document(&html);
    let selector = Selector::parse("table").unwrap();
    let table = document.select(&selector).next().unwrap();

    let mut wtr = Writer::from_path("output.csv")?;

    let headers = table
        .select(&Selector::parse("tr").unwrap())
        .next()
        .unwrap()
        .select(&Selector::parse("th, td").unwrap())
        .map(|cell| cell.text().collect::<String>())
        .collect::<Vec<String>>();

    wtr.write_record(&headers)?;

    for row in table.select(&Selector::parse("tr").unwrap()).skip(1) {
        let mut record = Vec::new();
        for cell in row.select(&Selector::parse("th, td").unwrap()) {
            record.push(cell.text().collect::<String>());
        }
        wtr.write_record(&record)?;
    }
    wtr.flush()?;
    Ok(())
}