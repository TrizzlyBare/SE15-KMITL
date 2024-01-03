#include <iostream>
#include <string>
#include <random>

using namespace std;

class GuessNumberGame
{
private:
    int randomNumber;
    int guessNumber;
    int guessCount;
    bool isCorrect;
    default_random_engine re;

public:
    GuessNumberGame()
        : guessCount(0), isCorrect(false)
    {
        random_device rd;
        re.seed(rd());
    }

    void generateRandomNum()
    {
        uniform_int_distribution<> dis(1, 100);
        randomNumber = dis(re);
    }

    void guess()
    {
        cout << "Guess a number (between 1 and 100): ";
        cin >> guessNumber;

        if (cin.fail())
        {
            cout << "Invalid input" << endl;
            return;
        }

        if (guessNumber == randomNumber)
        {
            isCorrect = true;
        }
        else if (guessNumber > randomNumber)
        {
            cout << "Too high. Try again." << endl;
        }
        else
        {
            cout << "Too low. Try again." << endl;
        }

        guessCount++;
    }

    bool getIsCorrect() const
    {
        return isCorrect;
    }

    int getRandomNumber() const
    {
        return randomNumber;
    }

    int getGuessCount() const
    {
        return guessCount;
    }
};

int main()
{
    string continueAnswer;
    GuessNumberGame guessNumberGame;

    while (true)
    {
        guessNumberGame.generateRandomNum();

        while (!guessNumberGame.getIsCorrect() && guessNumberGame.getGuessCount() < 10)
        {
            guessNumberGame.guess();
            if (guessNumberGame.getIsCorrect())
            {
                cout << "Congratulations! You win." << endl;
                break;
            }
            else if (guessNumberGame.getGuessCount() == 10)
            {
                cout << "You lose. The number was " << guessNumberGame.getRandomNumber() << endl;
                break;
            }
        }
        break;
    }
    return 0;
}
