#[derive(Debug, Clone, Copy)]
enum Shape {
    Circle(i32, i32, i32),
    Rectangle(i32, i32, i32, i32),
    Triangle(i32, i32, i32, i32, i32, i32),
}

impl Shape {
    fn area(&self) -> f64 {
        match *self {
            Shape::Circle(_, _, radius) => std::f64::consts::PI * radius as f64 * radius as f64,
            Shape::Rectangle(_, _, width, height) => width as f64 * height as f64,
            Shape::Triangle(x1, y1, x2, y2, x3, y3) => {
                0.5 * ((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) as f64
            }
        }
    }

    fn rep_string(&self) -> String {
        match *self {
            Shape::Circle(x, y, radius) => {
                format!("<Circle: {}, {}, {}>", x, y, radius)
            }
            Shape::Rectangle(x, y, width, height) => {
                format!("<Rectangle: {}, {}, {}, {}>", x, y, width, height)
            }
            Shape::Triangle(x1, y1, x2, y2, x3, y3) => {
                format!("<Triangle: {}, {}, {}, {}, {}, {}>", x1, y1, x2, y2, x3, y3)
            }
        }
    }
}

const INPUT_SHAPES: &[Shape] = &[
    Shape::Circle(0, 0, 1),
    Shape::Circle(50, 50, 15),
    Shape::Rectangle(40, 40, 20, 20),
    Shape::Rectangle(10, 40, 15, 10),
];

const EXPECTED: &[&str] = &[
    "<Circle: 0, 0, 1>, area: 3.14",
    "<Circle: 50, 50, 15>, area: 706.86",
    "<Rectangle: 40, 40, 20, 20>, area: 400.00",
    "<Rectangle: 10, 40, 15, 10>, area: 150.00",
];

#[test]
fn test_shapes() {
    let input_list = INPUT_SHAPES;
    let shape_list = input_list.clone();
    let omap = shape_list
        .iter()
        .map(|s| format!("{}, area: {:.2}", s.rep_string(), s.area()));
    let output: Vec<_> = omap.collect();
    assert_eq!(output, EXPECTED);
}

fn main() {
    println!("Hello, world!");
}

