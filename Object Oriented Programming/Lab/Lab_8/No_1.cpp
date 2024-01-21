#include <iostream>

using namespace std;

void mystery1(char *, const char *);
bool mystery2(char *, const char *);

int main()
{
    char string1[80];
    char string2[80];

    cout << "Enter two strings: ";
    cin >> string1 >> string2;
    mystery1(string1, string2);
    cout << string1 << endl;

    cout << "Enter two strings: ";
    cin >> string1 >> string2;
    if (mystery2(string1, string2) == true)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}

void mystery1(char *s1, const char *s2)
{
    while (*s1 != '\0')
        s1++;

    if (strlen(s1) + strlen(s2) >= 80)
    {
        cout << "Insufficient space for concatenation" << endl;
        return;
    }

    for (; (*s1 = *s2); ++s1, ++s2)
        ;
}

bool mystery2(char *s1, const char *s2)
{
    while (*s1 != '\0')
    {
        if (*s1 == *s2)
        {
            char *temp = s1;
            while (*temp == *s2)
            {
                temp++;
                s2++;
                if (*s2 == '\0')
                    return true;
            }
            s2 -= temp - s1;
        }
        s1++;
    }
    return false;
}
