#include "Album.h"
#include <iostream>
#include <string>

int Album::totalAlbums = 0;
double Album::totalSales = 0;

Album::Album(const std::string &title, const std::string &artist, double price, int copies)
    : title(title), artist(artist), price(price), copies(copies)
{
    totalAlbums += copies;
}

void Album::purchaseAlbum()
{
    if (copies > 0)
    {
        copies--;
        totalAlbums--;
        totalSales += price;
    }
    else
    {
        std::cout << "Album not available." << std::endl;
    }
}

int Album::getTotalAlbums()
{
    return totalAlbums;
}

double Album::getTotalSales()
{
    return totalSales;
}

double Album::getPrice() const
{
    return price;
}

std::string Album::getTitle() const
{
    return title;
}

std::string Album::getArtist() const
{
    return artist;
}

int Album::getCopiesAvailable() const
{
    return copies;
}