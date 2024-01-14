class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    
    def getdiscriminant(self):
        return self.__b**2 - 4*self.__a*self.__c
    
    def getroot1(self):
        if self.getdiscriminant() >= 0:
            return (-self.__b + self.getdiscriminant()**0.5) / (2*self.__a)
        else:
            return 0
    
    def getroot2(self):
        if self.getdiscriminant() >= 0:
            return (-self.__b - self.getdiscriminant()**0.5) / (2*self.__a)
        else:
            return 0

equation = QuadraticEquation(1, 2, 3)

if equation.getdiscriminant() > 0:
    print("Discriminant:", equation.getdiscriminant())
else :
    print("0")