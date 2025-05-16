// Sample JSON data
const jsonData = {
  Header: ["head1", "head2", "head3"],
  Body: [
    { col1: "value1", col2: "value2", col3: "value3" },
    { col1: "value4", col2: "value5", col3: "value6" },
    { col1: "value7", col2: "value8", col3: "value9" },
  ],
  Footer: [{ value: "footer1", colspan: 3 }],
};

// Function to convert JSON to HTML table
function jsonToTable(json) {
  const table = document.createElement("table");
  const thead = document.createElement("thead");
  const tbody = document.createElement("tbody");
  const tfoot = document.createElement("tfoot");

  // Create table headers
  const headerRow = document.createElement("tr");
  json.Header.forEach((header) => {
    const th = document.createElement("th");
    th.textContent = header;
    headerRow.appendChild(th);
  });
  thead.appendChild(headerRow);

  // Create table body rows
  json.Body.forEach((item) => {
    const row = document.createElement("tr");
    Object.values(item).forEach((value) => {
      const td = document.createElement("td");
      td.textContent = value;
      row.appendChild(td);
    });
    tbody.appendChild(row);
  });

  // Create table footer
  json.Footer.forEach((footer) => {
    const footerRow = document.createElement("tr");
    const td = document.createElement("td");
    td.textContent = footer.value;
    td.colSpan = footer.colspan;
    footerRow.appendChild(td);
    tfoot.appendChild(footerRow);
  });

  table.appendChild(thead);
  table.appendChild(tbody);
  table.appendChild(tfoot);
  return table;
}

// Append the table to the container
document.getElementById("tableContainer").appendChild(jsonToTable(jsonData));

// Function to convert HTML table to JSON
function tableToJson(table) {
  const headers = [];
  const rows = table.querySelectorAll("tr");
  const json = { Header: [], Body: [], Footer: [] };

  // Get headers
  rows[0].querySelectorAll("th").forEach((th) => {
    headers.push(th.textContent);
    json.Header.push(th.textContent);
  });

  // Get rows data
  for (let i = 1; i < rows.length - 1; i++) {
    const row = rows[i];
    const cells = row.querySelectorAll("td");
    const rowData = {};
    cells.forEach((cell, index) => {
      rowData[`col${index + 1}`] = cell.textContent;
    });
    json.Body.push(rowData);
  }

  // Get footer data
  const footerRow = rows[rows.length - 1];
  const footerCell = footerRow.querySelector("td");
  json.Footer.push({
    value: footerCell.textContent,
    colspan: footerCell.colSpan,
  });

  return json;
}

// Function to convert table to JSON and display in textarea
function convertTableToJson() {
  const table = document.querySelector("table");
  const tableJson = tableToJson(table);
  const jsonOutput = document.getElementById("jsonOutput");
  jsonOutput.value = JSON.stringify(tableJson, null, 2);
}
