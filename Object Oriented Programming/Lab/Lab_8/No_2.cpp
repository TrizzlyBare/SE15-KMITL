#include <iostream>
#include <cstring>

using namespace std;

int mystery3(const char *, int &length, int &vowel);
string reverseString(const char *, size_t index = 0);
  
int main()
{
    char string1[80];
    cout << "Enter a string: ";
    cin.getline(string1, 80);

    if (strlen(string1) >= 79)
    {
        cout << "Input error or insufficient space for concatenation" << endl;
        return 0;
    }

    int length, vowel;
    mystery3(string1, length, vowel);

    cout << "Length of the string: " << length + 1 << ", Vowels: " << vowel << endl;

    string reversed = reverseString(string1, length);
    cout << "Reverse: " << reversed << endl;

    return 0;
}

int mystery3(const char *s, int &length, int &vowel)
{
    length = 0;
    vowel = 0;
    while (*s != '\0')
    {
        length++;
        if (*s == 'a' || *s == 'e' || *s == 'i' || *s == 'o' || *s == 'u')
            vowel++;
        s++;
    }
    return length;
}

string reverseString(const char *s, size_t index)
{
    if (index == 0)
    {
        return "";
    }
    else
    {
        return s[index - 1] + reverseString(s, index - 1);
    }
}
