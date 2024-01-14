class BankAccount:
    def __init__(self, Bankname, Name, AccountNumber, Balance):
        self.Bankname = Bankname
        self.Name = Name
        self.AccountNumber = AccountNumber
        self.Balance = Balance
    
    def print(self):
        print(f"Bankname: {self.Bankname}\nName: {self.Name}\nAccountNumber: {self.AccountNumber}\nBalance: {self.Balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.Balance += amount
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        if amount <= self.Balance and amount > 0:
            self.Balance -= amount
        else:
            print("Not enough money")
    
    def getBalance(self):
        return self.Balance

account1 = BankAccount("K", "K", "123456789", 1000)
account1.withdraw(500)
account1.deposit(200)

account1.print()

print("Current Balance:", account1.getBalance())