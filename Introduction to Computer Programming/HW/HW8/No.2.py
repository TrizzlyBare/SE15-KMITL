string = input("Enter some text: ")
count = {}

for i in string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

length = len(string)

print("-- Character Frequency Table --")
print("char percentage (character count / string length)")
for char, char_count in count.items():
    percentage = (char_count / length) * 100
    print(f"{char}: {char_count} occurrences, {percentage:.2f}%")
