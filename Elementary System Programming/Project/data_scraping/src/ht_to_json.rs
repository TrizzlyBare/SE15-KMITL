use scraper::{Html, Selector};
use serde_json::Value;
use std::collections::HashMap;
use std::error::Error;

pub fn html_to_json(html: &str) -> Result<Value, Box<dyn Error>> {
    let document = Html::parse_document(&html);
    let selector = Selector::parse("table").unwrap();
    let is_table = document.select(&selector).next().is_some();

    if is_table {
        let mut table_data: Vec<HashMap<String, String>> = vec![];
        let mut column_map: HashMap<usize, Vec<String>> = HashMap::new();

        let row_selector = Selector::parse("table tr").unwrap();

        for row in document.select(&row_selector) {
            let mut col_idx = 0;
            let mut row_data = HashMap::new();

            let cell_selector = Selector::parse("td, th").unwrap();
            row.select(&cell_selector).for_each(|cell| {
                let text = cell.text().collect::<String>();
                row_data.insert(format!("col_{}", col_idx), text.clone());

                let column_entries = column_map.entry(col_idx).or_insert(Vec::new());
                column_entries.push(text);
                col_idx += 1;
            });

            table_data.push(row_data);
        }

        for (_, column) in column_map.iter_mut() {
            column.sort();
        }

        let mut sorted_table_data: Vec<HashMap<String, String>> = vec![];
        let num_columns = column_map.len();

        if num_columns > 0 {
            for row in 0..table_data.len() {
                let mut sorted_row: HashMap<String, String> = HashMap::new();
                for col_idx in 0..num_columns {
                    if let Some(column) = column_map.get(&col_idx) {
                        if row < column.len() {
                            sorted_row.insert(format!("col_{}", col_idx), column[row].clone());
                        } else {
                            sorted_row.insert(format!("col_{}", col_idx), "".to_string());
                        }
                    }
                }
                sorted_table_data.push(sorted_row);
            }
        }

        let result = serde_json::json!({
            "data": sorted_table_data,
            "type": "table"
        });

        Ok(result)
    } else {
        let error_result = serde_json::json!({ "error": "Input is not a table" });
        Ok(error_result)
    }
}