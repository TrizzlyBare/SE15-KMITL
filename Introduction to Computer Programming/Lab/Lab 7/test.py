import turtle as t

class Rectangle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.b = self.y + self.h
        self.r = self.x + self.w

    def getArea(self):
        return self.w * self.h

    def getPerimeter(self):
        return self.w*2 + self.h*2
    
    def move(self, nx, ny):
        self.x = nx
        self.y = ny

    def intersect(self, second_square):
        posX = max(self.x, second_square.x)
        posY = max(self.y, second_square.y)

        rec_overlap = Rectangle(posX, posY, min(self.r, second_square.r) - posX, min(self.b, second_square.b) - posY)
        if rec_overlap.w > 0 and rec_overlap.h > 0:
            return rec_overlap
        else:
            return Rectangle(0, 0, 0, 0)

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        for _ in range(2):
            t.right(90)
            t.forward(self.h)
            t.right(90)
            t.forward(self.w)

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