#include <iostream>
#include <string>

using namespace std;

class TemperatureConverter
{
private:
    double temperature;

public:
    TemperatureConverter(double temp)
    {
        temperature = temp;
    }

    double getCelsius()
    {
        return (temperature - 32) * 5 / 9;
    }

    double getFahrenheit()
    {
        return temperature * 9 / 5 + 32;
    }
};

double temperature;
string conversionType;
string continueAnswer;

int main()
{
    while (true)
    {
        cout << "Enter temperature: ";

        cin >> temperature;

        if (cin.fail())
        {
            cout << "Invalid input" << endl;
            break;
        }

        // Select the conversion type
        cout << "Convert to (C)elcius or (F)ahrenheit? Enter C or F: ";

        cin >> conversionType;

        TemperatureConverter temperatureConverter(temperature);
        if (conversionType == "C" || conversionType == "c")
        {
            cout << temperature << " Fahrenheit is " << temperatureConverter.getCelsius() << " Celsius." << endl;
        }
        else if (conversionType == "F" || conversionType == "f")
        {
            cout << temperature << " Celcius is " << temperatureConverter.getFahrenheit() << " Fahrenheit." << endl;
        }
        else
        {
            cout << "Invalid conversion type" << endl;
            break;
        }

        // Ask the user if they want to continue

        cout << "Do you want to perform another conversion? (Y/N): ";
        cin >> continueAnswer;

        if (continueAnswer == "Y" || continueAnswer == "y")
        {
            continue;
        }
        else if (continueAnswer == "N" || continueAnswer == "n")
        {
            break;
        }
        else
        {
            cout << "Invalid input" << endl;
            break;
        }
        return 0;
    }
}
