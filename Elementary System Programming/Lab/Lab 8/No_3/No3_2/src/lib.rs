use csv::{ReaderBuilder, Trim};
use std::io::Read;

#[derive(Debug, PartialEq)]
struct Point {
    x: f64,
    y: f64,
    color: String,
}

fn load_point<R: Read>(rdr: R) -> Vec<Point> {
    let mut reader
        = ReaderBuilder::new() 
        .delimiter(b',')
        .has_headers(false)
        .trim(Trim::All) 
        .from_reader(rdr);

        let mut out_list = vec![];
        for record in reader.records() {
            if let Ok(rec) = record {
            let x: f64 = rec[0].parse().unwrap(); 
            let y: f64 = rec[1].parse().unwrap(); 
            out_list.push( Point { x: x, y: y, color: "#000000".to_string() });
            } 
        }
    out_list 
}   

#[test]
fn test_load_point() {

    let csv_data = "1.0,2.0\n3.0,4.0\n";
    
    let input_file_path = csv_data.as_bytes();

    let pairs = load_point(input_file_path);

    let expected_output = vec![
        Point { x: 1.0, y: 2.0, color: "#000000".to_string() },
        Point { x: 3.0, y: 4.0, color: "#000000".to_string() },
    ];

    assert_eq!(pairs, expected_output);
}