function createCalendar() {
  let calendar = document.createElement("div");
  calendar.classList.add("calendar");

  let month = document.createElement("h2");
  month.textContent = "August 2024";
  calendar.appendChild(month);

  let table = document.createElement("table");
  let headerRow = document.createElement("tr");
  let days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

  days.forEach((day) => {
    let th = document.createElement("th");
    th.textContent = day;
    headerRow.appendChild(th);
  });
  table.appendChild(headerRow);

  let date = new Date(2024, 7, 1);
  let lastDate = new Date(2024, 8, 0).getDate();
  let firstDay = (date.getDay() + 6) % 7;

  let dayCounter = 1;
  let rowAdded = false;

  for (let week = 0; week < 6; week++) {
    let row = document.createElement("tr");
    for (let day = 0; day < 7; day++) {
      let td = document.createElement("td");
      if (week === 0 && day < firstDay) {
        td.textContent = "";
      } else if (dayCounter > lastDate) {
        td.textContent = "";
      } else {
        td.textContent = dayCounter;
        dayCounter++;
      }
      row.appendChild(td);
    }
    if (row.querySelector("td:not(:empty)")) {
      table.appendChild(row);
      rowAdded = true;
    } else if (rowAdded) {
      break;
    }
  }
  calendar.appendChild(table);

  document.body.appendChild(calendar);
}

createCalendar();
