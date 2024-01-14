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
