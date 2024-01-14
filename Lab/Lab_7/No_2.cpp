#include <iostream>
#include <array>
#include <random>

using namespace std;

int findMax(const array<int, 10> &arr, int max, size_t index)
{
    if (index == arr.size())
    {
        return max;
    }
    else
    {
        if (arr[index] > max)
        {
            max = arr[index];
        }
        return findMax(arr, max, index + 1);
    }
}

int main()
{
    array<int, 10> arr;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 100);

    for (size_t i = 0; i < 10; i++)
    {
        arr[i] = dis(gen);
    }

    cout << "Generate 10 random integers between 1 and 100: " << endl;
    for (const auto &element : arr)
    {
        cout << element << " ";
    }
    cout << endl;

    cout << "The largest element in the array is: " << findMax(arr, arr[0], 0) << endl;

    return 0;
}
