#include <iostream>
#include <list>

using namespace std;

void remove_negative(list<double> &myList)
{
    for (list<double>::iterator i = myList.begin(); i != myList.end();)
    {
        if (*i < 0)
        {
            i = myList.erase(i); // erase returns the iterator to the next valid position
        }
        else
        {
            ++i;
        }
    }
}

int main()
{
    list<double> myList{0.8, -5.1, 1.6, 6.5, 10.5};

    // original sequence
    cout << "Original sequence: ";
    for (const double &value : myList)
    {
        cout << value << " ";
    }
    cout << endl;

    // remove negative
    cout << "List after removing negative numbers: ";
    remove_negative(myList);
    for (const double &value : myList)
    {
        cout << value << " ";
    }
    cout << endl;
}
