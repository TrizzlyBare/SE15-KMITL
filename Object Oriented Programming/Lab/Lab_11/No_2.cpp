#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>

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
        : customerName(name), movieTitle(title), date(d), round(r), number(num)
    {
    }
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
                std::cout << ", " << 12 + (round) * 3 << ":00: " << movie.availableSeats[date][round];
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }
}

void makeReservation(std::vector<Movie> &movieVec, std::vector<Reservation> &reserved)
{
    std::string name;
    std::cout << "Enter name: ";
    std::cin.ignore();
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
        if (std::cin.fail() || n_movie - 1 >= movieVec.size() || n_movie - 1 < 0)
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
        if (std::cin.fail() || n_date - 1 >= movieVec[n_movie - 1].availableSeats.size() || n_date - 1 < 0)
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
        if (std::cin.fail() || n_round - 1 >= movieVec[n_movie - 1].availableSeats[n_date - 1].size() || n_round - 1 < 0)
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
    std::cout << "Successfully reserved " << seat << " seats for " << movieVec[n_movie - 1].title << " on 2024-03-0" << n_date << " for round " << n_round << std::endl;
}

void cancelReservation(std::vector<Movie> &movieVec, std::vector<Reservation> &reserved)
{
    std::cout << "Reservation list: " << std::endl;
    for (Reservation &reservation : reserved)
    {
        std::cout << reservation.customerName << ", " << reservation.movieTitle << ", 2024-03-0" << reservation.date + 1 << ", " << reservation.round + 1 << ", " << reservation.number << std::endl;
    }

    std::string name;
    std::cout << "Enter name to cancel: ";
    std::cin.ignore();
    std::getline(std::cin, name);

    bool reservationCanceled = false;
    for (Reservation &reservation : reserved)
    {
        if (reservation.customerName == name)
        {
            for (Movie &movie : movieVec)
            {
                if (movie.title == reservation.movieTitle)
                {
                    movie.availableSeats[reservation.date][reservation.round] += reservation.number;
                    reservation.customerName = ""; // Mark reservation as canceled by clearing the name
                    reservationCanceled = true;
                    std::cout << "Success" << std::endl;
                    break;
                }
            }
            if (reservationCanceled)
            {
                break; // No need to continue searching if reservation is found and canceled
            }
        }
    }

    if (!reservationCanceled)
    {
        std::cout << "No reservation found for the given name." << std::endl;
    }
}

void saveMoviesData(const std::vector<Movie> &movies, const std::string &filename)
{
    std::ofstream file(filename);
    if (!file.is_open())
    {
        std::cerr << "Error opening file for writing." << std::endl;
        return;
    }

    for (const Movie &movie : movies)
    {
        file << movie.title << "," << movie.date;
        for (const auto &seats : movie.availableSeats)
        {
            for (int seat : seats)
            {
                file << "," << seat;
            }
        }
        file << "\n";
    }
    file.close();
}

void saveReservationsData(const std::vector<Reservation> &reservations, const std::string &filename)
{
    std::ofstream file(filename);
    if (!file.is_open())
    {
        std::cerr << "Error opening file for writing." << std::endl;
        return;
    }

    for (const Reservation &reservation : reservations)
    {
        if (!reservation.customerName.empty())
        { // Only save reservations with non-empty customer name
            file << reservation.customerName << ","
                 << reservation.movieTitle << ","
                 << reservation.date << ","
                 << reservation.round << ","
                 << reservation.number << "\n";
        }
    }
    file.close();
}

void loadMoviesData(std::vector<Movie> &movies, const std::string &filename)
{
    std::ifstream file(filename);
    if (!file.is_open())
    {
        std::cerr << "Error opening file for reading. Starting with a default setup." << std::endl;
        return;
    }

    std::string line;
    while (getline(file, line))
    {
        std::istringstream iss(line);
        std::string token;
        getline(iss, token, ',');
        std::string title = token;
        getline(iss, token, ',');
        int date = std::stoi(token);

        std::vector<std::vector<int>> availableSeats;
        std::vector<int> seatsPerDay;
        while (getline(iss, token, ','))
        {
            seatsPerDay.push_back(std::stoi(token));
            if (seatsPerDay.size() == 4)
            { // Assuming 4 rounds per day as per initial setup
                availableSeats.push_back(seatsPerDay);
                seatsPerDay.clear();
            }
        }
        movies.push_back(Movie{title, date, availableSeats});
    }
    file.close();
}

void loadReservationsData(std::vector<Reservation> &reservations, const std::string &filename)
{
    std::ifstream file(filename);
    if (!file.is_open())
    {
        std::cerr << "Error opening file for reading." << std::endl;
        return;
    }

    std::string line;
    while (getline(file, line))
    {
        std::istringstream iss(line);
        std::string customerName, movieTitle;
        int date, round, number;

        getline(iss, customerName, ',');
        getline(iss, movieTitle, ',');
        iss >> date >> round >> number;

        reservations.push_back(Reservation{customerName, movieTitle, date, round, number});
    }
    file.close();
}

int main()
{
    bool isRunning = true;
    std::vector<Reservation> reserved;
    std::vector<Movie> movies;

    loadMoviesData(movies, "movies.txt");
    loadReservationsData(reserved, "reservations.txt");

    if (movies.empty())
    {
        movies = {
            Movie{"Poor Things", 3, {{10, 10, 10, 10}, {10, 10, 10, 10}, {10, 10, 10, 10}}},
            Movie{"เหมรย", 3, {{10, 10, 10, 10}, {10, 10, 10, 10}, {10, 10, 10, 10}}},
            Movie{"4KingsII", 3, {{10, 10, 10, 10}, {10, 10, 10, 10}, {10, 10, 10, 10}}}};
    }

    while (isRunning)
    {
        std::cout << "1. View Schedule" << std::endl;
        std::cout << "2. Make Reservation" << std::endl;
        std::cout << "3. Cancel Reservation" << std::endl;
        std::cout << "4. Exit" << std::endl;
        std::cout << "5. Save Data" << std::endl;

        int choice;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice)
        {
        case 1:
            displaySchedule(movies);
            break;
        case 2:
            makeReservation(movies, reserved);
            break;
        case 3:
            cancelReservation(movies, reserved);
            break;
        case 4:
            isRunning = false;
            break;
        case 5:
            saveMoviesData(movies, "movies.txt");
            saveReservationsData(reserved, "reservations.txt");
            std::cout << "Data saved." << std::endl;
            break;
        default:
            std::cout << "Invalid choice. Please enter a valid option." << std::endl;
        }
    }
    std::cout << "Exiting program. Data saved." << std::endl;

    return 0;
}