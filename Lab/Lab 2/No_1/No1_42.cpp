#include <iostream>
#include <string>

using namespace std;

const int pad = 1;
const int rows = pad * 4 + 5;

int main()
{
    cout << "Please enter P1 name: ";
    string p1Name;
    getline(cin, p1Name);

    cout << "Please enter P2 name: ";
    string p2Name;
    cin >> p2Name;

    const string greeting1 = "Player 1: " + p1Name;
    const string greeting2 = "Player 2: " + p2Name;

    const int cols = max(greeting1.size(), greeting2.size()) + pad * 2 + 2;

    cout << endl;

    for (int r = 0; r != rows; ++r)
    {
        int c = 0;
        while (c != cols)
        {
            if (r == pad + 1 && c == pad + 1)
            {
                cout << greeting1;
                c += greeting1.size();
            }
            else if (r == pad * 3 + 1 && c == pad + 1)
            {
                for (int i = 0; i < cols - 2 * pad - 2; ++i)
                {
                    cout << "-";
                }
                c += cols - 2 * pad - 2;
            }
            else if (r == rows - pad - 2 && c == pad + 1)
            {
                cout << greeting2;
                c += greeting2.size();
            }
            else
            {
                if ((r == 0 && c == 0) || (r == 0 && c == cols - 1) || (r == rows - 1 && c == 0) || (r == rows - 1 && c == cols - 1))
                {
                    cout << "+";
                }
                else if (r == 0 || r == rows - 1)
                {
                    cout << "-";
                }
                else if (r == pad * 2 + 2 && (c == 0 || c == cols - 1))
                {
                    cout << "+";
                }
                else if (c == 0 || c == cols - 1)
                {
                    cout << "|";
                }
                else
                {
                    cout << " ";
                }
                ++c;
            }
        }
        cout << endl;
    }

    return 0;
}
