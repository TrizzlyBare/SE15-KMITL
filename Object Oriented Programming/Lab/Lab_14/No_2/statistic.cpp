#include <iostream>
#include <vector>

double c_sqrt(double x)
{
    double guess = x / 2.0;
    double prevGuess;

    do
    {
        prevGuess = guess;
        guess = (guess + x / guess) / 2.0;
    } while (prevGuess != guess);

    return guess;
}

int main()
{
    std::vector<double> numbers;
    double input;
    double sum = 0;
    double mean;
    double median;
    double standardDeviation;
    double minimum;
    double maximum;

    std::cout << "Enter a sequence of numbers (enter a non-number to stop): ";
    while (std::cin >> input)
    {
        numbers.push_back(input);
    }

    for (double number : numbers)
    {
        sum += number;
    }
    mean = sum / numbers.size();

    // Bubble sort for sorting numbers
    size_t size = numbers.size();
    for (size_t i = 0; i < size - 1; ++i)
    {
        for (size_t j = 0; j < size - i - 1; ++j)
        {
            if (numbers[j] > numbers[j + 1])
            {
                // Swap elements
                double temp = numbers[j];
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = temp;
            }
        }
    }

    if (size % 2 == 0)
    {
        median = (numbers[size / 2 - 1] + numbers[size / 2]) / 2.0;
    }
    else
    {
        median = numbers[size / 2];
    }

    sum = 0;
    for (double number : numbers)
    {
        sum += (number - mean) * (number - mean);
    }
    standardDeviation = c_sqrt(sum / numbers.size());

    minimum = numbers[0];
    maximum = numbers[size - 1];

    printf("Mean: %.2f\n", mean);
    printf("Median: %.2f\n", median);
    printf("Standard Deviation: %.2f\n", standardDeviation);
    printf("Minimum: %.2f\n", minimum);
    printf("Maximum: %.2f\n", maximum);

    return 0;
}
