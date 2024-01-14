s1 = str(input("Enter some text: "))
s2 = str(input("Enter some text: "))
i1 = int(input("Enter some number: "))
i2 = int(input("Enter some number: "))

if i1 % 2 == 0  or i1 % 3 == 0:
    print((s1+' ')*(i2-1) + s1+s2)
