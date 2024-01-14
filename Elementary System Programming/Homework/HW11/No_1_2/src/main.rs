use std::fs::File;
use std::io::{BufRead, BufReader};
use std::io::prelude::*;

#[derive(Clone, PartialEq, Debug)]
struct Document {
    text: String,
}

fn make_document(text: &str) -> Document {
    Document { text: text.to_string() }
}

fn split_into_paragraphs(document: &Document) -> Vec<String> {
    document.text
        .split("\n\n")
        .map(|paragraph| paragraph.to_string())
        .collect()
}

fn rank_documents(docs: &[Document]) -> Vec<Document> {
    let mut rnk_docs = docs.to_vec();
    rnk_docs.sort_by_key(|doc| doc.text.matches("\n\n").count());
    rnk_docs.reverse();
    rnk_docs
}

#[test]
fn test_rank_documents() {
    let fox = "The quick brown fox jumps over the lazy dog.";
    let para3 = "a\n\nb\n\nc";
    let bustle = "\
    The bustle in a house\n\
    The morning after death\n\
    Is solemnest of industries\n\
    Enacted upon earth,—\n\
    \n\
    The sweeping up the heart,\n\
    And putting love away\n\
    We shall not want to use again\n\
    Until eternity.\n\
    ";
    let doc1 = make_document(fox); // 1 paragraph
    let doc2 = make_document(bustle); // 2 paragraphs
    let doc3 = make_document(para3); // 3 paragraphs
    let docs = vec![doc1.clone(), doc3.clone(), doc2.clone()];
    let rnk_docs = rank_documents(&docs);
    assert_eq!(rnk_docs, [doc3, doc2, doc1]);
}

fn read_file(filename: &str) -> String {
    let file = File::open(filename).expect("file not found");
    let mut buf_reader = BufReader::new(file);
    let mut contents = String::new();
    buf_reader.read_to_string(&mut contents).expect("unable to read file");
    contents
}

fn count_paragraphs(filename: &str) -> usize {
    let doc = make_document(&read_file(filename));
    split_into_paragraphs(&doc).len()
}

fn word_count(document: &Document) -> usize {
    document.text.split_whitespace().count()
}

fn create_html_file(docs: &[Document]) {
    let mut file = File::create("output.html").expect("unable to create file");
    let mut html = String::new();
    html.push_str("<!DOCTYPE html>\n");
    html.push_str("<html>\n");
    html.push_str("<head>\n");
    html.push_str("<title>Document Paragraphs</title>\n");
    html.push_str("</head>\n");
    html.push_str("<body>\n");
    html.push_str("<table border=\"1\">\n");
    html.push_str("<tr><th>File</th><th>Paragraphs</th><th>Word Count</th></tr>\n");
    for (i, doc) in docs.iter().enumerate() {
        html.push_str("<tr>\n");
        html.push_str("<td>File ");
        html.push_str(&format!("{}", i + 1));
        html.push_str("</td>\n");
        html.push_str("<td>\n");
        html.push_str("<p>");
        for paragraph in split_into_paragraphs(&doc) {
            html.push_str(&format!("{}\n", paragraph));
        }
        html.push_str("</p>\n");
        html.push_str("</td>\n");
        html.push_str("<td>");
        html.push_str(&word_count(&doc).to_string());
        html.push_str("</td>\n");
        html.push_str("</tr>\n");
    }
    html.push_str("</table>\n");
    html.push_str("</body>\n");
    html.push_str("</html>\n");
    file.write_all(html.as_bytes()).expect("unable to write file");
}

fn main() {
    let input_files = ["src/input/input.txt", "src/input/input2.txt", "src/input/input3.txt"];
    let mut docs = Vec::new();

    for &file in &input_files {
        docs.push(make_document(&read_file(file)));
    }

    let rnk_docs = rank_documents(&docs);
    create_html_file(&rnk_docs);
}
