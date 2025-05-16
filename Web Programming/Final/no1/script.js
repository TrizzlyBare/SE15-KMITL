currentValue = "";
resultDisplay = false;

let resultElement = document.getElementById("result");
let buttons = document.querySelectorAll("#table td");

function updateDisplay(value) {
    resultElement.innerText = value;
}

function handleButtonClick(value) {
    if (resultDisplay) {
        currentValue = value;
        resultDisplay = false;
    } else {
        currentValue += value;
    }
    updateDisplay(currentValue);
}

function handleDelClick() {
    if (currentValue.length > 0) {
        currentValue = currentValue.substring(0, currentValue.length - 1)
    }
    updateDisplay(currentValue || "Please dial a tel no.");
}

function handleCallClick() {
    if (resultDisplay) {
        resultDisplay = false;
    } else {
        if (currentValue.length < 10) {
            return;
        } else if (currentValue.length === 10) {
            currentValue += "Calling";
        } else {
            currentValue += "Err!";
        }
    }
    updateDisplay(currentValue);
}

buttons.forEach((button) => {
    button.addEventListener("click", () => {
        const value = button.id;

        if (!isNaN(value)) {
            handleButtonClick(value);
        } else if (value == "del") {
            handleDelClick();
        } else {
            handleCallClick();
        }
    });
});
