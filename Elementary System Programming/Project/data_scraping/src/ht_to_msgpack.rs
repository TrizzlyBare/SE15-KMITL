use select::document::Document;
use select::predicate::Name;
use serde::Serialize;
use std::error::Error;

#[derive(Serialize)]
struct TableRow {
    cells: Vec<TableCell>,
}

#[derive(Serialize)]
struct TableCell {
    name: String,
    content: String,
}

pub fn html_to_msgpack(html: &str) -> Result<(), Box<dyn Error>> {
    let document = Document::from(html);
    let table = document
        .find(Name("table"))
        .next()
        .ok_or("No table found in the HTML")?;

    let mut table_data = vec![];

    for row in table.find(Name("tr")) {
        let mut cells = vec![];
        for cell in row.find(Name("th, td")) {
            let name = cell.name();
            let content = cell.text();

            let cell_data = TableCell {
                name: name.expect("REASON").to_string(),
                content,
            };
            cells.push(cell_data);
        }

        let row_data = TableRow { cells };
        table_data.push(row_data);
    }

    let packed = rmp_serde::to_vec(&table_data)?;

    std::fs::write("output.msgpack", packed)?;

    Ok(())
}