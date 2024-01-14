#include <iostream>
#include <string>

using namespace std;

const int pad = 1;
const int rows = pad * 2 + 3;

int main()
{
    cout << "Please enter P1 name: ";
    string p1Name;
    getline(cin, p1Name);

    cout << "Please enter P2 name: ";
    string p2Name;
    getline(cin, p2Name);

    const string text = "Player 1: " + p1Name + " * " + "Player 2: " + p2Name;
    const string text1 = "Player 1: " + p1Name;
    const int cols = text.length() + pad * 2 + 2;
    const int spaces = text1.length() + pad * 2 + 2;

    cout << endl;

    for (int r = 0; r < rows; ++r)
    {
        for (int c = 0; c < cols; ++c)
        {
            if (r == pad + 1 && c == pad + 1)
            {
                cout << text;
                c += text.length() - 1;
            }
            else
            {
                if (r == 0 || r == rows - 1 || c == 0 || c == cols - 1 || c == spaces - 1)
                    cout << "*";
                else
                    cout << " ";
            }
        }
        cout << endl;
    }

    return 0;
}
