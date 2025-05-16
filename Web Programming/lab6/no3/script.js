function calculate() {
  let weight = parseFloat(document.getElementById("weight").value);
  let height = parseFloat(document.getElementById("height").value);

  let heightCon = height / 100;

  let bmi = weight / (heightCon * heightCon);

  let under = document.getElementById("underweight");
  let norm = document.getElementById("normal");
  let over = document.getElementById("overweight");
  let ob = document.getElementById("obese");
  let table = document.getElementById("btable");
  let text = document.getElementById("summaryText");
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
    "With your weight of " +
    weight +
    " kg and height of " +
    height +
    " cm.\nYour BMI is " +
    bmi;
}
