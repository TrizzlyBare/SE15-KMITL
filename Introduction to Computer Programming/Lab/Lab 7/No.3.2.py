import turtle as t

class Circle:
    def __init__(self, x, y,radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def getArea(self):
        return self.radius**2 * 3.14
    
    def getPerimeter(self):
        return self.radius * 2 * 3.14
    
    def move(self, dx, dy):
        self.x = dx
        self.y = dy

    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.circle(self.radius)
        t.penup()
    
C1 = Circle(0, 0, 50)
C1.draw()

print("The circle area is:", C1.getArea())
print("The circle perimeter is:", C1.getPerimeter())

t.done()