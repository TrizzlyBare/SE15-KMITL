use csv::Writer;
use rand::Rng;
use std::fs::File;
use std::convert::TryInto;
use std::error::Error;
use std::io::Write;

struct Point {
    x: f64,
    y: f64,
}

struct Layer {
    name: String,
    color: String,
    points: Vec<Point>,
}

fn gen_layer(name: String, color: String) -> Layer {
    let mut rng = rand::thread_rng();
    let mut points = Vec::new();
    for _ in 0..rng.gen_range(20..=50) {
        points.push(Point {
            x: rng.gen_range(-100.0..=100.0),
            y: rng.gen_range(-100.0..=100.0),
        });
    }
    Layer {
        name,
        color,
        points,
    }
}

fn get_circle(layer: &Layer) -> String {
    let mut result = String::new();
    let r = 10;
    result.push_str("<svg width=\"500\" height=\"500\" xmlns=\"http://www.w3.org/2000/svg\">
        <rect width=\"100%\" height=\"100%\" fill=\"#EEEEEE\" />");
    for point in &layer.points {
        let result_x = (point.x + 100.0) / (100.0 + 100.0) * (500.0 - 0.0) + 0.0;
        let result_y = (point.y + 100.0) / (100.0 + 100.0) * (500.0 - 0.0) + 0.0;
        result.push_str("<circle ");
        result.push_str(&format!("cx=\"{}\" ", result_x));
        result.push_str(&format!("cy=\"{}\" ", result_y));
        result.push_str(&format!("r=\"{}\" ", r));
        result.push_str("fill=\"#00FF00\" ");
        result.push_str("/>\n");
    }
    result.push_str("</svg>");
    result
}

fn gen_layer_list<R: Rng>(rng: &mut R, n: i32) -> Vec<Layer> {
    let mut result = Vec::new();

    for i in 1..n + 1 {
        let r : u8  = rng.gen();
        let g : u8 = rng.gen();
        let b : u8  = rng.gen();
        let layer = gen_layer(
            format!("Layer {}", i),
            format!("#{:02X}{:02X}{:02X}", r, g, b),
        );
        result.push(layer);
    }
    result
}

fn to_svg_file(layer: &Layer, filename: &str) -> Result<(), Box<dyn Error>> {
    let svg = get_circle(layer);
    std::fs::write(filename, svg)?;
    Ok(())
}

// fn main() -> Result<(), Box<dyn Error>> {
//     let mut rng = rand::thread_rng();
//     let layer_list = gen_layer_list(&mut rng, 5);
//     for (i, layer) in layer_list.iter().enumerate() {
//         let filename = format!("layer{}.svg", i);
//         to_svg_file(layer, &filename)?;
//     }
//     Ok(())
// }

fn main() {
    get_circle_2()
}

fn get_circle_2() {
    let args: Vec<_> = std::env::args().collect();
    let n: i32 = args[1].parse().unwrap();

    let mut result = String::new();
    let mut rng = rand::thread_rng();
    let layer = gen_layer_list(&mut rng, n);
    let r = 10;

    result.push_str("<svg width=\"500\" height=\"500\" xmlns=\"http://www.w3.org/2000/svg\">
        <rect width=\"100%\" height=\"100%\" fill=\"#EEEEEE\" />");
   
    for point in layer{
        for point in point.points {
            let colors: i64 = rng.gen_range(0x00000000..=0xFFFFFFFF);
            let formatted_color = format!("#{:08X}", colors); 
            let result_x = (point.x + 100.0) / (100.0 + 100.0) * (500.0 - 0.0) + 0.0;
            let result_y = (point.y + 100.0) / (100.0 + 100.0) * (500.0 - 0.0) + 0.0;
            result.push_str("<circle ");
            result.push_str(&format!("cx=\"{}\" ", result_x));
            result.push_str(&format!("cy=\"{}\" ", result_y));
            result.push_str(&format!("r=\"{}\" ", r));
            result.push_str(&format!("fill=\"{}\" ", formatted_color));
            result.push_str("/>\n");
        }
    }
    result.push_str("</svg>");
    let mut file = File::create("output2.svg").expect("none");
    file.write(result.as_bytes()).expect("none");

    println!("Created a file output2.svg");
}