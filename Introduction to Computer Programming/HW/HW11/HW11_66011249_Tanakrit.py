#No.1

class Clock:
    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss
    
    def run(self):
        self.ss += 1
        if self.ss == 60:
            self.ss = 0
            self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
                if self.hh == 24:
                    self.hh = 0
        print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")

    def setTime(self, h, m, s):
        self.hh = int(h)
        self.mm = int(m)
        self.ss = int(s)

class AlarmClock(Clock):
    def __init__(self, hh, mm, ss):
        super().__init__(hh, mm, ss)
        self.alarm_hh = int(hh)
        self.alarm_mm = int(mm)
        self.alarm_ss = int(ss)
        self.alarm_on = False 

    def setAlarmTime(self, h, m, s):
        self.alarm_hh = int(h)
        self.alarm_mm = int(m)
        self.alarm_ss = int(s)

    def alarm_on(self): 
        self.alarm_on = True

    def alarm_off(self):  
        self.alarm_on = False

    def run(self):
        while True:
            self.ss += 1
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
                if self.mm == 60:
                    self.mm = 0
                    self.hh += 1
                    if self.hh == 24:
                        self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")

            if (
                self.hh == self.alarm_hh
                and self.mm == self.alarm_mm
                and self.ss == self.alarm_ss
                and self.alarm_on
            ):
                print("ALARM")
                break 

#====================================================================================================

#No.2

import turtle as t

def RobotBattle():
    robotList = []

    while True:
        t.clear()
        for robot in robotList:
            robot.draw()

        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, " : ")
            robot.display_status()
            i += 1
        print("===============")

        choice = input("Enter which robot to order, 'c' to create a new robot, 'q' to quit: ")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robot to create: ")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList.append(newRobot)
        else:
            n = int(choice)
            robotList[n].command(robotList)

        robotList = [robot for robot in robotList if robot.health > 0]

class Robot(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100

    def move(self, x, y):
        if self.energy > 0:
            self.x = x
            self.y = y
            self.energy -= 10

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(15)
        t.penup()
        t.goto(self.x, self.y - 20)
        t.pendown()
        t.write(f"{self.health}, {self.energy}", align="center")

    def display_status(self):
        print("x=", self.x, "y=", self.y, "health", self.health, "energy", self.energy)

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()

    def heal(self, r):
        if self.energy >= 20 and abs(self.x - r.x) <= 10 and abs(self.y - r.y) <= 10:
            self.energy -= 20
            r.health += 10

    def command(self, robotList):
        print("Possible actions: move or heal")
        cm = input("Please input the command move(m) or heal(h): ")
        if cm == "m":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        elif cm == "h":
            rob = int(input("Which robot you want to heal (enter the index): "))
            if 0 <= rob < len(robotList):
                self.heal(robotList[rob])

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def strike(self, r):
        if self.energy >= 20 and self.missile > 0 and abs(self.x - r.x) <= 10 and abs(self.y - r.y) <= 10:
            self.energy -= 20
            self.missile -= 1
            r.health -= 50

    def display_status(self):
        print("x=", self.x, "y=", self.y, "health", self.health, "energy", self.energy, "missile", self.missile)

    def command(self, robotList):
        print("Possible actions: move or attack")
        cm = input("Please input the command move(m) or attack(s): ")
        if cm == "m":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        elif cm == "s":
            rob = int(input("Which robot you want to attack (enter the index): "))
            if 0 <= rob < len(robotList):
                self.strike(robotList[rob])

RobotBattle()

#====================================================================================================

#No.3

import turtle as t

class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.dot(5)
    
    def position(self):
        return (self.x, self.y)
    
class Rectangle2D(Point):
    def __init__(self, maxx, maxy, minx, miny):
        super().__init__((maxx + minx) / 2, (maxy + miny) / 2)
        self.maxx = maxx
        self.maxy = maxy
        self.minx = minx
        self.miny = miny
    
    def draw(self):
        t.penup()
        t.goto(self.minx, self.miny)
        t.pendown()
        t.goto(self.maxx, self.miny)
        t.goto(self.maxx, self.maxy)
        t.goto(self.minx, self.maxy)
        t.goto(self.minx, self.miny)
        super().draw()

    def width(self):
        return self.maxx - self.minx
    
    def height(self):
        return self.maxy - self.miny
    
def rectangle(points):
    x = []
    y = []

    for point in points:
        x.append(point.x)
        y.append(point.y)

    maxx = max(x)
    maxy = max(y)
    minx = min(x)
    miny = min(y)

    return Rectangle2D(maxx, maxy, minx, miny)

def main():
    points = []
    while True:
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        if x == 0 and y == 0:
            break
        points.append(Point(x, y))
    
    rectangle(points).draw()
    t.done()    

main()

#====================================================================================================

#No.4

import turtle as t 

class Char:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.write(self.char, align="center")

    def getWidth(self):
        return 10
    
class Char0(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "0")

    def draw(self):
        super().draw()
        t.circle(10)

    def getWidth(self):
        return 20

class Char1(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "1")

    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x, self.y - 10)
        t.pendown()
        t.goto(self.x, self.y + 10)

    def getWidth(self):
        return 10

