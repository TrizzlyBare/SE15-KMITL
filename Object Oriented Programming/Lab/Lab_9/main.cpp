#include <iostream>
#include <vector>
#include "Album.h"

int main()
{
    std::vector<Album> albums;
    albums.emplace_back("Abbey Road", "The Beatles", 19.99, 5);
    albums.emplace_back("The Dark Side of the Moon", "Pink Floyd", 21.99, 3);
    albums.emplace_back("Hotel California", "Eagles", 15.99, 4);
    albums.emplace_back("Back in Black", "AC/DC", 20.99, 2);
    albums.emplace_back("Rumours", "Fleetwood Mac", 16.99, 3);
    albums.emplace_back("Thriller", "Michael Jackson", 18.99, 5);
    albums.emplace_back("The Wall", "Pink Floyd", 22.99, 2);
    albums.emplace_back("Led Zeppelin IV", "Led Zeppelin", 17.99, 3);

    while (true)
    {
        std::cout << std::endl;
        std::cout << "Online Music Store" << std::endl;
        std::cout << "1. List all albums" << std::endl;
        std::cout << "2. Purchase an album" << std::endl;
        std::cout << "3. Display sales statistics" << std::endl;
        std::cout << "4. Exit" << std::endl;
        std::cout << "Enter your choice: ";

        int choice;
        std::cin >> choice;

        if (std::cin.fail() || choice < 1 || choice > 4)
        {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid choice. Please try again." << std::endl;
        }
        else
        {
            std::cin.ignore();

            if (choice == 1)
            {
                int i = 1;
                for (auto &album : albums)
                {
                    std::cout << i << ". " << album.getTitle() << " by " << album.getArtist() << " - $" << album.getPrice() << "( " << album.getCopiesAvailable() << " copies available)" << std::endl;
                    i++;
                }
            }
            else if (choice == 2)
            {
                std::cout << "Enter the title of the album you want to purchase: ";
                std::string title;
                getline(std::cin, title);

                for (auto &album : albums)
                {
                    if (album.getTitle() == title)
                    {
                        album.purchaseAlbum();
                        std::cout << "You have purchased " << album.getTitle() << " by " << album.getArtist() << "." << std::endl;
                        break;
                    }
                    else if (&album == &albums.back())
                    {
                        std::cout << "Album not found." << std::endl;
                    }
                }
            }
            else if (choice == 3)
            {
                std::cout << "Total albums: " << Album::getTotalAlbums() << std::endl;
                std::cout << "Total revenue: " << Album::getTotalSales() << std::endl;
            }
            else if (choice == 4)
            {
                return 0;
            }
            else
            {
                std::cout << "Invalid choice." << std::endl;
            }
        }
    }
}
