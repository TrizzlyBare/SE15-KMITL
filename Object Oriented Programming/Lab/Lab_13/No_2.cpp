#include <iostream>
#include <string>

class CarbonFootprint
{
public:
    virtual double getCarbonFootprint() const = 0;
    virtual ~CarbonFootprint() {}
};

class Building : public CarbonFootprint
{
    int numberOfOccupants;
    double energyConsumption;

public:
    Building(int occupants, double energy) : numberOfOccupants(occupants), energyConsumption(energy) {}
    double getCarbonFootprint() const override
    {
        return numberOfOccupants * energyConsumption * 0.00029;
    }
};

class Car : public CarbonFootprint
{
    int milesTravelled;
    double fuelEfficiency;

public:
    Car(double efficiency, int travelled) : fuelEfficiency(efficiency), milesTravelled(travelled) {}
    double getCarbonFootprint() const override
    {
        return milesTravelled / fuelEfficiency * 8.887;
    }
};

class ElectricCar : public Car
{
    double batteryCapacity;
    double chargeEfficiency;

public:
    ElectricCar(double efficiency, int travelled, double capacity, double chargeEff) : Car(efficiency, travelled), batteryCapacity(capacity), chargeEfficiency(chargeEff) {}
    double getCarbonFootprint() const override
    {
        std::cout << "Electric Car Carbon Footprint: " << batteryCapacity << chargeEfficiency << std::endl;
        return (batteryCapacity / chargeEfficiency) * 0.233; // kWh to tons of CO2 conversion factor
    }
};

class Factory : public CarbonFootprint
{
    double productionHours;
    double energyPerHour;
    double wastePerHour;
    double wasteConversionFactor;

public:
    Factory(double hours, double energy, double waste, double conversion) : productionHours(hours), energyPerHour(energy), wastePerHour(waste), wasteConversionFactor(conversion) {}
    double getCarbonFootprint() const override
    {
        return (productionHours * energyPerHour * 0.00029) + (productionHours * wastePerHour * wasteConversionFactor);
    }
};

class Bicycle : public CarbonFootprint
{
    double manufacturingEmissions;

public:
    Bicycle(double emissions) : manufacturingEmissions(emissions) {}
    double getCarbonFootprint() const override
    {
        return manufacturingEmissions;
    }
};

#include <vector>
#include <iostream>

int main()
{
    std::vector<CarbonFootprint *> objects;

    std::cout << "Enter building's energy consumption (kWh) and number of occupants: " << std::endl;
    int input1;
    int input2;
    std::cin >> input1 >> input2;

    std::cout << "Enter car's fuel consumption (miles/l) and distnace travelled (miles): " << std::endl;
    int input3;
    int input4;
    std::cin >> input3 >> input4;
    
    std::cout << "Enter Electric car's energy consumption (kWh) and charge efficiency (ratio): " << std::endl;
    int input5;
    double input6;
    std::cin >> input5 >> input6;
    objects.push_back(new Building(input1, input2));
    objects.push_back(new Car(input3, input4));
    objects.push_back(new ElectricCar(input3, input4, input5, input6));

    double totalFootprint = 0;
    for (const auto &obj : objects)
    {
        double footprint = obj->getCarbonFootprint();
        std::cout << "Carbon Footprint: " << footprint << " tons of CO2" << std::endl;
        totalFootprint += footprint;
    }

    for (auto &obj : objects)
    {
        delete obj;
    }
}