class Char2(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "2")

    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x - 10, self.y + 10)
        t.pendown()
        t.goto(self.x + 10, self.y + 10)
        t.goto(self.x + 10, self.y)
        t.goto(self.x - 10, self.y)
        t.goto(self.x - 10, self.y - 10)
        t.goto(self.x + 10, self.y - 10)

    def getWidth(self):
        return 20
    
class Char3(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "3")

    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x - 10, self.y + 10)
        t.pendown()
        t.goto(self.x + 10, self.y + 10)
        t.goto(self.x + 10, self.y)
        t.goto(self.x - 10, self.y)
        t.penup()
        t.goto(self.x + 10, self.y)
        t.pendown()
        t.goto(self.x + 10, self.y - 10)
        t.goto(self.x - 10, self.y - 10)

    def getWidth(self):
        return 20
    
class Char4(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "4")

    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x + 10, self.y + 10)
        t.pendown()
        t.goto(self.x + 10, self.y)
        t.goto(self.x - 10, self.y)
        t.penup()
        t.goto(self.x, self.y + 10)
        t.pendown()
        t.goto(self.x, self.y - 10)

    def getWidth(self):
        return 20
    
class Char5(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "5")

    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x + 10, self.y + 10)
        t.pendown()
        t.goto(self.x - 10, self.y + 10)
        t.goto(self.x - 10, self.y)
        t.goto(self.x + 10, self.y)
        t.goto(self.x + 10, self.y - 10)
        t.goto(self.x - 10, self.y - 10)

    def getWidth(self):
        return 20

class Char6(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "6")

    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x - 10, self.y + 10)
        t.pendown()
        t.goto(self.x - 10, self.y - 10)
        t.goto(self.x + 10, self.y - 10)
        t.goto(self.x + 10, self.y)
        t.goto(self.x - 10, self.y)

    def getWidth(self):
        return 20
    
class Char7(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "7")

    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x - 10, self.y + 10)
        t.pendown()
        t.goto(self.x + 10, self.y + 10)
        t.goto(self.x + 10, self.y - 10)

    def getWidth(self):
        return 20
    
class Char8(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "8")

    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x - 10, self.y + 10)
        t.pendown()
        t.goto(self.x + 10, self.y + 10)
        t.goto(self.x + 10, self.y - 10)
        t.goto(self.x - 10, self.y - 10)
        t.goto(self.x - 10, self.y + 10)
        t.penup()
        t.goto(self.x - 10, self.y)
        t.pendown()
        t.goto(self.x + 10, self.y)
    
    def getWidth(self):
        return 20
    
class Char9(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "9")

    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x + 10, self.y + 10)
        t.pendown()
        t.goto(self.x + 10, self.y - 10)
        t.goto(self.x - 10, self.y - 10)
        t.goto(self.x - 10, self.y)
        t.goto(self.x + 10, self.y)
    
    def getWidth(self):
        return 20
    
def drawNum(x):
    x = str(x)
    x = list(x)
    x = [int(i) for i in x]
    x = [Char0(0,0), Char1(0,0), Char2(0,0), Char3(0,0), Char4(0,0), Char5(0,0), Char6(0,0), Char7(0,0), Char8(0,0), Char9(0,0)]
    for i in range(len(x)):
        x[i].draw()
        t.penup()
        t.goto(x[i].getWidth(), 0)
        t.pendown()
    
def main():
    drawNum(1234567890)
    t.done()

main()

#====================================================================================================

#No.5

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

#====================================================================================================