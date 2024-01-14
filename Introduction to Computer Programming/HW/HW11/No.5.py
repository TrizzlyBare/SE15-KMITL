class StationaryGood:
    def __init__(self, magazine, book, ribbon, price):
        self.magazine = magazine
        self.book = book
        self.ribbon = ribbon
        self.price = price

    def cost(self):
        return self.magazine + self.book * 0.9 + self.ribbon * 5

class Magazine(StationaryGood):
    def __init__(self, magazine,price):
        self.magazine = magazine
        self.price = price

    def cost(self):
        return self.magazine * self.price

class Book(StationaryGood):
    def __init__(self, book, price):
        self.book = book
        self.price = price

    def cost(self):
        return self.book * 0.9 * self.price 
    
class Ribbon(StationaryGood):
    def __init__(self, ribbon):
        self.ribbon = ribbon

    def cost(self):
        return self.ribbon * 5 

def getTotalCost(basket):
    total = 0
    for item in basket:
        total += item.cost()
    return total

def main():
    basket = []
    while True:
        print("1. Magazine")
        print("2. Book")
        print("3. Ribbon")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            magazine = int(input("Enter number of magazines: "))
            price = int(input("Enter price of magazine: "))
            basket.append(Magazine(magazine, price))
        elif choice == 2:
            book = int(input("Enter number of books: "))
            price = int(input("Enter price of book: "))
            basket.append(Book(book, price))
        elif choice == 3:
            ribbon = int(input("Enter number of ribbons: "))
            basket.append(Ribbon(ribbon))
        elif choice == 4:
            break
        else:
            print("Invalid choice")
    print("Total cost of goods: ", getTotalCost(basket))

main()