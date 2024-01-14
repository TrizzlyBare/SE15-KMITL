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
