#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(non_snake_case)]

use rand::Rng;
use csv::Writer;
use std::fs::File;
use std::error::Error;
use std::io::Write;

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

fn cal_average_area(layers: &Vec<Layer>) -> Vec<(String, f64, f64, f64)> {
    let mut result = Vec::new();

    for layer in layers {
        let mut sum = 0.0;
        let mut count = 0;
        let mut min_area = f64::MAX; 
        let mut max_area = f64::MIN; 

        for circle in &layer.objects {
            let area = circle.radius * circle.radius * std::f64::consts::PI;
            sum += area;
            count += 1;

            if area < min_area {
                min_area = area;
            }

            if area > max_area {
                max_area = area;
            }
        }

        if count > 0 {
            let average_area = sum / count as f64;
            result.push((layer.name.clone(), average_area, min_area, max_area));
        }
    }

    result
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

fn save_average_areas_as_html(average_areas: &[(String, f64, f64, f64)], filename: &str) -> Result<(), Box<dyn Error>> {
    let mut file = File::create(filename)?;
    let mut html = String::new();

    html.push_str("<table border=\"1\">\n");
    html.push_str("<tr><th>Layer Name</th><th>Average Area</th><th>Minimum Area</th><th>Maximum Area</th></tr>\n");

    for (name, avg_area, min_area, max_area) in average_areas {
        html.push_str("<tr>");
        html.push_str(&format!("<td>{}</td>", name));
        html.push_str(&format!("<td>{:.2}</td>", avg_area));
        html.push_str(&format!("<td>{:.2}</td>", min_area)); 
        html.push_str(&format!("<td>{:.2}</td>", max_area));
        html.push_str("</tr>\n");
    }

    html.push_str("</table>\n</body>\n</html>");


    file.write_all(html.as_bytes())?;

    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    let mut rng = rand::thread_rng();
    let num_layers = 3;
    let layers = gen_obj_layer_list(&mut rng, num_layers);

    save_layers_as_csv(&layers)?;

    let average_areas = cal_average_area(&layers);
    save_average_areas_as_html(&average_areas, "areas.html")?; 

    Ok(())
}
