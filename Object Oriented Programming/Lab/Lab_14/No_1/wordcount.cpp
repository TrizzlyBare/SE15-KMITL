#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Mapper
{
public:
    vector<pair<string, int> > map(const string &filename)
    {
        ifstream file(filename);
        string word;
        vector<pair<string, int> > wordCount;

        while (file >> word)
        {
            wordCount.push_back(make_pair(word, 1));
        }

        return wordCount;
    }

    void shuffle(vector<pair<string, int> > &wordCount)
    {
        sort(wordCount.begin(), wordCount.end());
    }
};

class Reducer
{
public:
    vector<pair<string, int> > reduce(const vector<pair<string, int> > &wordCount)
    {
        vector<pair<string, int> > reducedWordCount;
        pair<string, int> currentPair = wordCount[0];
        int count = 1;

        for (int i = 1; i < wordCount.size(); i++)
        {
            if (wordCount[i].first == currentPair.first)
            {
                count++;
            }
            else
            {
                reducedWordCount.push_back(make_pair(currentPair.first, count));
                currentPair = wordCount[i];
                count = 1;
            }
        }

        reducedWordCount.push_back(make_pair(currentPair.first, count));

        return reducedWordCount;
    }
};

int main()
{
    string filename;
    cout << "Enter the name of the text file: ";
    cin >> filename;

    ifstream file(filename);
    if (!file.is_open())
    {
        cout << "File does not exist." << endl;
        return 1;
    }

    Mapper mapper;
    vector<pair<string, int> > wordCount = mapper.map(filename);
    mapper.shuffle(wordCount);

    Reducer reducer;
    vector<pair<string, int> > reducedWordCount = reducer.reduce(wordCount);

    string outputFilename = filename.substr(0, filename.find('.')) + "_mr.txt";
    ofstream outputFile(outputFilename);
    for (const auto &pair : reducedWordCount)
    {
        cout << pair.first << " " << pair.second << endl;
        outputFile << pair.first << " " << pair.second << endl;
    }

    return 0;
}