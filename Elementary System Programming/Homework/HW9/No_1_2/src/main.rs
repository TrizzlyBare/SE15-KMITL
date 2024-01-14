#![allow(dead_code)]
#![allow(non_snake_case)]

use rand::Rng;
use csv::Writer;
use std::error::Error;

struct Circle {
    x: f64,
    y: f64,
    radius: f64,
}

struct Layer {
    name: String,
    color: String,
    objects: Vec<Circle>,
}

fn gen_layer(name: String, color: String) -> Layer {
    let mut rng = rand::thread_rng();
    let mut objects = Vec::new();
    for _ in 0..rng.gen_range(20..=50) {
        objects.push(Circle {
            x: rng.gen_range(-100.0..=100.0),
            y: rng.gen_range(-100.0..=100.0),
            radius: rng.gen_range(-10.0..=20.0),
        });
    }
    Layer {
        name,
        color,
        objects,
    }
}

fn gen_obj_layer_list<R: Rng>(rng: &mut R, n: i32) -> Vec<Layer> {
    let mut result = Vec::new();

    for i in 1..=n {
        let r: u8 = rng.gen();
        let g: u8 = rng.gen();
        let b: u8 = rng.gen();
        let layer = gen_layer(
            format!("Layer {}", i),
            format!("#{:02X}{:02X}{:02X}AA", r, g, b),
        );
        result.push(layer);
    }
    result
}

#[test]
fn test_gen_obj_layer_list() {
    let mut rng = rand::thread_rng();
    let layers = gen_obj_layer_list(&mut rng, 3);
    for layer in &layers {
        let num_circles = layer.objects.len();
        assert!(num_circles >= 20 && num_circles <= 50);
    }
}

fn cal_average_area(layers: &Vec<Layer>) -> Vec<(String, f64)> {
    let mut result = Vec::new();

    for layer in layers {
        let mut sum = 0.0;
        let mut count = 0;

        for circle in &layer.objects {
            sum += circle.radius * circle.radius * std::f64::consts::PI;
            count += 1;
        }

        if count > 0 {
            let average_area = sum / count as f64;
            result.push((layer.name.clone(), average_area));
        }
    }

    result
}

#[test]
fn test_cal_average_area() {
    let mut rng = rand::thread_rng();
    let layers = gen_obj_layer_list(&mut rng, 3);
    let average_areas = cal_average_area(&layers);
    assert_eq!(average_areas.len(), 3);
}

fn save_layers_as_csv(layers: &[Layer]) -> Result<(), Box<dyn Error>> {
    let mut writer = Writer::from_path("layers.csv")?;
    writer.write_record(&["Layer Name", "Color", "Number of Circles"])?;

    for layer in layers {
        let num_circles = layer.objects.len();
        writer.write_record(&[&layer.name, &layer.color, &num_circles.to_string()])?;
    }

    writer.flush()?;
    Ok(())
}

fn save_average_areas_as_csv(average_areas: &[(String, f64)], filename: &str) -> Result<(), Box<dyn Error>> {
    let mut writer = Writer::from_path(filename)?;
    writer.write_record(&["Layer Name", "Average Area"])?;

    for (name, avg_area) in average_areas {
        writer.write_record(&[name, &avg_area.to_string()])?;
    }

    writer.flush()?;
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    let mut rng = rand::thread_rng();
    let num_layers = 3;
    let layers = gen_obj_layer_list(&mut rng, num_layers);

    save_layers_as_csv(&layers)?;

    let average_areas = cal_average_area(&layers);
    save_average_areas_as_csv(&average_areas, "areas.csv")?;

    Ok(())
}
