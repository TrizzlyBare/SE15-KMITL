#include <iostream>
#include <vector>

using namespace std;

void remove_negative(vector<double> &myVec)
{
    for (int i = 0; i < myVec.size();)
    {
        if (myVec[i] < 0)
        {
            myVec.erase(myVec.begin() + i);
        }
        else
        {
            i++;
        }
    }
}

int main()
{
    vector<double> myVec{0.8, 5.1, 1.6, -6.5, -10.5};

    // original sequence
    cout << "Original sequence: ";
    for (int i = 0; i < myVec.size(); i++)
    {
        cout << myVec[i] << " ";
    }
    cout << endl;

    // remove negative
    cout << "List after removing negative numbers: ";
    remove_negative(myVec);
    for (int i = 0; i < myVec.size(); i++)
    {
        cout << myVec[i] << " ";
    }
    cout << endl;
}