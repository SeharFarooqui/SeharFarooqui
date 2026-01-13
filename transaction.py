from datetime import datetime
class Transactions :
    def __init__ (self,amount,category,transaction_type):
        self.amount=amount
        self.category=category
        self.transaction_type=transaction_type
        self.date=datetime.now().strftime("%Y-%m-%d")
    def __str__(self):
     return f"{self.date} {self.transaction_type.capitalize()} {self.category.capitalize()} {self.amount}"

# obj1=Transactions(300,"food","expense")
# print(obj1)

   