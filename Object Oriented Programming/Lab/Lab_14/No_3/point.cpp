#include <iostream>
#include <sstream>

class Point
{
private:
    int xCoordinate;
    int yCoordinate;

public:
    Point() : xCoordinate(0), yCoordinate(0) {}

    friend std::istream &operator>>(std::istream &input, Point &point);
    friend std::ostream &operator<<(std::ostream &output, const Point &point);
};

std::istream &operator>>(std::istream &input, Point &point)
{
    std::cout << "Enter the coordinates of the point (x, y): ";
    input >> point.xCoordinate >> point.yCoordinate;

    if (input.fail())
    {
        input.clear();
    }

    return input;
}

std::ostream &operator<<(std::ostream &output, const Point &point)
{
    output << "(" << point.xCoordinate << ", " << point.yCoordinate << ")";
    return output;
}

int main()
{
    Point myPoint;

    std::cin >> myPoint;

    if (std::cin.fail())
    {
        std::cout << "Invalid input. Exiting program." << std::endl;
        return 1;
    }

    std::cout << "The point is: " << myPoint << std::endl;

    return 0;
}
