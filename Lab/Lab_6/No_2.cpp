#include <iostream>
#include <string>
#include <vector>

using namespace std;

class QuizQuestion
{
private:
    string question;
    string choiceA;
    string choiceB;
    string choiceC;
    string answer;

public:
    QuizQuestion(string ques, string A, string B, string C, string ans)
    {
        question = ques;
        choiceA = A;
        choiceB = B;
        choiceC = C;
        answer = ans;
    }

    void displayQuestion()
    {
        cout << question << endl;
        cout << "A. " << choiceA << endl;
        cout << "B. " << choiceB << endl;
        cout << "C. " << choiceC << endl;
    }

    bool checkAnswer(string ans)
    {
        while (true)
        {
            switch (ans[0])
            {
            case 'a':
            case 'A':
                return answer == "a" || answer == "A";
            case 'b':
            case 'B':
                return answer == "b" || answer == "B";
            case 'c':
            case 'C':
                return answer == "c" || answer == "C";

            default:
                cout << "Invalid input. Please enter a, b, or c" << endl;
                cout << "Enter your answer: ";
                cin >> ans;
                break;
            }
        }
    }
};

int main()
{
    QuizQuestion quizQuestion("What is the capital of France?", "Berlin", "Paris", "London", "b");
    QuizQuestion quizQuestion2("Which planet is known as the Red Planet?", "Mars", "Jupiter", "Saturn", "a");
    QuizQuestion quizQuestion3("What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "b");
    QuizQuestion quizQuestion4("Who wrote 'Hamlet'?", "Mark Twain", "Charles Dickens", "William Shakespeare", "c");
    QuizQuestion quizQuestion5("What is the chemical symbol for water?", "H20", "CO2", "O2", "a");

    vector<QuizQuestion> questions{quizQuestion, quizQuestion2, quizQuestion3, quizQuestion4, quizQuestion5};

    int score = 0;
    string answer;

    int i = 0;
    while (i < questions.size())
    {
        questions[i].displayQuestion();
        cout << "Enter your answer: ";
        cin >> answer;

        if (questions[i].checkAnswer(answer))
        {
            cout << "Correct!" << endl;
            score++;
        }
        else if (answer != "a" && answer != "b" && answer != "c")
        {
            cout << "Invalid answer!" << endl;
        }
        else
        {
            cout << "Incorrect!" << endl;
        }

        i++;
    }
    cout << "Your total score: " << score << "/" << questions.size() << endl;
}