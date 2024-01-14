use scraper::{Html, Selector};
use std::error::Error;
use std::fs;
use std::io::Write;
use xml::writer::{EmitterConfig, XmlEvent};

pub fn html_to_xml(html: &str) -> Result<(), Box<dyn Error>> {
    let document = Html::parse_document(html);
    let selector = Selector::parse("table").unwrap();
    let table = document
        .select(&selector)
        .next()
        .ok_or("No table found in the HTML")?;

    let config = EmitterConfig::new().perform_indent(true);
    let mut writer = config.create_writer(Vec::<u8>::new());

    writer.write(XmlEvent::start_element("table"))?;

    for row in table.select(&Selector::parse("tr").unwrap()) {
        writer.write(XmlEvent::start_element("tr"))?;

        for cell in row.select(&Selector::parse("th, td").unwrap()) {
            let name = cell.value().name();
            writer.write(XmlEvent::start_element(name))?;
            writer.write(XmlEvent::characters(
                cell.text().collect::<String>().as_str(),
            ))?;
            writer.write(XmlEvent::end_element())?;
        }

        writer.write(XmlEvent::end_element())?;
    }

    writer.write(XmlEvent::end_element())?;

    let result = writer.into_inner();
    let mut output_file = fs::File::create("output.xml")?;
    output_file.write_all(&result)?;

    Ok(())
}