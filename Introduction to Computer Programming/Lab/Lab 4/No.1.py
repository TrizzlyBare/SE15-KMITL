score = float(input("Enter a score:"))

if 80 <= score <= 100 :
    print("Your grade : A")
elif 70 <= score < 80 :
    print("Your grade : B")
elif 60 <= score < 70 :
    print("Your grade : C")
elif 50 <= score < 60 :
    print ("Your grade : D")
elif 0 <= score < 50 :
    print ("Your grade : F ")
else :
    print ("Invalid")