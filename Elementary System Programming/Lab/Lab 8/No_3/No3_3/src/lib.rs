use csv::{ReaderBuilder,Writer, Trim};
use std::io::Read;


struct Point {
    x: f64,
    y: f64,
    color: String,
}

fn save_points<W: std::io::Write>(writer: W, pt_list: Vec<Point>) {
    let mut wtr = Writer::from_writer(writer);
    for pt in pt_list {
        wtr.write_record(&[pt.x.to_string(), pt.y.to_string(), pt.color])
            .unwrap();
    }
    wtr.flush().unwrap();
}

#[test]
fn test_save_points() {
    let pt_list = vec![
        Point {
            x: 0.0,
            y: 0.0,
            color: String::new(),
        },
        Point {
            x: 0.5,
            y: 0.5,
            color: String::new(),
        },
        Point {
            x: 1.0,
            y: 1.0,
            color: String::new(),
        },
    ];
    let mut result = Vec::new();
    save_points(&mut result, pt_list);
    let result = String::from_utf8(result).unwrap();
    assert_eq!(result, "0,0,\n0.5,0.5,\n1,1,\n");
}