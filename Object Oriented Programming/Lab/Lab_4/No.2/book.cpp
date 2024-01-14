#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Book
{
private:
    string title;
    string author;
    int quantity;

public:
    Book(string ti, string au, int quan)
    {
        title = ti;
        author = au;
        quantity = quan;
    }

    void setTitle(string ti)
    {
        title = ti;
    }

    void setAuthor(string au)
    {
        author = au;
    }

    void setQuantity(int quan)
    {
        quantity = quan;
    }

    string getTitle() const
    {
        return title;
    }

    string getAuthor() const
    {
        return author;
    }

    int getQuantity() const
    {
        return quantity;
    }
};

class Inventory
{
private:
    vector<Book> books;

public:
    void addBook(Book book)
    {
        books.push_back(book);
    }

    void removeBook(string title)
    {
        for (int i = 0; i < books.size(); i++)
        {
            if (books[i].getTitle() == title)
            {
                books.erase(books.begin() + i);
                return;
            }
        }
    }

    void findBook(string title)
    {
        for (int i = 0; i < books.size(); i++)
        {
            if (books[i].getTitle() == title)
            {
                cout << "Title: " << books[i].getTitle() << ", ";
                cout << "Author: " << books[i].getAuthor() << ", ";
                cout << "Quantity: " << books[i].getQuantity();
            }
        }

        cout << "Book not found!" << endl;
    }
    void printInventory()
    {
        for (int i = 0; i < books.size(); i++)
        {
            cout << "Title: " << books[i].getTitle() << ", ";
            cout << "Author: " << books[i].getAuthor() << ", ";
            cout << "Quantity: " << books[i].getQuantity();
            cout << endl;
        }
    }
};

int main()
{
    Inventory inventory;

    while (true)
    {
        cout << "Enter command (a: add, r: remove,  s: search, l: list, q: quit): ";

        char choice;
        cin >> choice;

        if (cin.fail())
        {
            cout << "Invalid input" << endl;
            return 0;
        }

        switch (choice)
        {
        case 'a':
        {
            string title, author;
            int quantity;

            cout << "Enter title: ";
            cin >> title;

            cout << "Enter author: ";
            cin >> author;

            cout << "Enter quantity: ";
            cin >> quantity;

            if (cin.fail() || cin.peek() != '\n')
            {
                cout << "Invalid input for quantity. Please enter a valid integer." << endl;
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                continue;
            }

            Book book(title, author, quantity);
            inventory.addBook(book);
            break;
        }

        case 'r':
        {
            string title;

            cout << "Enter title: ";
            cin >> title;

            if (cin.fail())
            {
                cout << "Invalid input" << endl;
                return 0;
            }

            inventory.removeBook(title);
            break;
        }

        case 's':
        {
            string title;

            cout << "Enter title: ";
            cin >> title;

            if (cin.fail())
            {
                cout << "Invalid input" << endl;
                return 0;
            }

            inventory.findBook(title);
            break;
        }

        case 'l':
            inventory.printInventory();
            break;

        case 'q':
            return 0;
            break;

        default:
            cout << "Invalid command. Please enter a valid command." << endl;
            break;
        }
    }
}