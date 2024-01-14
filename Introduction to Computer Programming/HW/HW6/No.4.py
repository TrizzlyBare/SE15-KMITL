money = int(input("Input your amount of money: "))
moneytypes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]

for moneytype in moneytypes:
    if money >= moneytype:
        num = money // moneytype
        if money >= 20:
            print(str(moneytype) + "-Baht notes: " + str(num))
            money = money - num * moneytype
        else:
            print(str(moneytype) + "-Baht coins: " + str(num))
            money = money - num * moneytype
    