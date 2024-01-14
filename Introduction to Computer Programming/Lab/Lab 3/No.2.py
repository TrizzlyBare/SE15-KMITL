x = str(input("Please enter your character : "))

y = ord(x)  

hex = format(y, "04x")

print("The unicode of",x, "is u"+hex)