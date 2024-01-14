#include <iostream>
#include <iomanip>
#include <array>
#include <string>

using namespace std;

class FoodSurvey
{
private:
    string dishes[5] = {"Pad Thai", "Som Tam", "Mango Sticky Rice", "Tom Yum Goong", "Green Curry"};
    int points[5][5] = {0};
    double average;

public:
    FoodSurvey(string dish, int pts)
    {
        dishes[0] = dish;
        points[0][0] = pts;
    }

    void collectRating()
    {
        for (int i = 0; i < 5; i++)
        {
            cout << "Poll " << i + 1 << endl;

            for (int j = 0; j < 5; j++)
            {
                cout << "Rate " << dishes[j] << " on a scale of 1 to 10: ";
                cin >> points[i][j];

                while (points[i][j] < 1 || points[i][j] > 10)
                {
                    if (cin.fail())
                    {
                        cin.clear();
                        cin.ignore(1000, '\n');
                    }
                    cout << "Invalid input. Please enter a number between 1 and 10" << endl;
                    cout << "Rate " << dishes[j] << " on a scale of 1 to 10: ";
                    cin >> points[i][j];
                }
            }
        }
    }

    void displayResults()
    {
        cout << setw(25) << left << "Dish";
        for (int i = 1; i <= 10; i++)
        {
            cout << setw(5) << right << i;
        }
        cout << setw(10) << right << "Average" << endl;

        for (int i = 0; i < 5; i++)
        {
            cout << setw(25) << left << dishes[i];
            int sum = 0;
            int count = 0;

            for (int k = 1; k <= 10; k++)
            {
                int ratingCount = 0;
                for (int j = 0; j < 5; j++)
                {
                    if (points[j][i] == k)
                    {
                        ratingCount++;
                    }
                }
                cout << setw(5) << right << ratingCount;
                sum += k * ratingCount; 
                count += ratingCount;
            }

            double dishAverage = (count != 0) ? static_cast<double>(sum) / count : 0;
            cout << setw(10) << right << dishAverage << endl;
        }

        int highestScore = 0, lowestScore = INT_MAX;
        string highestRatedDish, lowestRatedDish;

        for (int i = 0; i < 5; i++)
        {
            int dishScore = 0;
            for (int j = 0; j < 5; j++)
            {
                dishScore += points[j][i];
            }

            if (dishScore > highestScore)
            {
                highestScore = dishScore;
                highestRatedDish = dishes[i];
            }

            if (dishScore < lowestScore)
            {
                lowestScore = dishScore;
                lowestRatedDish = dishes[i];
            }
        }

        cout << "Highest Rated Dish: " << highestRatedDish << " (Score: " << highestScore << ")" << endl;
        cout << "Lowest Rated Dish: " << lowestRatedDish << " (Score: " << lowestScore << ")" << endl;
    }
};

int main()
{
    FoodSurvey survey("Pad Thai", 0);
    survey.collectRating();
    survey.displayResults();

    return 0;
}
