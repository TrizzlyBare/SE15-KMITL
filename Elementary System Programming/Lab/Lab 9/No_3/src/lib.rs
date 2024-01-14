use csv::Writer;
use rand::Rng;
use std::fs::File;
use std::io::Write;
use std::convert::TryInto;
use std::env;
use std::error::Error;

#[derive(Debug, Clone)]
struct Point {
    x: f64,
    y: f64,
}

#[derive(Debug)]
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

#[test]
fn test_gen_layer() {
    let layer = gen_layer("foo".to_string(), "red".to_string());
    assert_eq!(layer.name, "foo");
    assert_eq!(layer.color, "red");
    assert!(layer.points.len() >= 20);
    assert!(layer.points.len() <= 50);
    for point in &layer.points {
        assert!(point.x >= -100.0);
        assert!(point.x <= 100.0);
        assert!(point.y >= -100.0);
        assert!(point.y <= 100.0);
    }
}

fn gen_layer_list<R: Rng>(rng: &mut R, n: i32) -> Vec<Layer> {
    let mut result = Vec::new();
    let mut point = Vec::new();
    
    
    for _ in 0..n {
        let x = rng.gen_range(-100. ..= 100.);
        let y = rng.gen_range(-100. ..= 100.);

        point.push(Point {x, y})
    }

    for i in 0..n {
        let co = rng.gen_range(00000000 ..= 99999999);
        let color = format!("#{}", co);
        println!("{}", color);
        let name = format!("Layer {}", i+1);
        result.push(Layer { name: name.clone(), color: color.clone(), points: point.clone() })
    }
    
    result
}

// #[test]
// fn test_gen_layer_list() {
//     let mut rng = rand::thread_rng();
//     let n = 5;
//     let layers = gen_layer_list(&mut rng, n);

//     assert_eq!(layers.len(), n.try_into().unwrap());

//     for (i, layer) in layers.iter().enumerate() {
//         assert_eq!(layer.points.len(), n.try_into().unwrap());

//         for point in &layer.points {
//             assert!(point.x >= -100.0 && point.x <= 100.0);
//             assert!(point.y >= -100.0 && point.y <= 100.0);
//         }

//         assert_eq!(layer.name, format!("Layer {}", i+1));
        
//         assert_eq!(layer.color.chars().count(), 7);
//     }
// }

fn write_layer<W: Write>(writer: W, layers: Vec<Layer>) {
    let mut wtr = csv::Writer::from_writer(writer);

    for layer in layers {
        let mut records = Vec::new();

        let points_str = layer
            .points
            .iter()
            .map(|point| format!("{},{}", point.x, point.y))
            .collect::<Vec<String>>()
            .join(";");

        records.push(layer.name);
        records.push(layer.color);
        records.push(points_str);

        wtr.write_record(&records).unwrap();
    }

    wtr.flush().unwrap();
}

fn to_csv() {
    let arg: Vec<_> = std::env::args().collect();
    let num: i32 = arg[1].parse().unwrap();
    let output: String = arg[2].parse().unwrap();
    
    let mut rng = rand::thread_rng();

    let layers = gen_layer_list(&mut rng, num);

    let result = write_layer(File::create(output).unwrap(), layers);
    
    result
}

#[test]
fn test_to_csv() {
    let args = vec!["5".to_string(), "output.csv".to_string()];
    let num: i32 = args[0].parse().unwrap();
    let output_name: String = args[1].parse().unwrap();
    
    let mut rng = rand::thread_rng();

    let layers = gen_layer_list(&mut rng, num);

    let result = write_layer(File::create(output_name).unwrap(), layers);
    
    result
}