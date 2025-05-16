function calculate() {
  let weight = parseFloat(document.getElementById("weight").value);
  let height = parseFloat(document.getElementById("height").value);

  let bmi = weight / (height * height);

  let under = document.getElementById("underweight");
  let norm = document.getElementById("normal");
  let over = document.getElementById("overweight");
  let ob = document.getElementById("obese");
  let table = document.getElementById("btable");
  let text = document.getElementById("summaryText");
  let user = document.getElementById("name");
  var recog;

  table.style.display = "block";

  if (bmi >= 30) {
    ob.style.backgroundColor = "yellow";
    recog = "obese";
  } else if (bmi >= 25.0 && bmi <= 29.9) {
    over.style.backgroundColor = "yellow";
    recog = "overweight";
  } else if (bmi >= 18.5 && bmi <= 24.9) {
    norm.style.backgroundColor = "yellow";
    recog = "normal";
  } else {
    under.style.backgroundColor = "yellow";
    recog = "underweight";
  }

  text.innerHTML =
    "BMI of " +
    user.value +
    " is " +
    bmi.toFixed(2) +
    " and you are " +
    recog +
    ".";
}
