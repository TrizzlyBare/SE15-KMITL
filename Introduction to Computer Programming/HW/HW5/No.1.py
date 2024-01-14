n = float(input("Please enter your number : "))

guess = n / 2.0
for _ in range(0, 5) :
    temp = n / guess 
    guess = (guess + temp) / 2.0
    approx_5_iter = round(guess, 3)

guess = n / 2.0
for _ in range(0, 6) :
    temp = n / guess
    guess = (guess + temp) / 2.0
    approx_6_iter = round(guess,3)

guess = n / 2.0
for _ in range(0, 7) :
    temp = n / guess
    guess = (guess + temp) / 2.0
    approx_7_iter = round(guess,3)

print ("5 iterations", approx_5_iter)
print ("6 iterations", approx_6_iter)
print ("7 iterations", approx_7_iter)

