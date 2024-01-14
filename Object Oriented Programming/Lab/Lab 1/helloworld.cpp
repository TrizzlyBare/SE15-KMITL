#include <iostream>

void hello()
{
    std::cout << "Hello World!" << std::endl;
    std::cout << "This is my first program in C++" << std::endl;
    std::cout << "Good bye!" << std::endl;

}

int main() {
    double num1, num2;
    char operation;

    std::cout << "Enter first number: ";
    std::cin >> num1;

    std::cout << "Enter operator (+, -, *, /): ";
    std::cin >> operation;

    std::cout << "Enter second number: ";
    std::cin >> num2;

    switch(operation) {
        case '+':
            std::cout << "Result: " << num1 + num2 << std::endl;
            break;
        case '-':
            std::cout << "Result: " << num1 - num2 << std::endl;
            break;
        case '*':
            std::cout << "Result: " << num1 * num2 << std::endl;
            break;
        case '/':
            if(num2 != 0)
                std::cout << "Result: " << num1 / num2 << std::endl;
            else
                std::cout << "Error! Division by zero." << std::endl;
            break;
        default:
            std::cout << "Invalid operator!" << std::endl;
    }

    return 0;
}