#![allow(dead_code)]
#![allow(non_snake_case)]

use std::env;
use std::fs::File;
use std::io::Write;
use rand::Rng;

#[derive(Debug, Clone)]
struct Point {
    x: f64,
    y: f64,
}

#[derive(Debug)]
struct Config {
    x_min: f64,
    x_max: f64,
    y_min: f64,
    y_max: f64,
}

#[derive(Debug, Clone)]
struct Circle {
    center: Point,
    radius: f64,
}

#[derive(Debug)]
enum PtList {
    Inside(Point, f64),
    Outside(Point, f64),
}

fn gen_point_list<R: Rng>(rng: &mut R, cfg: &Config, n: i32) -> Vec<Point> {
    let mut points = Vec::new();
    for _ in 0..n {
        let x = rng.gen_range(cfg.x_min..=cfg.x_max);
        let y = rng.gen_range(cfg.y_min..=cfg.y_max);
        points.push(Point { x, y });
    }
    points
}

fn calculate_distance(p1: &Point, p2: &Point) -> f64 {
    let x = p1.x - p2.x;
    let y = p1.y - p2.y;
    (x * x + y * y).sqrt()
}

fn locate_n_points(points: &[Point], c: &Circle) -> Vec<PtList> {
    let mut pt_list = Vec::new();
    for p in points {
        let d = calculate_distance(&p, &c.center);
        if d <= c.radius {
            pt_list.push(PtList::Inside(p.clone(), d));
        } else {
            pt_list.push(PtList::Outside(p.clone(), d));
        }
    }
    pt_list
}

fn generate_point_list<R: Rng>(
    rng: &mut R,
    cfg: &Config,
    n: i32,
    c: Circle,
) -> Vec<(Point, PtList)> {
    let points = gen_point_list(rng, cfg, n);
    let pt_list = locate_n_points(&points, &c);
    points.into_iter().zip(pt_list.into_iter()).collect()
}

fn main() {
    let mut rng = rand::thread_rng();
    let cfg = Config {
        x_min: -1.5,
        x_max: 1.5,
        y_min: -1.5,
        y_max: 1.5,
    };
    let c = Circle {
        center: Point { x: -0.1, y: 0.1 },
        radius: 0.8,
    };

    let pt_list = generate_point_list(&mut rng, &cfg, 50, c);

    for (point, pt_type) in &pt_list {
        let formatted_x = format!("{:.2}", point.x);
        let formatted_y = format!("{:.2}", point.y);

        let pt_str = match pt_type {
            PtList::Inside(_, dist) => format!(
                "Inside((Point {{ x: {}, y: {} }}, {:.2}))",
                formatted_x, formatted_y, dist
            ),
            PtList::Outside(_, dist) => format!(
                "Outside((Point {{ x: {}, y: {} }}, {:.2}))",
                formatted_x, formatted_y, dist
            ),
        };
        println!("{}", pt_str);
    }
}

#[test]
fn test_locate_n_point() {
    let circle = Circle {
        center: Point { x: 0.0, y: 0.0 },
        radius: 1.0,
    };

    let inside_point = Point { x: 0.5, y: 0.5 };
    let outside_point = Point { x: 1.5, y: 1.5 };

    let positions = locate_n_points(&[inside_point, outside_point], &circle);

    assert_eq!(positions.len(), 2);

    match &positions[0] {
        PtList::Inside(_, distance) => {
            assert!(*distance <= circle.radius);
        }
        _ => panic!("Expected Inside position"),
    }

    match &positions[1] {
        PtList::Outside(_, distance) => {
            assert!(*distance > circle.radius);
        }
        _ => panic!("Expected Outside position"),
    }
}

// fn generate_svg(cfg: &Config, c: Circle, pt_list: &[(Point, PtList)]) {
//     let mut result = String::new();
//     result.push_str("<svg width=\"500\" height=\"500\" xmlns=\"http://www.w3.org/2000/svg\">");
//     result.push_str("<rect width=\"100%\" height=\"100%\" fill=\"#EEEEEE\" />");
    
//     // Calculate SVG coordinates for the circle center
//     let cx = (c.center.x - cfg.x_min) / (cfg.x_max - cfg.x_min) * 500.0;
//     let cy = (c.center.y - cfg.y_min) / (cfg.y_max - cfg.y_min) * 500.0;
    
//     result.push_str(&format!(
//         "<circle cx=\"{}\" cy=\"{}\" r=\"{}\" stroke=\"black\" stroke-width=\"1\" fill=\"none\" />",
//         cx, cy, c.radius * 500.0
//     ));
    
//     for (point, pt) in pt_list {
//         let color = match pt {
//             PtList::Inside(_, _) => "blue",
//             PtList::Outside(_, _) => "red",
//         };
//         // Calculate SVG coordinates for the points
//         let px = (point.x - cfg.x_min) / (cfg.x_max - cfg.x_min) * 500.0;
//         let py = (point.y - cfg.y_min) / (cfg.y_max - cfg.y_min) * 500.0;
//         result.push_str(&format!(
//             "<circle cx=\"{}\" cy=\"{}\" r=\"2\" stroke=\"{}\" stroke-width=\"1\" fill=\"{}\" />",
//             px, py, color, color
//         ));
//     }
    
//     result.push_str("</svg>");
    
//     let mut file = File::create("output.svg").expect("Unable to create file");
//     file.write_all(result.as_bytes()).expect("Unable to write to file");
// }

// fn main() {
//     let args: Vec<String> = env::args().collect();
//     if args.len() != 8 {
//         eprintln!("Usage: {} <x_min> <x_max> <y_min> <y_max> <px_circle> <py_circle>", args[0]);
//         std::process::exit(1);
//     }

//     let x_min = args[1].parse::<f64>().expect("Invalid x_min");
//     let x_max = args[2].parse::<f64>().expect("Invalid x_max");
//     let y_min = args[3].parse::<f64>().expect("Invalid y_min");
//     let y_max = args[4].parse::<f64>().expect("Invalid y_max");
//     let px_circle = args[5].parse::<f64>().expect("Invalid px_circle");
//     let py_circle = args[6].parse::<f64>().expect("Invalid py_circle");
//     let r_circle = args[7].parse::<f64>().expect("Invalid radius");

//     let mut rng = rand::thread_rng();
//     let cfg = Config {
//         x_min,
//         x_max,
//         y_min,
//         y_max,
//     };
//     let c = Circle {
//         center: Point {
//             x: px_circle,
//             y: py_circle,
//         },
//         radius: r_circle, 
//     };

//     let pt_list = generate_point_list(&mut rng, &cfg, 1000, c.clone());
//     generate_svg(&cfg, c, &pt_list);
// }

