#include <iostream>
#include <vector>

using namespace std;

void lshift(vector<int> &myVec, int number)
{
    for (int i = 0; i < number; i++)
    {
        myVec.erase(myVec.begin());
    }
}

void rshift(vector<int> &myVec, int number)
{
    for (int i = 0; i < number; i++)
    {
        myVec.insert(myVec.begin(), 0);
    }
}

int main()
{
    vector<int> myVec{1, 2, 3, 4, 5};
    int number;

    // original sequence
    cout << "Original sequence: ";
    for (int i = 0; i < myVec.size(); i++)
    {
        cout << myVec[i] << " ";
    }
    cout << endl;

    // left shift
    cout << "After lshift by 2: ";
    lshift(myVec, 2);
    for (int i = 0; i < myVec.size(); i++)
    {
        cout << myVec[i] << " ";
    }
    cout << endl;

    // right shift
    cout << "After rshift by 3: ";
    rshift(myVec, 3);
    for (int i = 0; i < myVec.size(); i++)
    {
        cout << myVec[i] << " ";
    }
    cout << endl;
}
