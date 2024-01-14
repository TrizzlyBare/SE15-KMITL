num = 0

for i in range(50):
    if i % 3 == 0:
        continue
    if i == 49:
        print(i)
        break
    print(i, ",", end="")
