from transaction import Transactions
class Budget:
   def __init__(self):
        self.transactions=[]
   def add_transactions(self,amount,category,transaction_type):
         transaction=Transactions(amount,category,transaction_type)
         self.transactions.append(transaction)
         print("Transaction added successfully") 
   def get_balance(self):
       income=sum(t.amount for t in self.transactions if t.transaction_type=="income")
       expense=sum(t.amount for t in self.transactions if t.transaction_type=="expense")
       return income-expense
   def show_transactions(self):
       if not self.transactions:
           print("No transactions made")
       else:
           for t in self.transactions:
               print(t)
# obj1=Budget()
# obj1.add_transactions(500,"rent","expense")
# obj1.add_transactions(1000,"work","income")
# balance=obj1.get_balance()
# obj1.show_transactions()
# print("current balance :",balance)

