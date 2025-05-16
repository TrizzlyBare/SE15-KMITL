const calendar = document.getElementById("calendar");
const monthYear = document.getElementById("month-year");
const prevMonthButton = document.getElementById("prev-month");
const nextMonthButton = document.getElementById("next-month");

let currentMonth = 1;
let currentYear = 2024;

function updateCalendar() {
    monthYear.textContent = `${currentMonth}/${currentYear}`;

    const daysInMonth = new Date(currentYear, currentMonth, 0).getDate();
    let firstDay = new Date(currentYear, currentMonth - 1, 1).getDay();
    firstDay = firstDay === 0 ? 6 : firstDay - 1;

    let table = "<table><tr>";
    const daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

    for (let day of daysOfWeek) {
        table += `<th>${day}</th>`;
    }
    table += "</tr>";

    let day = 1;
    for (let week = 0; week < 6; week++) {
        table += "<tr>";
        for (let i = 0; i < 7; i++) {
            if (week === 0 && i < firstDay) {
                table += "<td></td>";
            } else if (day > daysInMonth) {
                table += "<td></td>";
            } else {
                const className = i === 6 ? "sunday" : "";
                table += `<td class="${className}">${day}</td>`;
                day++;
            }
        }
        table += "</tr>";
        if (day > daysInMonth) break;
    }

    table += "</table>";
    calendar.innerHTML = table;
}

prevMonthButton.addEventListener("click", () => {
    if (currentMonth === 1 && currentYear === 2024) {
        return;
    } else if (currentMonth === 1) {
        currentMonth = 12;
        currentYear--;
    } else {
        currentMonth--;
    }
    updateCalendar();
});

nextMonthButton.addEventListener("click", () => {
    if (currentMonth === 12 && currentYear === 2024) {
        return;
    } else if (currentMonth === 12) {
        currentMonth = 1;
        currentYear++;
    } else {
        currentMonth++;
    }
    updateCalendar();
});

updateCalendar();
