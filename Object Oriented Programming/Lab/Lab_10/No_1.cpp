#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

class Fraction
{
private:
    int numerator;
    int denominator;

    int gcd(int a, int b)
    {
        if (b == 0)
        {
            return a;
        }
        return gcd(b, a % b);
    }

    void simplify()
    {
        int divisor = gcd(numerator, denominator);
        numerator /= divisor;
        denominator /= divisor;
    }

public:
    Fraction(int numerator = 0, int denominator = 1) : numerator(numerator), denominator(denominator)
    {
        if (denominator == 0)
        {
            throw invalid_argument("Denominator cannot be zero.");
        }
        simplify();
    }

    Fraction operator+(const Fraction &other) const
    {
        int newNumerator = numerator * other.denominator + other.numerator * denominator;
        int newDenominator = denominator * other.denominator;
        return Fraction(newNumerator, newDenominator);
    }

    Fraction operator-(const Fraction &other) const
    {
        int newNumerator = numerator * other.denominator - other.numerator * denominator;
        int newDenominator = denominator * other.denominator;
        return Fraction(newNumerator, newDenominator);
    }

    Fraction operator*(const Fraction &other) const
    {
        int newNumerator = numerator * other.numerator;
        int newDenominator = denominator * other.denominator;
        return Fraction(newNumerator, newDenominator);
    }

    Fraction operator/(const Fraction &other) const
    {
        int newNumerator = numerator * other.denominator;
        int newDenominator = denominator * other.numerator;
        return Fraction(newNumerator, newDenominator);
    }

    bool operator==(const Fraction &other) const
    {
        return numerator * other.denominator == other.numerator * denominator;
    }

    bool operator<(const Fraction &other) const
    {
        return numerator * other.denominator < other.numerator * denominator;
    }

    bool operator>(const Fraction &other) const
    {
        return other < *this;
    }

    friend istream &operator>>(istream &is, Fraction &f)
    {
        char slash;
        string input;
        is >> input;

        if (!is)
        {
            is.setstate(ios::failbit);
            return is;
        }

        stringstream ss(input);
        ss >> f.numerator >> slash >> f.denominator;

        if (!ss || slash != '/' || f.denominator == 0)
        {
            is.setstate(ios::failbit);
            throw invalid_argument("Invalid fraction input.");
        }

        f.simplify();

        return is;
    }

    friend ostream &operator<<(ostream &os, const Fraction &f)
    {
        if (f.denominator < 0)
        {
            os << "-" << abs(f.numerator) << "/" << abs(f.denominator);
        }
        else
        {
            os << f.numerator << "/" << f.denominator;
        }
        return os;
    }
};

int main()
{
    Fraction f1, f2;
    cout << "Enter the first fraction (numerator/denominator): ";
    cin >> f1;
    cout << "Enter the second fraction (numerator/denominator): ";
    cin >> f2;

    cout << "f1 + f2: " << f1 + f2 << endl;
    cout << "f1 - f2: " << f1 - f2 << endl;
    cout << "f1 * f2: " << f1 * f2 << endl;
    cout << "f1 / f2: " << f1 / f2 << endl;

    if (f1 == f2)
        std::cout << "f1 and f2 are equal" << std::endl;
    if (f1 > f2)
        std::cout << "f1 is greater than f2" << std::endl;
    if (f1 < f2)
        std::cout << "f1 is less than f2" << std::endl;

    return 0;
}
