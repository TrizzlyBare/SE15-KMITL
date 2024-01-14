#include <random>
#include <iostream>
#include <iomanip>
#include <cmath>

class Rand_double
{
public:
    Rand_double(double low, double high) : dist(low, high)
    {
        std::random_device rd;
        re.seed(rd());
    }
    double operator()()
    {
        return dist(re);
    }

private:
    std::default_random_engine re;
    std::uniform_real_distribution<double> dist;
};

int main()
{
    const double rnd_min = -1.0, rnd_max = 1.0;
    Rand_double rnd(rnd_min, rnd_max);

    const int N = 100000; // Number of points to generate
    int points_inside = 0;

    for (int i = 0; i < N; ++i)
    {
        double x = rnd();
        double y = rnd();
        double distance_squared = std::sqrt(x * x + y * y);

        if (distance_squared <= 1 && distance_squared >= -1)
        {
            ++points_inside;
        }
    }

    double probability = static_cast<double>(points_inside) / N;
    double pi_estimate = probability * 4;

    std::cout << std::fixed << std::setprecision(3);
    std::cout << "Estimated Pi: " << pi_estimate << std::endl;
    return 0;
}
