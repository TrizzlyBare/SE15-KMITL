import turtle as t
from abc import ABC, abstractmethod

class TwoDshape:
    def __init__(self, x, y,):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y
    
    @abstractmethod
    def draw(self):
        pass

class Line(TwoDshape):
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.length = length
    
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.forward(self.length)
        t.penup()

class Rectangle(TwoDshape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.left(90)
        t.forward(self.width)
        t.left(90)
        t.forward(self.height)
        t.penup()

class Circle(TwoDshape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(self.radius)
        t.penup()

class Square(TwoDshape):
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.length = length
    
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.forward(self.length)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.length)
        t.left(90)
        t.forward(self.length)
        t.penup()

Line(0, 0, 100).draw()
Rectangle(50, 50, 100, 50).draw()
Circle(-50, -50, 50).draw()
Square(0, 0, 100).draw()

t.done()
