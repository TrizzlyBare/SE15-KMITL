let currentInput = "";
let resultDisplayed = false;

const resultElement = document.getElementById("result");
const buttons = document.querySelectorAll("#myTable td");

function updateDisplay(value) {
  resultElement.innerText = value;
}

function handleNumberClick(value) {
  if (resultDisplayed) {
    currentInput = value;
    resultDisplayed = false;
  } else {
    currentInput += value;
  }
  updateDisplay(currentInput);
}

function handleOperatorClick(value) {
  if (resultDisplayed) {
    resultDisplayed = false;
  }
  currentInput += value;
  updateDisplay(currentInput);
}

function handleClearClick() {
  currentInput = "";
  updateDisplay("0");
}

function handleBackspaceClick() {
  if (currentInput.length > 0) {
    currentInput = currentInput.substring(0, currentInput.length - 1);
  }
  updateDisplay(currentInput || "0");
}
function handleEqualsClick() {
  try {
    currentInput = eval(currentInput).toString();
    updateDisplay(currentInput);
    resultDisplayed = true;
  } catch (error) {
    updateDisplay("Error");
    currentInput = "";
  }
}

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const value = button.id;

    if (!isNaN(value)) {
      handleNumberClick(value);
    } else if (value === "c") {
      handleClearClick();
    } else if (value === "Backspace") {
      handleBackspaceClick();
    } else if (value === "Enter") {
      handleEqualsClick();
    } else {
      handleOperatorClick(value);
    }
  });
});

document.addEventListener("keydown", (event) => {
  const key = event.key;

  if (!isNaN(key)) {
    handleNumberClick(key);
  } else if (key === "c" || key === "C") {
    handleClearClick();
  } else if (key === "<") {
    handleBackspaceClick();
  } else if (key === "Enter" || key === "=") {
    handleEqualsClick();
  } else if (["+", "-", "*", "/"].includes(key)) {
    handleOperatorClick(key);
  }
});
