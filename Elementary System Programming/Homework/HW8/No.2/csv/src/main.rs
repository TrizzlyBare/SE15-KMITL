use csv::{ReaderBuilder, Writer, Trim};
use std::fs::File;
use std::io::{Read, Write};

fn main() {
    read_point();
    read_point2(); 
}

struct Point {
    x: f64,
    y: f64,
}

struct PolarPoint {
    r: f64,
    t: f64,
}

fn to_polar(pt_list: Vec<Point>) -> Vec<PolarPoint> {
    let mut polar_list = Vec::new();
    for pt in pt_list {
        let r = (pt.x * pt.x + pt.y * pt.y).sqrt();
        let t = pt.y.atan2(pt.x);
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

fn load_point<R: Read>(rdr: R) -> Vec<Point> {
    let mut reader = ReaderBuilder::new()
        .delimiter(b',')
        .has_headers(false)
        .trim(Trim::All)
        .from_reader(rdr);

    let mut out_list = vec![];
    for record in reader.recorads() {
        if let Ok(rec) = record {
            let x: f64 = rec[0].parse().unwrap();
            let y: f64 = rec[1].parse().unwrap();
            out_list.push(Point { x, y });
        }
    }
    out_list
}

fn save_points<W: Write>(writer: W, pt_list: Vec<PolarPoint>) {
    let mut wtr = Writer::from_writer(writer);
    for pt in pt_list {
        wtr.write_record(&[pt.r.to_string(), pt.t.to_string()])
            .unwrap();
    }
    wtr.flush().unwrap();
}

fn save_points2<W: Write>(writer: W, pt_list: Vec<Point>) {
    let mut wtr = Writer::from_writer(writer);
    for pt in pt_list {
        wtr.write_record(&[pt.x.to_string(), pt.y.to_string()])
            .unwrap();
    }
    wtr.flush().unwrap();
}

fn read_point() {
    let input_file = "src/input.csv";
    let output_file = "output.csv";

    let point = load_point(File::open(input_file).unwrap());
    let tagged_points = to_polar(point);
    save_points(File::create(output_file).unwrap(), tagged_points);
}

fn read_point2() {
    let input_file = "src/input2.csv";
    let output_file = "output2.csv";
    
    let point = load_point(File::open(input_file).unwrap());
    
    let tagged_points = to_polar(point);
    let cartesian_points = to_cartesian(tagged_points);
    save_points2(File::create(output_file).unwrap(), cartesian_points); 
}
