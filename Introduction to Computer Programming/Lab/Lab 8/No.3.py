string1 = input("Enter a short string: ")
string2 = input("Enter a long string: ")

for i in range(len(string2)):
    if string2[i:i+len(string1)] == string1:
        print("The short string is found in the long string")
        break
    
    else:
        print("The short string is not found in the long string")
        break