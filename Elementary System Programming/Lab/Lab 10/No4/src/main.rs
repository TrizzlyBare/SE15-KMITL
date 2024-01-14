#![allow(dead_code)]
#![allow(non_snake_case)]

use rand::Rng;
use std::env;
use std::fs::File;
use std::io::prelude::*;

#[derive(Debug, Clone)]
struct Point {
    x: f64,
    y: f64,
}

#[derive(Debug, Clone)]
struct Circle {
    center: Point,
    radius: f64,
}

#[derive(Debug)]
enum PtList {
    InsideFirst(Point, f64),
    InsideSecond(Point, f64),
    InsideBoth(Point, f64),
    Outside(Point, f64),
}

#[derive(Debug, Clone)]
struct Bound {
    circle1: Circle,
    circle2: Circle,
}

struct Config {
    x_min: f64,
    x_max: f64,
    y_min: f64,
    y_max: f64,
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

fn calculate_distance(p: &Point, c: &Circle) -> f64 {
    let x = p.x - c.center.x;
    let y = p.y - c.center.y;
    (x * x + y * y).sqrt()
}

fn calculate_distance2(p: &Point, c1: &Circle, c2: &Circle) -> (f64, f64) {
    let d1 = calculate_distance(p, c1);
    let d2 = calculate_distance(p, c2);
    (d1, d2)
}

fn locate_n_points(points: &[Point], b: &Bound) -> Vec<PtList> {
    let mut pt_list = Vec::new();
    for p in points {
        let (d1, d2) = calculate_distance2(&p, &b.circle1, &b.circle2);
        if d1 <= b.circle1.radius && d2 <= b.circle2.radius {
            pt_list.push(PtList::InsideBoth(p.clone(), d1.min(d2)));
        } 
        else if d1 <= b.circle1.radius {
            pt_list.push(PtList::InsideFirst(p.clone(), d1));
        }
        else if d2 <= b.circle2.radius {
            pt_list.push(PtList::InsideSecond(p.clone(), d2));
        }
        else {
            pt_list.push(PtList::Outside(p.clone(), d1.min(d2)));
        }
    }
    pt_list
}

fn generate_point_list<R: Rng>(
    rng: &mut R,
    cfg: &Config,
    n: i32,
    b: Bound, 
) -> Vec<(Point, PtList)> {
    let points = gen_point_list(rng, cfg, n);
    let pt_list = locate_n_points(&points, &b);
    points.into_iter().zip(pt_list.into_iter()).collect()
}

fn generate_svg(cfg: &Config, c1: Circle, c2: Circle, pt_list: &[(Point, PtList)]) {
    let mut result = String::new();
    result.push_str("<svg width=\"500\" height=\"500\" xmlns=\"http://www.w3.org/2000/svg\">");
    result.push_str("<rect width=\"100%\" height=\"100%\" fill=\"#EEEEEE\" />");
    
    // Calculate SVG coordinates for the first circle center
    let cx1 = (c1.center.x - cfg.x_min) / (cfg.x_max - cfg.x_min) * 500.0;
    let cy1 = (c1.center.y - cfg.y_min) / (cfg.y_max - cfg.y_min) * 500.0;
    
    // Calculate SVG coordinates for the second circle center
    let cx2 = (c2.center.x - cfg.x_min) / (cfg.x_max - cfg.x_min) * 500.0;
    let cy2 = (c2.center.y - cfg.y_min) / (cfg.y_max - cfg.y_min) * 500.0;
    
    result.push_str(&format!(
        "<circle cx=\"{}\" cy=\"{}\" r=\"{}\" stroke=\"black\" stroke-width=\"1\" fill=\"none\" />",
        cx1, cy1, c1.radius * 500.0 / (cfg.x_max - cfg.x_min)
    ));
    
    result.push_str(&format!(
        "<circle cx=\"{}\" cy=\"{}\" r=\"{}\" stroke=\"black\" stroke-width=\"1\" fill=\"none\" />",
        cx2, cy2, c2.radius * 500.0 / (cfg.x_max - cfg.x_min)
    ));
    
    for (point, pt) in pt_list {
        let color = match pt {
            PtList::InsideFirst(_, _) => "blue",
            PtList::InsideSecond(_, _) => "green",
            PtList::InsideBoth(_, _) => "purple",
            PtList::Outside(_, _) => "red",
        };
        // Calculate SVG coordinates for the points
        let px = (point.x - cfg.x_min) / (cfg.x_max - cfg.x_min) * 500.0;
        let py = (point.y - cfg.y_min) / (cfg.y_max - cfg.y_min) * 500.0;
        result.push_str(&format!(
            "<circle cx=\"{}\" cy=\"{}\" r=\"2\" stroke=\"{}\" stroke-width=\"1\" fill=\"{}\" />",
            px, py, color, color
        ));
    }
    
    result.push_str("</svg>");
    
    let mut file = File::create("output.svg").expect("Unable to create file");
    file.write_all(result.as_bytes()).expect("Unable to write to file");
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 11 {
        eprintln!("Usage: {} <x_min> <x_max> <y_min> <y_max> <px_circle1> <py_circle1> <r_circle1> <px_circle2> <py_circle2> <r_circle2>", args[0]);
        std::process::exit(1);
    }

    let x_min = args[1].parse::<f64>().expect("Invalid x_min");
    let x_max = args[2].parse::<f64>().expect("Invalid x_max");
    let y_min = args[3].parse::<f64>().expect("Invalid y_min");
    let y_max = args[4].parse::<f64>().expect("Invalid y_max");
    let px_circle1 = args[5].parse::<f64>().expect("Invalid px_circle1");
    let py_circle1 = args[6].parse::<f64>().expect("Invalid py_circle1");
    let r_circle1 = args[7].parse::<f64>().expect("Invalid r_circle1");
    let px_circle2 = args[8].parse::<f64>().expect("Invalid px_circle2");
    let py_circle2 = args[9].parse::<f64>().expect("Invalid py_circle2");
    let r_circle2 = args[10].parse::<f64>().expect("Invalid r_circle2");

    let mut rng = rand::thread_rng();
    let cfg = Config {
        x_min,
        x_max,
        y_min,
        y_max,
    };
    let c1 = Circle {
        center: Point { x: px_circle1, y: py_circle1 },
        radius: r_circle1,
    };
    let c2 = Circle {
        center: Point { x: px_circle2, y: py_circle2 },
        radius: r_circle2,
    };
    let b = Bound {
        circle1: c1.clone(),
        circle2: c2.clone(),
    };
    let point_list = generate_point_list(&mut rng, &cfg, 1000, b);
    generate_svg(&cfg, c1, c2, &point_list);
}
