#A bounding rectangle is the minimum rectangle that encloses a set of points in a two-dimensional place. Write a method that returns a bounding rectangle for a set of points in a two dimentional plane, as follows
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
