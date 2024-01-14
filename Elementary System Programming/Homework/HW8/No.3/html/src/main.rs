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
    for record in reader.records() {
        if let Ok(rec) = record {
            let x: f64 = rec[0].parse().unwrap();
            let y: f64 = rec[1].parse().unwrap();
            out_list.push(Point { x, y });
        }
    }
    out_list
}

fn save_points_as_html<W: Write>(writer: W, pt_list: Vec<PolarPoint>) {
    let mut wtr = writer;

    wtr.write_all("<table border = '1'>\n<tr><th>r</th><th>t</th></tr>\n".as_bytes()).unwrap();
    for pt in pt_list {
        let row = format!("<tr><td>{}</td><td>{}</td></tr>\n", pt.r, pt.t);
        wtr.write_all(row.as_bytes()).unwrap();
    }
    wtr.write_all("</table>\n".as_bytes()).unwrap();
}

fn save_points2_as_html<W: Write>(writer: W, pt_list: Vec<Point>) {
    let mut wtr = writer;
    
    wtr.write_all("<table border = '1'>\n<tr><th>x</th><th>y</th></tr>\n".as_bytes()).unwrap();
    for pt in pt_list {
        let row = format!("<tr><td>{}</td><td>{}</td></tr>\n", pt.x, pt.y);
        wtr.write_all(row.as_bytes()).unwrap();
    }
    wtr.write_all("</table>\n".as_bytes()).unwrap();
}

fn read_point() {
    let input_file = "src/input.csv";
    let output_file = "output.html";

    let point = load_point(File::open(input_file).unwrap());
    let tagged_points = to_polar(point);

    let file = File::create(output_file).unwrap();
    save_points_as_html(file, tagged_points);
}

fn read_point2() {
    let input_file = "src/input2.csv";
    let output_file = "output2.html";

    let point = load_point(File::open(input_file).unwrap());
    let tagged_points = to_polar(point);
    let cartesian_points = to_cartesian(tagged_points);

    let file = File::create(output_file).unwrap();
    save_points2_as_html(file, cartesian_points);
}
