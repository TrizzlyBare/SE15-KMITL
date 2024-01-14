#No.1
class Clock:
    def __init__(self, hour, minute, second):
        self.set_time(hour, minute, second)

    def set_time(self, hour, minute, second):
        if self.valid_hour(hour) and self.valid_minute(minute) and self.valid_second(second):
            self.hour = hour
            self.minute = minute
            self.second = second
        else:
            print("Invalid time values provided.")

    def valid_hour(self, hour):
        return 0 <= hour < 24

    def valid_minute(self, minute):
        return 0 <= minute < 60

    def valid_second(self, second):
        return 0 <= second < 60
    
    def get_time(self):
        if self.hour > 12:
            return f"{self.hour - 12:02}:{self.minute:02}:{self.second:02} PM."
        elif self.hour == 12:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02} PM."
        elif self.hour == 0:
            return f"{self.hour + 12:02}:{self.minute:02}:{self.second:02} AM."
        else:
            return f"{self.hour:02}:{self.minute:02}:{self.second:02} AM."

    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.minute += 1
            self.second -= 60
            if self.minute >= 60:
                self.hour += 1
                self.minute -= 60
                if self.hour >= 24:
                    self.hour -= 24

my_clock = Clock(10, 30, 45)
print(my_clock.get_time()) 

my_clock.set_time(20, 15, 30)
print(my_clock.get_time()) 

my_clock.tick()
print(my_clock.get_time())  

#====================================================================================================

#No.2

class Poly:
    def __init__(self, args):
        self.p = args

    def add(self, other):
        if len(self.p) > len(other.p):
            for i in range(len(other.p)):
                self.p[i] += other.p[i]
            return self
        else:
            for i in range(len(self.p)):
                other.p[i] += self.p[i]
            return other
    
    def scalar_mul(self, scalar):
        for i in range(len(self.p)):
            self.p[i] *= scalar
        return self
    
    def multiply(self, other):
        result = [0] * (len(self.p) + len(other.p) - 1)
        for i in range(len(self.p)):
            for j in range(len(other.p)):
                result[i + j] += self.p[i] * other.p[j]
        return Poly(result)
    
    def diff(self):
        result = []
        for i in range(1, len(self.p)):
            result.append(self.p[i] * i)
        return Poly(result)
    
    def integrate(self):
        result = [0]
        for i in range(len(self.p)):
            result.append(self.p[i] / (i + 1))
        return Poly(result)
    
    def eval(self, x):
        result = 0
        for i in range(len(self.p)):
            result += self.p[i] * (x ** i)
        return result
    
    def print(self):
        output = ""
        for i in range(len(self.p)):
            if self.p[i] != 0:
                if i == 0:
                    if self.p[i] > 0 and self.p[i] != 0:
                        output += f"{self.p[i]} "
                    else:
                        output += f"- {abs(self.p[i])} "
                elif i == 1:
                    if self.p[i] > 0 and self.p[i] != 0:
                        output += f"{self.p[i]}x "
                    else:
                        output += f"- {abs(self.p[i])}x "
                elif i < len(self.p) - 1:
                    if self.p[i] > 0 and self.p[i] != 0:
                        output += f"+ {self.p[i]}x^{i} "
                    else:
                        output += f"- {abs(self.p[i])}x^{i} "
                else:
                    if self.p[i] > 0 and self.p[i] != 0:
                        output += f"+ {self.p[i]}x^{i} "
                    else:
                        output += f"- {abs(self.p[i])}x^{i} "

        print(output)

poly = Poly([3, 0, -2, 0, 5])
poly.print()

poly1 = Poly([3, 0, -2, 0, 5])
poly2 = Poly([1, 2, 3])

poly1.print()
poly2.print()

(poly1.add(poly2)).print()
(poly1.scalar_mul(2)).print()
(poly1.multiply(poly2)).print()
(poly1.diff()).print()
(poly1.integrate()).print()

print(poly1.eval(2))

#====================================================================================================

#No.3

class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f

    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e 
    
    def getF(self):
        return self.__f 
    
    def isSolvable(self):
        if (self.__a*self.__d-self.__b*self.__c) != 0:
            return True
        else:
            return False
        
    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)
    
    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
    
def main():
    a, b, c, d, e, f = eval(input("Enter a,b,c,d,e,f: "))

    linearEquation = LinearEquation(a, b, c, d, e, f)

    if linearEquation.isSolvable():
        x = linearEquation.getX()
        y = linearEquation.getY()
        return x, y
    else:
        return None

result = main()

if result:
    x, y = result
    print("x is", x, "and y is", y)
else:
    print("The equation has no solution.")

#====================================================================================================