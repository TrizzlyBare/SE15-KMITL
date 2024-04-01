#include <iostream>
#include <vector>
#include <limits>

struct Movie
{
    std::string title;
    int date;
    std::vector<std::vector<int>> availableSeats;
};

struct Reservation
{
    std::string customerName = "";
    std::string movieTitle = "";
    int date = 0;
    int round = 0;
    int number = 0;

    Reservation(std::string name = "", std::string title = "", int d = 0, int r = 0, int num = 0)
        : customerName(name), movieTitle(title), date(d), round(r), number(num) {}
};

void displaySchedule(const std::vector<Movie> &movieVec)
{
    for (const Movie &movie : movieVec)
    {
        std::cout << "Movie: " << movie.title << std::endl;
        for (int date = 0; date < movie.availableSeats.size(); ++date)
        {
            std::cout << "Date: 2024-03-0" << date + 1 << " ";
            for (int round = 0; round < movie.availableSeats[date].size(); ++round)
            {
                std::cout << " " << 12 + (round) * 3 << ":00: " << movie.availableSeats[date][round] << " seats aviailable";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
}

void makeReservation(std::vector<Movie> &movieVec, std::vector<Reservation> &reserved)
{
    std::string name;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Clear input buffer
    std::cout << "Enter name: ";
    std::getline(std::cin, name);

    std::cout << "Select a movie: " << std::endl;
    for (int m = 0; m < movieVec.size(); ++m)
    {
        std::cout << m + 1 << ") " << movieVec[m].title << std::endl;
    }

    int n_movie;
    while (true)
    {
        std::cout << "Enter movie number: ";
        std::cin >> n_movie;
        if (std::cin.fail() || n_movie - 1 > movieVec.size() || n_movie - 1 < 0)
        {
            std::cout << "Invalid input." << std::endl;
            std::cin.clear();
            std::cin.ignore();
            continue;
        }
        else
        {
            break;
        }
    }
    std::cout << "Select a date: " << std::endl;
    for (int date = 0; date < movieVec[n_movie - 1].availableSeats.size(); ++date)
    {
        std::cout << date + 1 << ") Date: 2024-03-0" << date + 1 << std::endl;
    }

    int n_date;
    while (true)
    {
        std::cout << "Enter date number: ";
        std::cin >> n_date;
        if (std::cin.fail() || n_date - 1 > movieVec[n_movie - 1].availableSeats.size() || n_date - 1 < 0)
        {
            std::cout << "Invalid input." << std::endl;
            std::cin.clear();
            std::cin.ignore();
            continue;
        }
        else
        {
            break;
        }
    }
    for (int round = 0; round < movieVec[n_movie - 1].availableSeats[n_date - 1].size(); ++round)
    {
        std::cout << round + 1 << ") Round " << round + 1 << " - " << movieVec[n_movie - 1].availableSeats[n_date - 1][round] << " seats left" << std::endl;
    }
    int n_round;
    while (true)
    {
        std::cout << "Enter round number: ";
        std::cin >> n_round;
        if (std::cin.fail() || n_round - 1 > movieVec[n_movie - 1].availableSeats[n_date - 1].size() || n_round - 1 < 0)
        {
            std::cout << "Invalid input." << std::endl;
            std::cin.clear();
            std::cin.ignore();
            continue;
        }
        else
        {
            break;
        }
    }
    int seat;
    while (true)
    {
        std::cout << "Enter amount of seat: ";
        std::cin >> seat;
        if (std::cin.fail() || seat > movieVec[n_movie - 1].availableSeats[n_date - 1][n_round - 1] || seat < 0 || movieVec[n_movie - 1].availableSeats[n_date - 1][n_round - 1] - seat < 0)
        {
            std::cout << "Invalid input." << std::endl;
            std::cin.clear();
            std::cin.ignore();
            continue;
        }
        else
        {
            break;
        }
    }
    movieVec[n_movie - 1].availableSeats[n_date - 1][n_round - 1] -= seat;
    reserved.push_back(Reservation{name, movieVec[n_movie - 1].title, n_date - 1, n_round - 1, seat});
    std::cout << "Successfully reserved " << seat << " seats for " << movieVec[n_movie].title << " on 2024-03-0" << n_date << " for round " << n_round << std::endl;
}

void cancelReserved(std::vector<Movie> &movieVec, std::vector<Reservation> &reserved)
{

    std::cout << "Reserve lists: " << std::endl;
    for (Reservation i : reserved)
    {
        std::cout << "Name: " << i.customerName << " Movie: " << i.movieTitle << " Date: 2024-03-0" << i.date + 1 << " Movie Round: " << i.round + 1 << " Seats amount: " << i.number << std::endl;
    }

    std::string name;
    std::cout << "Enter name for cancellation: ";
    std::cin.ignore();
    std::getline(std::cin, name);

    for (Reservation i : reserved)
    {
        if (i.customerName == name)
        {
            for (Movie &j : movieVec)
            {
                if (j.title == i.movieTitle)
                {
                    j.availableSeats[i.date][i.round] += i.number;
                    std::cout << "Success" << std::endl;
                }
            }
        }
    }
}

int main()
{
    bool isRunning = true;

    std::vector<Reservation> reserved = {};
    std::vector<Movie> example = {
        Movie{"Poor things", 3, {{10, 10, 10, 10}, {10, 10, 10, 10}, {10, 10, 10, 10}}},
        Movie{"เหมรย", 3, {{10, 10, 10, 10}, {10, 10, 10, 10}, {10, 10, 10, 10}}},
        Movie{"4KingsII", 3, {{10, 10, 10, 10}, {10, 10, 10, 10}, {10, 10, 10, 10}}}};

    while (isRunning)
    {
        std::cout << "1. View Schedule" << std::endl;
        std::cout << "2. Make Reservation" << std::endl;
        std::cout << "3. Cancel Reservation" << std::endl;
        std::cout << "4. Exit" << std::endl;

        int choice;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice)
        {
        case 1:
            displaySchedule(example);
            break;
        case 2:
            makeReservation(example, reserved);
            break;
        case 3:
            cancelReserved(example, reserved);
            break;
        case 4:
            isRunning = false;
            std::cout << "Exiting..." << std::endl;
            break;
        default:
            std::cout << "Invalid choice. Please enter a valid option." << std::endl;
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
    }

    return 0;
}