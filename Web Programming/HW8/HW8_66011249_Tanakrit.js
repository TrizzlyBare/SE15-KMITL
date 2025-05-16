let currentInput = "";
let resultDisplayed = false;
let memory = 0;

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
    currentInput = currentInput.slice(0, -1);
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

function handleScientificFunction(func) {
    try {
        let value = parseFloat(currentInput);
        switch (func) {
            case "sin":
                currentInput = Math.sin(value).toString();
                break;
            case "cos":
                currentInput = Math.cos(value).toString();
                break;
            case "tan":
                currentInput = Math.tan(value).toString();
                break;
            case "sqrt":
                currentInput = Math.sqrt(value).toString();
                break;
            case "square":
                currentInput = Math.pow(value, 2).toString();
                break;
            case "1/x":
                currentInput = (1 / value).toString();
                break;
            case "pi":
                currentInput = Math.PI.toString();
                break;
            case "factorial":
                currentInput = factorial(value).toString();
                break;
            case "mc":
                memory = 0;
                break;
            case "m+":
                memory += value;
                break;
            case "m-":
                memory -= value;
                break;
            case "mr":
                currentInput = memory.toString();
                break;
        }
        updateDisplay(currentInput);
        resultDisplayed = true;
    } catch (error) {
        updateDisplay("Error");
        currentInput = "";
    }
}

function factorial(n) {
    if (n === 0 || n === 1) return 1;
    return n * factorial(n - 1);
}

buttons.forEach((button) => {
    button.addEventListener("click", () => {
        const value = button.id;

        if (!isNaN(value) || value === ".") {
            handleNumberClick(value);
        } else if (value === "c") {
            handleClearClick();
        } else if (value === "Backspace") {
            handleBackspaceClick();
        } else if (value === "Enter") {
            handleEqualsClick();
        } else if (["sin", "cos", "tan", "sqrt", "square", "1/x", "pi", "factorial", "mc", "m+", "m-", "mr"].includes(value)) {
            handleScientificFunction(value);
        } else {
            handleOperatorClick(value);
        }
    });
});

document.addEventListener("keydown", (event) => {
    const key = event.key;

    if (!isNaN(key) || key === ".") {
        handleNumberClick(key);
    } else if (key === "c" || key === "C") {
        handleClearClick();
    } else if (key === "Backspace") {
        handleBackspaceClick();
    } else if (key === "Enter" || key === "=") {
        handleEqualsClick();
    } else if (["+", "-", "*", "/"].includes(key)) {
        handleOperatorClick(key);
    }
});