use No3_1::tag_points;
use No3_1::Point;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
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

    for point in result {
        println!("x: {}, y: {}, color: {}", point.x, point.y, point.color);
    }

    Ok(())
}