import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def printInfo(self):
        return f"Position: {self.x}, {self.y}"

class Circle(Point):
    def __init__(self, x=0.0, y=0.0, radius=0.0): 
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
    def printinfo(self):
        return f"{super().printInfo()}; Radius: {self.radius:.2f}; Area: {self.area():.2f}"
    
point = Point(1, 2)
print(point.printInfo())

circle = Circle(1, 2, 3)
print(circle.printinfo())
