#include <iostream>

using namespace std;

int mystery(int a, int b)
{
    if (b == 1)
    {
        return a;
    }
    else if (a == 0 || b == 0)
    {
        cout << "a or b is zero." << endl;
        return 0;
    }
    else if (a < 0 && b < 0)
    {
        cout << "a and b are negative" << endl;
        return 0;
    }
    else if (b < 0)
    {
        cout << "b is negative" << endl;
        return 0;
    }
    else if (a < 0)
    {
        cout << "a is negative" << endl;
        return 0;
    }
    else
    {
        return a + mystery(a, b - 1);
    }
}

int main()
{
    int x = 0;
    int y = 0;

    cout << "Enter two integers: ";
    if (!(cin >> x >> y) || cin.fail())
    {
        cout << "Invalid input" << endl;
        return 0;
    }

    cout << "The result is " << mystery(x, y) << endl;

    return 0;
}
