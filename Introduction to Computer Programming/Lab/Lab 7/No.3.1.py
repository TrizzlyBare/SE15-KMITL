import turtle as t

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y  
        self.width = width
        self.height = height
        self.b = self.y + self.height
        self.r = self.x + self.width

    def getArea(self):
        return self.width * self.height
    
    def getPerimeter(self):
        return 2 * (self.width + self.height)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
   
    def intersect(self, other):
            a, b = self, other
            x1 = max(min(a.x, a.x+a.width), min(b.x, b.x+b.width))
            y1 = max(min(a.y, a.y-a.height), min(b.y, b.y-b.height))
            x2 = min(max(a.x, a.x+a.width), max(b.x, b.x+b.width))
            y2 = min(max(a.y, a.y-a.height), max(b.y, b.y-b.height))
            if x1<x2 and y1<y2:
                return Rectangle(x1, y2, abs(x1-x2), abs(y1-y2))
    
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        for _ in range(2):
            t.forward(self.width)
            t.rt(90)
            t.forward(self.height)
            t.rt(90)


A = Rectangle(0, 0, 100, 200)
B = Rectangle(-200, 0, 100, 100)

A.draw()
B.draw()

C = A.intersect(B)
try:
    C.draw()
except Exception as x:
    print(x)

D = Rectangle(-50, -50, 200, 50)
D.draw()
t.color("red")

E = A.intersect(D)
E.draw()

E.move(-100,100)
E.draw()

t.done()