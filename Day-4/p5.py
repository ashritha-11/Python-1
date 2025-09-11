#Bank Account problem
class BankAccount():
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Amount deposited:", amount)
        print("Updated Balance:", self.__balance)
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
            print("Updated Balance:", self.__balance)
    def get_balance(self):
        print("Current Balance:", self.__balance)
a = BankAccount(5000)   
a.deposit(10000)
a.withdraw(2000)
a.get_balance()
