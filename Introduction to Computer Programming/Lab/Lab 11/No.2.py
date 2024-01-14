import math

class Calculator:
    def __init__(self, acc=0):
        self.acc = acc

    def set_accumulator(self, a):
        self.acc = a

    def get_accumulator(self):
        return self.acc
    
    def add(self, num):
        self.acc += num

    def subtract(self, num):
        self.acc -= num

    def multiply(self, num):
        self.acc *= num

    def divide(self, num):
        self.acc /= num

    def print_result(self):
        print(f"Result: {self.acc:e}")

class Sci_calc(Calculator):
    def __init__(self, acc=0):
        super().__init__(acc)

    def square(self):
        self.acc = self.acc ** 0.5

    def exp(self, num):
        self.acc **= num
    
    def factorial(self):
        self.acc = math.factorial(self.acc)

    def print_result(self):
        print(f"Result: {self.acc:e}")


calculator = Calculator()
calculator.add(5)
calculator.multiply(2)
calculator.multiply(2)
calculator.print_result()

sci_calc = Sci_calc()  
sci_calc.add(5)
sci_calc.multiply(2)
sci_calc.exp(2)
sci_calc.print_result()
