import turtle as t 

class Char:
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

    #draw the character using turtle at position(x,y)
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.write(self.char, align="center")

    #returns get width of the character drawn by method draw(x,y)
    def getWidth(self):
        return 10
    
class Char0(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "0")

    #draw the character 0 using turtle at position(x,y)
    def draw(self):
        super().draw()
        t.circle(10)
    
    #returns get width of the image of character 0 drawn by method draw(x,y)
    def getWidth(self):
        return 20

class Char1(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "1")

    #draw the character 1 using turtle at position(x,y)
    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x, self.y - 10)
        t.pendown()
        t.goto(self.x, self.y + 10)
    
    #returns get width of the image of character 1 drawn by method draw(x,y)
    def getWidth(self):
        return 10

class Char2(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "2")

    #draw the character 2 using turtle at position(x,y)
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
    
    #returns get width of the image of character 2 drawn by method draw(x,y)
    def getWidth(self):
        return 20
    
class Char3(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "3")

    #draw the character 3 using turtle at position(x,y)
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
    
    #returns get width of the image of character 3 drawn by method draw(x,y)
    def getWidth(self):
        return 20
    
class Char4(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "4")

    #draw the character 4 using turtle at position(x,y)
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
    
    #returns get width of the image of character 4 drawn by method draw(x,y)
    def getWidth(self):
        return 20
    
class Char5(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "5")

    #draw the character 5 using turtle at position(x,y)
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
    
    #returns get width of the image of character 5 drawn by method draw(x,y)
    def getWidth(self):
        return 20

class Char6(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "6")

    #draw the character 6 using turtle at position(x,y)
    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x - 10, self.y + 10)
        t.pendown()
        t.goto(self.x - 10, self.y - 10)
        t.goto(self.x + 10, self.y - 10)
        t.goto(self.x + 10, self.y)
        t.goto(self.x - 10, self.y)
    
    #returns get width of the image of character 6 drawn by method draw(x,y)
    def getWidth(self):
        return 20
    
class Char7(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "7")

    #draw the character 7 using turtle at position(x,y)
    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x - 10, self.y + 10)
        t.pendown()
        t.goto(self.x + 10, self.y + 10)
        t.goto(self.x + 10, self.y - 10)
    
    #returns get width of the image of character 7 drawn by method draw(x,y)
    def getWidth(self):
        return 20
    
class Char8(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "8")

    #draw the character 8 using turtle at position(x,y)
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
    
    #returns get width of the image of character 8 drawn by method draw(x,y)
    def getWidth(self):
        return 20
    
class Char9(Char):
    def __init__(self, x, y):
        super().__init__(x, y, "9")

    #draw the character 9 using turtle at position(x,y)
    def draw(self):
        super().draw()
        t.penup()
        t.goto(self.x + 10, self.y + 10)
        t.pendown()
        t.goto(self.x + 10, self.y - 10)
        t.goto(self.x - 10, self.y - 10)
        t.goto(self.x - 10, self.y)
        t.goto(self.x + 10, self.y)
    
    #returns get width of the image of character 9 drawn by method draw(x,y)
    def getWidth(self):
        return 20
    
#define a method drawNum(x) where x is either a natural number or a string of digits 0, ..., 9. drawsNum(x) will draw x using turtle.
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