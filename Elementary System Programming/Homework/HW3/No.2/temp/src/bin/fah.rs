fn main() {
    let args: Vec<String> = std::env::args().collect();

    let fahr1: f64 = match args[1].parse() {
        Ok(value) => value,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };

    let fahr2: f64 = match args[2].parse() {
        Ok(value) => value,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };

    let fahr3: f64 = match args[3].parse() {
        Ok(value) => value,
        Err(_) => {
            println!("Invalid input");
            return;
        }
    };

    println!("{}\t{}", "Fahr", "Celcius");

    if fahr2 >= fahr1 {
        let mut fahr = fahr1;
        while fahr <= fahr2 {
            let c = (5.0 / 9.0) * (fahr - 32.0);
            let formatted_c = format!("{:.1}", c);
            println!("{}\t{}", fahr, formatted_c);
            fahr += fahr3;
            if fahr3 == 0.0 {
                break;
            }
        }
    } else {
        let mut fahr = fahr1;
        while fahr >= fahr2 {
            let c = (5.0 / 9.0) * (fahr - 32.0);
            let formatted_c = format!("{:.1}", c);
            println!("{}\t{}", fahr, formatted_c);
            fahr -= fahr3;
            if fahr3 == 0.0 {
                break;
            }
        }
    }
}