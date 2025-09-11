#payment problem
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class cash(Payment):
    def __init__(self,amount):
        self.amount=amount
    def pay(self,amount):
        print("Paid",self.amount,"in cash")
class credeb(Payment):
    def __init__(self,amount):
        self.amount=amount
    def pay(self,amount):
        print("Paid",self.amount,"in credit/debit card")
class UPI(Payment):
    def __init__(self,amount):
        self.amount=amount
    def pay(self,amount):
        print("Paid",self.amount,"in UPI")
payments = [cash(1000), credeb(1000), UPI(1000)]
 
for p in payments:
    p.pay(1000)
    
        