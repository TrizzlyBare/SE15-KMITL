use std::f64::consts::PI;

// #[derive(Debug, Clone, Copy)]
// enum Shape {
//     Circle(i32,i32,i32),
//     Rectangle(i32,i32,i32,i32),
// }

// impl Shape {
//     fn area(&self) -> f64 {
//         match *self {
//             Shape::Circle(_,_, radius) => PI *radius as f64 *radius as f64,
//             Shape::Rectangle(_,_,width,height) => width as f64 * height as f64,

//         }
//     }

//     fn rep_string(&self) -> String {
//         match *self {
//             Shape::Circle(x,y,radius) => {
//                 format!("<Circle: {}, {}, {}>",x,y, radius)
//             }
//             Shape::Rectangle(x,y,width, height) => {
//                 format!("<Rectangle: {}, {}, {}, {}>", x,y, width, height)
//             }
//         }
//     }
// }

// const INPUT_SHAPES: &[Shape] = &[
// Shape::Circle(0, 0, 1), Shape::Circle(50, 50, 15),
// Shape::Rectangle(40, 40, 20, 20), Shape::Rectangle(10, 40, 15, 10)
// ];

// const EXPECTED: &[&str] = &[
// "<Circle: 0, 0, 1>, area: 3.14",
// "<Circle: 50, 50, 15>, area: 706.86",
// "<Rectangle: 40, 40, 20, 20>, area: 400.00",
// "<Rectangle: 10, 40, 15, 10>, area: 150.00"
// ];


trait Shape {
    fn rep_string(&self) -> String;
    fn area(&self) -> f64;
    fn clone_box(&self) -> Box<dyn Shape>; 
}

impl Clone for Box<dyn Shape> {
    fn clone(&self) -> Self {
        self.clone_box()
    }
}

struct Circle {
    x: i32,
    y: i32,
    radius: i32,
}

impl Circle {
    fn new(x: i32, y:i32, radius: i32) -> Box<dyn Shape> {
        Box::new(Circle {x,y, radius})
    }
}

impl Shape for Circle {
    fn rep_string(&self) -> String {
        format!("<Circle: {}, {}, {}>", self.x, self.y, self.radius)
    }

    fn area(&self) -> f64 {
        PI *self.radius as f64 * self.radius as f64
    }
    fn clone_box(&self) -> Box<dyn Shape> {
        Circle::new(self.x, self.y, self.radius)
    }
}

struct Rectangle {
    x: i32,
    y: i32,
    width: i32,
    height: i32,
}

impl Rectangle {
    fn new(x: i32, y: i32, width: i32, height: i32) -> Box<dyn Shape> {
        Box::new(Rectangle {x,y, width, height})
    }
}

impl Shape for Rectangle {
    fn rep_string(&self) -> String {
        format!("<Rectangle: {}, {}, {}, {}>", self.x,self.y, self.width, self.height)
    }

    fn area(&self) -> f64 {
        self.width as f64 * self.height as f64
    }

    fn clone_box(&self) -> Box<dyn Shape> {
        Rectangle::new(self.x, self.y, self.width, self.height)
    }
}

fn input_shape_list() -> Vec<Box<dyn Shape>> {
    vec![
        Circle::new(0, 0, 1),
        Circle::new(50, 50, 15),
        Rectangle::new(40, 40, 20, 20),
        Rectangle::new(10, 40, 15, 10),
    ]
}

const EXPECTED_001: &[&str] = &[
    "<Circle: 0, 0, 1>",
    "<Circle: 50, 50, 15>",
    "<Rectangle: 40, 40, 20, 20>",
    "<Rectangle: 10, 40, 15, 10>",
];

const EXPECTED_002: &[&str] = &[
    "<Circle: 0, 0, 1>, area: 3.14",
    "<Circle: 50, 50, 15>, area: 706.86",
    "<Rectangle: 40, 40, 20, 20>, area: 400.00",
    "<Rectangle: 10, 40, 15, 10>, area: 150.00",
];

#[test]
fn test_shapes_001() {
    let shape_list = input_shape_list();
    let omap = shape_list.iter().map(|s| s.rep_string());
    let output: Vec<_> = omap.collect();
    assert_eq!(output, EXPECTED_001);
}

#[test]
fn test_shapes_002() {
    let shape_list = input_shape_list();
    let omap = shape_list.iter().map(|s| format!("{}, area: {:.2}", s.rep_string(), s.area()));
    let output: Vec<_> = omap.collect();
    assert_eq!(output, EXPECTED_002);
}

#[test]
fn test_shapes_003() {
    let input_list = input_shape_list();
    let shape_list = input_list.clone();
    let omap = shape_list.iter().map(
    |s| format!("{}, area: {:.2}", s.rep_string(), s.area()) );
    let output: Vec<_> = omap.collect();
    assert_eq!(output, EXPECTED_002);
}
fn main() {
    println!("Hello, world!");
}
