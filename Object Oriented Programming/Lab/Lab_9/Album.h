#ifndef ALBUM_H
#define ALBUM_H
#include <string>

using namespace std;

class Album
{
public:
    Album(const string &title, const string &artist, double price, int copies);

    string getTitle() const;
    string getArtist() const;
    double getPrice() const;
    int getCopiesAvailable() const;

    static int getTotalAlbums();
    static double getTotalSales();

    void purchaseAlbum();

private:
    string title;
    string artist;
    double price;
    int copies;
    static int totalAlbums;
    static double totalSales;
};
#endif