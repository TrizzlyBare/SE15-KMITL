#include <iostream>
#include <string>
#include <vector>

using namespace std;

class MazeGenerator
{
public:
    MazeGenerator(int mazeLength) : length(mazeLength), path(generateRandomPath(mazeLength))
    {
        srand(time(NULL));
    }

    void printMaze()
    {
        for (int row = 0; row < 15; ++row)
        {
            for (int col = 0; col < 15; ++col)
            {
                if (col == 0 || col == 14)
                {
                    cout << "#";
                }
                else if (row % 2 == 0)
                {
                    printEvenRow(row, col);
                }
                else
                {
                    printOddRow(row, col);
                }
            }
            cout << endl;
        }
    }

private:
    int length;
    vector<int> path;

    void printByChance(int chance, char charIfTrue, char charIfFalse)
    {
        int n = rand() % 10 + 1;
        if (n <= chance)
        {
            cout << charIfTrue;
        }
        else
        {
            cout << charIfFalse;
        }
    }

    vector<int> generateRandomPath(int length)
    {
        vector<int> newPath;
        for (int i = 0; i < length; ++i)
        {
            newPath.push_back(rand() % 13 + 1);
        }
        return newPath;
    }

    void printEvenRow(int row, int col)
    {
        if (col == path[row / 2])
        {
            cout << ".";
        }
        else
        {
            if (row == 0 || row == 14)
            {
                cout << "#";
            }
            else
            {
                printByChance(9, '#', ' ');
            }
        }
    }

    void printOddRow(int row, int col)
    {
        int start = min(path[row / 2], path[row / 2 + 1]);
        int end = max(path[row / 2], path[row / 2 + 1]);

        if (col >= start && col <= end)
        {
            cout << ".";
        }
        else
        {
            printByChance(1, '#', ' ');
        }
    }
};

int main()
{
    MazeGenerator maze(8);
    maze.printMaze();

    return 0;
}
