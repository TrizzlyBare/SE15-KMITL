#include <iostream>
#include <string>

using namespace std;

class HeartRateMonitor
{
private:
    string firstname;
    string lastname;
    int birthyear;
    int birthmonth;
    int birthday;
    int age;
    int maxHeartRate;
    int minTargetHeartRate;
    int maxTargetHeartRate;

public:
    HeartRateMonitor(string firstname, string lastname, int birthyear, int birthmonth, int birthday)
        : firstname(firstname), lastname(lastname), birthyear(birthyear), birthmonth(birthmonth), birthday(birthday)
    {

        age = 2023 - birthyear;
        if (birthmonth > 12 || (birthmonth == 12 && birthday > 28))
        {
            age--;
        }

        maxHeartRate = 220 - age;

        minTargetHeartRate = static_cast<int>(maxHeartRate * 0.5);
        maxTargetHeartRate = static_cast<int>(maxHeartRate * 0.85);
    }

    void displayInformation()
    {
        cout << "Hello " << age << " years old " << firstname << " " << lastname << endl;
        cout << "Your maximum heart rate should be " << maxHeartRate << " beats per minute" << endl;
        cout << "Your Target Heart Rate: " << minTargetHeartRate << " - " << maxTargetHeartRate << " beats per minute." << endl;
    }
};

int main()
{
    string firstname, lastname;
    int birthyear, birthmonth, birthday;

    cout << "Enter your firstname: ";
    cin >> firstname;
    cout << "Enter your lastname: ";
    cin >> lastname;
    cout << "Enter your birthyear: ";
    cin >> birthyear;
    cout << "Enter your birthmonth: ";
    cin >> birthmonth;
    cout << "Enter your birthday: ";
    cin >> birthday;

    HeartRateMonitor heartRateMonitor(firstname, lastname, birthyear, birthmonth, birthday);

    heartRateMonitor.displayInformation();

    return 0;
}