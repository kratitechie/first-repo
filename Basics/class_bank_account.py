class bank:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance

    def deposit(self, amount):
        #self.amount=amount
        self.balance= amount+self.balance
        print (f"Your new balance after deposit of Rs {amount} is {self.balance}")

    def show_balance(self):
        print (f"Your current balance is Rs {self.balance}")    

b1=bank(input("Account Holder Name please enter:\n"), int(input("Initial Balance pleasse enter:\n")))
b1.show_balance()

amt=int(input("Enter amount to be deposited:\n"))
b1.deposit(amt)
b1.show_balance()
