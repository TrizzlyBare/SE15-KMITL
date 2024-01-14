use std::fs::File;
use std::io::Write;
use std::io::{BufRead, BufReader, Result};

#[derive(Debug)]
struct XPM2 {
    colors: Vec<(String, String)>,
    pixels: Vec<Vec<char>>,
    width: usize,
    height: usize,
}

fn make_xpm2(ctable: &[(&str, &str)], pixels: &[String]) -> XPM2 {
    let mut colors = Vec::new();
    let mut pixel_rows = Vec::new();
    let mut width = 0;
    let mut height = 0;

    for row in pixels {
        let row_pixels: Vec<char> = row.chars().collect();
        pixel_rows.push(row_pixels.clone());
        if row.len() > width {
            width = row.len();
        }
    }

    height = pixel_rows.len();

    for (key, value) in ctable {
        colors.push((key.to_string(), value.to_string()));
    }

    XPM2 {
        colors,
        pixels: pixel_rows,
        width,
        height,
    }
}

#[test]
fn test_make_xpm2() {
    let ctable = &[
        ("#".into(), "#000000".into()),
        ("-".into(), "#FFFFFF".into()),
    ];

    let rows = ["##--", "##--", "--##", "--##"];
    let pixels: Vec<_> = rows.iter().map(|r| r.to_string()).collect();
    let img = make_xpm2(ctable, &pixels);
    assert_eq!(
        img.colors,
        [
            ("#".into(), "#000000".into()),
            ("-".into(), "#FFFFFF".into())
        ]
    );

    assert_eq!(img.pixels.len(), 4);
    assert_eq!(img.pixels.iter().map(|r| r.len()).max(), Some(4));
    assert_eq!(img.colors.len(), 2);
}

fn make_svg_file(xpm2: &XPM2, scale: usize, filename: &str) {
    let mut file = File::create(filename).unwrap();
    let width = xpm2.width * scale;
    let height = xpm2.height * scale;

    let mut svg = format!(
        r#"<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">"#,
        width, height
    );

    svg.push_str(r#"<style type="text/css">"#);
    svg.push_str(r#"rect { stroke: #00FFFF; }"#);

    for (i, (key, value)) in xpm2.colors.iter().enumerate() {
        svg.push_str(&format!(r#"rect.c{} {{ fill: {}; }}"#, i, value));
    }

    svg.push_str(r#"</style>"#);

    for (y, row) in xpm2.pixels.iter().enumerate() {
        for (x, pixel) in row.iter().enumerate() {
            let color_index = xpm2
                .colors
                .iter()
                .position(|(key, _)| *key == pixel.to_string())
                .unwrap();

            svg.push_str(&format!(
                r#"<rect class="c{}" x="{}" y="{}" width="{}" height="{}" />"#,
                color_index,
                x * scale,
                y * scale,
                scale,
                scale
            ));
        }
    }

    svg.push_str(r#"</svg>"#);

    file.write_all(svg.as_bytes()).unwrap();
}

// fn main() {
//     let ctable = &[
//         ("#".into(), "#000000".into()),
//         ("-".into(), "#FFFFFF".into()),
//     ];

//     let rows = ["##--", "##--", "--##", "--##"];
//     let pixels: Vec<_> = rows.iter().map(|r| r.to_string()).collect();
//     let img = make_xpm2(ctable, &pixels);

//     make_svg_file(&img, 50, "test.svg");
// }
#[derive(Debug)]
struct XpmImage {
    colors: Vec<(String, String)>,
    pixels: Vec<Vec<String>>,
}

fn read_xpm2(reader: &mut BufReader<File>) -> Result<XPM2> {
    let mut header_line = String::new();
    reader.read_line(&mut header_line)?;

    if !header_line.trim().starts_with("! XPM2") {
        return Err(std::io::Error::new(
            std::io::ErrorKind::InvalidData,
            "Not a valid XPM2 image",
        ));
    }

    let mut dimensions_line = String::new();
    reader.read_line(&mut dimensions_line)?;

    let dimensions: Vec<usize> = dimensions_line
        .split_whitespace()
        .take(3)
        .filter_map(|s| s.parse().ok())
        .collect();

    let width = dimensions.get(0).cloned().unwrap_or(0);
    let height = dimensions.get(1).cloned().unwrap_or(0);
    let color_count = dimensions.get(2).cloned().unwrap_or(0);

    let mut colors: Vec<(String, String)> = Vec::new();
    for _ in 0..color_count {
        let mut color_line = String::new();
        reader.read_line(&mut color_line)?;
        let parts: Vec<&str> = color_line.trim().splitn(3, ' ').collect();
        println!("{:?}", parts);
        if parts.len() == 3 {
            colors.push((parts[0].to_string(), parts[2].to_string()));
        }
    }

    let mut pixels: Vec<Vec<char>> = Vec::new();
    for _ in 0..height {
        let mut pixel_row = String::new();
        reader.read_line(&mut pixel_row)?;
        pixel_row = pixel_row.trim().to_string();
        let pixel_row: Vec<char> = pixel_row.chars().collect();
        pixels.push(pixel_row);
    }

    Ok(XPM2{
        colors,
        pixels,
        width,
        height,
    })
}

fn main() {
    let mut reader = BufReader::new(File::open("text.xpm").unwrap());
    let img = read_xpm2(&mut reader).unwrap();
    println!("{:?}", img);
    make_svg_file(&img, 50, "test1.svg")
}