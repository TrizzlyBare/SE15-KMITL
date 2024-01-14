#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int amount;
    cout << "Enter the number of integers: ";
    cin >> amount;

    vector<int> arr;

    int integer;
    for (int i = 0; i < amount; i++)
    {
        cout << "Enter an integer: ";
        cin >> integer;
        arr.push_back(integer);
    }

    int smallest = arr[0];
    for (int i = 0; i < amount; i++)
    {
        if (arr[i] < smallest)
        {
            smallest = arr[i];
        }
    }
    cout << "The smallest integer is: " << smallest << endl;
}