#Define recursive function to calculate a greatest common divisor(gcd) of two numbers, x and y, by using this Euclid definition of gcd: gcd(x,0) = x and gcd(x,y) = gcd(y, x mod y)

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
print(gcd(12, 8))