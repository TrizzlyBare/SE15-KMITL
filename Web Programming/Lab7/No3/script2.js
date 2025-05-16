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
  const footerRow = document.createElement("tr");
  json.Footer.forEach((footer) => {
    const td = document.createElement("td");
    td.textContent = footer.value;
    if (footer.colspan) {
      td.colSpan = footer.colspan;
    }
    footerRow.appendChild(td);
  });
  tfoot.appendChild(footerRow);

  table.appendChild(thead);
  table.appendChild(tbody);
  table.appendChild(tfoot);
  return table;
}

// Function to convert JSON from text area to HTML table
function convertJsonToTable() {
  const jsonInput = document.getElementById("jsonInput").value;
  let jsonData;
  try {
    jsonData = JSON.parse(jsonInput);
  } catch (e) {
    alert("Invalid JSON format");
    return;
  }

  const tableContainer = document.getElementById("tableContainer");
  tableContainer.innerHTML = ""; // Clear any existing table
  tableContainer.appendChild(jsonToTable(jsonData));
}
