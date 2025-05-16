var AlertTime = [
  { time: "09.00", alert: "Wake up" },
  { time: "11.05", alert: "Brush teeth" },
  { time: "15.30", alert: "Take a shower" },
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

updateCurrentTime();
