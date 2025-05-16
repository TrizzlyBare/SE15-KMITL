var AlertTime = [
  { time: "09.00", alert: "Wake up" },
  { time: "11.05", alert: "Lunch time" },
  { time: "15.30", alert: "Take a break" },
];

var time = 8 * 3600 * 1000;
var timer = setInterval(function () {
  time += 1000;
  for (var i = 0; i < AlertTime.length; i++) {
    const alertTimeParts = AlertTime[i].time.split(".");
    const alertTimeInMs =
      (parseInt(alertTimeParts[0]) * 3600 + parseInt(alertTimeParts[1]) * 60) *
      1000;
    if (time == alertTimeInMs) {
      alert(AlertTime[i].alert);
    }
  }
  updateCurrentTime();
}, 1);

function updateCurrentTime() {
  const displayCurrentTime = document.getElementById("displayCurrentTime");
  const now = new Date(time);
  const hours = now.getUTCHours().toString().padStart(2, "0");
  const minutes = now.getUTCMinutes().toString().padStart(2, "0");
  const seconds = now.getUTCSeconds().toString().padStart(2, "0");
  displayCurrentTime.innerHTML = `${hours}:${minutes}:${seconds}`;
}

function toggleEdit() {
  const alertTimes = document.querySelectorAll(".alertTime");
  const alertMessages = document.querySelectorAll(".alertMessage");
  const alertTimeInputs = document.querySelectorAll(".alertTimeInput");
  const alertMessageInputs = document.querySelectorAll(".alertMessageInput");
  const editButton = document.getElementById("editButton");
  const removeButtons = document.querySelectorAll(".removeButton");
  const addRowButton = document.getElementById("addRowButton");

  if (editButton.innerText === "Edit") {
    alertTimes.forEach((span, index) => {
      span.style.display = "none";
      alertTimeInputs[index].style.display = "inline";
    });
    alertMessages.forEach((span, index) => {
      span.style.display = "none";
      alertMessageInputs[index].style.display = "inline";
    });
    removeButtons.forEach((button) => (button.style.display = "inline"));
    addRowButton.style.display = "inline";
    editButton.innerText = "Done";
  } else {
    alertTimes.forEach((span, index) => {
      span.innerText = alertTimeInputs[index].value;
      span.style.display = "inline";
      alertTimeInputs[index].style.display = "none";
    });
    alertMessages.forEach((span, index) => {
      span.innerText = alertMessageInputs[index].value;
      span.style.display = "inline";
      alertMessageInputs[index].style.display = "none";
    });
    removeButtons.forEach((button) => (button.style.display = "none"));
    addRowButton.style.display = "none";
    editButton.innerText = "Edit";

    AlertTime = Array.from(alertTimes).map((span, index) => ({
      time: alertTimeInputs[index].value,
      alert: alertMessageInputs[index].value,
    }));
    alert("Alerts updated!");
  }
}

function addRow() {
  const table = document.getElementById("alertTable");
  const row = table.insertRow();
  const timeCell = row.insertCell(0);
  const alertCell = row.insertCell(1);
  const actionCell = row.insertCell(2);

  timeCell.innerHTML =
    '<span class="alertTime" style="display:none;"></span><input type="text" class="alertTimeInput">';
  alertCell.innerHTML =
    '<span class="alertMessage" style="display:none;"></span><input type="text" class="alertMessageInput">';
  actionCell.innerHTML =
    '<button class="removeButton" onclick="removeRow(this)">Remove</button>';

  AlertTime.push({ time: "", alert: "" });
}

function removeRow(button) {
  const row = button.parentElement.parentElement;
  const rowIndex = Array.from(row.parentElement.children).indexOf(row) - 1;
  AlertTime.splice(rowIndex, 1);
  row.remove();
}

updateCurrentTime();
