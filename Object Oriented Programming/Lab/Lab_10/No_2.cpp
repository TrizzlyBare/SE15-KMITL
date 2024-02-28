#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Polynomial
{
public:
    struct Term
    {
        int coefficient;
        int exponent;

        Term(int coeff, int exp) : coefficient(coeff), exponent(exp) {}
    };

private:
    vector<Term> terms;

    void simplify()
    {
        sort(terms.begin(), terms.end(),
             [](const Term &a, const Term &b)
             { return a.exponent > b.exponent; });

        for (size_t i = 0; i < terms.size() - 1; ++i)
        {
            if (terms[i].exponent == terms[i + 1].exponent)
            {
                terms[i].coefficient += terms[i + 1].coefficient;
                terms.erase(terms.begin() + i + 1);
                --i;
            }
        }
    }

public:
    Polynomial() = default;

    explicit Polynomial(const vector<Term> &terms) : terms(terms)
    {
        simplify();
    }

    const vector<Term> &getTerms() const
    {
        return terms;
    }

    void setPoly(int coefficient, int exponent)
    {
        // Error handling for invalid coefficients or exponents
        if (exponent < 0)
        {
            throw invalid_argument("Exponent cannot be negative.");
        }

        auto it = find_if(terms.begin(), terms.end(),
                          [exponent](const Term &term)
                          { return term.exponent == exponent; });

        if (it != terms.end())
        {
            it->coefficient = coefficient;
        }
        else
        {
            terms.push_back(Term(coefficient, exponent));
        }

        simplify();
    }

    Polynomial &operator=(const Polynomial &other)
    {
        if (this != &other)
        {
            terms = other.terms;
        }
        return *this;
    }

    Polynomial operator+(const Polynomial &other) const
    {
        Polynomial result = *this;
        result.terms.insert(result.terms.end(), other.terms.begin(), other.terms.end());
        result.simplify();
        return result;
    }

    Polynomial &operator+=(const Polynomial &other)
    {
        *this = *this + other;
        return *this;
    }

    Polynomial operator-(const Polynomial &other) const
    {
        Polynomial result = *this;
        for (const auto &term : other.terms)
        {
            result.setPoly(-term.coefficient, term.exponent);
        }
        result.simplify();
        return result;
    }

    Polynomial &operator-=(const Polynomial &other)
    {
        *this = *this - other;
        return *this;
    }

    Polynomial operator*(const Polynomial &other) const
    {
        Polynomial result;
        vector<Term> tempResult;

        for (const auto &term1 : terms)
        {
            for (const auto &term2 : other.terms)
            {
                int newCoefficient = term1.coefficient * term2.coefficient;
                int newExponent = term1.exponent + term2.exponent;

                auto it = find_if(tempResult.begin(), tempResult.end(),
                                  [newExponent](const Term &term)
                                  { return term.exponent == newExponent; });

                if (it != tempResult.end())
                {
                    it->coefficient += newCoefficient;
                }
                else
                {
                    tempResult.push_back(Term(newCoefficient, newExponent));
                }
            }
        }
        result.terms = std::move(tempResult);
        result.simplify();

        return result;
    }

    Polynomial &operator*=(const Polynomial &other)
    {
        *this = *this * other;
        return *this;
    }

    friend ostream &operator<<(ostream &os, const Polynomial &poly)
    {
        for (const auto &term : poly.terms)
        {
            os << (term.coefficient > 0 ? "+" : "") << term.coefficient << "x^" << term.exponent << " ";
        }
        return os;
    }
};

int main()
{
    try
    {
        Polynomial p1;
        p1.setPoly(2, 3);
        p1.setPoly(4, 1);

        Polynomial p2;
        p2.setPoly(3, 2);
        p2.setPoly(5, 0);

        Polynomial p3 = p1 + p2;
        Polynomial p4 = p1 - p2;
        Polynomial p5 = p1 * p2;

        cout << "Polynomial p1: " << p1 << endl;
        cout << "Polynomial p2: " << p2 << endl;
        cout << "Polynomial p3 (p1 + p2): " << p3 << endl;
        cout << "Polynomail p4 (p1 - p2): " << p4 << endl;
        cout << "Polynomail p5 (p1 * p2): " << p5 << endl;
    }
    catch (const invalid_argument &e)
    {
        cerr << "Errpr" << e.what() << endl;
    }

    return 0;
}
