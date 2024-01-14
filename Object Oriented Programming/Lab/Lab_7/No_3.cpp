#include <iostream>
#include <string>

using namespace std;

string reverse(string str = "", size_t index = 0)
{
    if (index == 0)
    {
        return "";
    }
    else
    {
        return str[index - 1] + reverse(str, index - 1);
    }
}

int main()
{
    string str;
    cout << "Enter a string: ";
    getline(cin, str); // Read a whole line

    cout << reverse(str, str.length()) << endl;

    return 0;
}
