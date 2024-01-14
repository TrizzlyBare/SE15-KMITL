fn main() {
    let points = vec![
        Point { x: 1.0, y: 1.0 },
        Point { x: 2.0, y: 2.0 },
        Point { x: 0.0, y: 1.0 },
        Point { x: 1.0, y: 0.0 },
    ];

    let polar_points = to_polar(points.clone());
    let cartesian_points = to_cartesian(polar_points.clone());

    println!("Original Points: {:?}", points);
    println!("Polar Points: {:?}", polar_points);
    println!("Cartesian Points: {:?}", cartesian_points);
}

#[derive(Debug, Clone)]
struct Point {
    x: f64,
    y: f64,
}

#[derive(Debug, Clone)]
struct PolarPoint {
    r: f64,
    t: f64,
}

fn to_polar(pt_list: Vec<Point>) -> Vec<PolarPoint> {
    let mut polar_list = Vec::new();
    for pt in pt_list {
        let r = (pt.x * pt.x + pt.y * pt.y).sqrt();
        let t = (pt.y / pt.x).atan();
        polar_list.push(PolarPoint { r, t });
    }
    polar_list
}

fn to_cartesian(pt_list: Vec<PolarPoint>) -> Vec<Point> {
    let mut cartesian_list = Vec::new();
    for pt in pt_list {
        let x = pt.r * pt.t.cos();
        let y = pt.r * pt.t.sin();
        cartesian_list.push(Point { x, y });
    }
    cartesian_list
}
