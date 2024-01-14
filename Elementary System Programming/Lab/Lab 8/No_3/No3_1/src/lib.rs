use csv::{ReaderBuilder, Writer, Trim};
use std::io::Read;

pub struct Point {
    pub x: f64,
    pub y: f64,
    pub color: String,
}

const GREEN_TONE: &str = "#80FF8080";
const RED_TONE: &str = "#FF808080";

pub fn tag_points(pt_list: Vec<Point>) -> Vec<Point> {
    let mut result: Vec<Point> = Vec::new();
    for pt in pt_list {
        let dist = (pt.x.powi(2) + pt.y.powi(2)).sqrt();
        let color = if dist > 1.0 {
            RED_TONE.to_string()
        } else {
            GREEN_TONE.to_string()
        };
        result.push(Point {
            x: pt.x,
            y: pt.y,
            color,
        });
    }
    result
}

#[test]
fn test_tag_points() {
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
    let result = tag_points(pt_list);
    assert_eq!(result[0].color, GREEN_TONE);
    assert_eq!(result[1].color, GREEN_TONE);
    assert_eq!(result[2].color, RED_TONE);
}

