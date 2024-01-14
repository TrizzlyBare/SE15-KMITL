name = input("Enter your first name: ")
surname = input("Enter your last name: ")
gender = input("Enter your gender (m/f): ")

print("Your username: "+ gender.upper() + surname[0].upper() + name[:6].upper())