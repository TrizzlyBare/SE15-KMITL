#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

class PopulationGrowth
{
private:
    double initialPopulation;
    double annualGrowthRate;

public:
    PopulationGrowth(double Population, double GrowthRate)
    {
        initialPopulation = Population;
        annualGrowthRate = GrowthRate;
    }

    void setInitialPopulation(double Population)
    {
        initialPopulation = Population;
    }

    void setAnnualGrowthRate(double GrowthRate)
    {
        annualGrowthRate = GrowthRate;
    }

    double getInitialPopulation() const
    {
        return initialPopulation;
    }

    double getAnnualGrowthRate() const
    {
        return annualGrowthRate;
    }

    double getPopulationSize(double year) const
    {
        return initialPopulation * pow((1 + annualGrowthRate / 100), year);
    }

    double getAnnualIncrease(double year) const
    {
        return getPopulationSize(year) - getPopulationSize(year - 1);
    }

    double getDoublePopulation() const
    {
        double year = 0;
        while (getPopulationSize(year) < 2 * initialPopulation)
        {
            year++;
        }
        return year;
    }
};

int main()
{
    double population;
    double growthRate;

    cout << "Enter the initial population: ";
    cin >> population;

    cout << "Enter the annual growth rate (%): ";
    cin >> growthRate;
    cout << endl;

    PopulationGrowth populationGrowth(population, growthRate);

    cout << "Year\tProjected Population\tAnnual Increase" << endl;

    for (int i = 1; i <= 75; i++)
    {
        cout.imbue(locale(""));
        cout << i << "\t" << fixed << setprecision(0) << populationGrowth.getPopulationSize(i) << "\t\t" << fixed << setprecision(0) << populationGrowth.getAnnualIncrease(i) << endl;
    }

    cout << "The population will double in " << populationGrowth.getDoublePopulation() << " years." << endl;

    return 0;
}
