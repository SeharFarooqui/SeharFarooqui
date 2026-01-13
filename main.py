import streamlit as st
from transaction import Transactions
from budget import Budget
def main():
    my_budget=Budget()
    while True:
     print("\nWelcome to Personal Budget Tracker ")
     print("1.Add Income")
     print("2.Add Expense ")
     print("3.View Balance")
     print("4.Show all transactions")
     print("5.Exit")
     select=input("Enter your choice from(1-5):  ")
     if select=="1":
        amount=float(input("Enter amount:  "))
        category=input("Enter category:  ")
        my_budget.add_transactions(amount,category,"income")
     elif select=="2":
        amount=float(input("Enter amount:  "))
        category=input("Enter category:  ")
        my_budget.add_transactions(amount,category,"expense")
     elif select=="3":
       balance= my_budget.get_balance()
       print(f"Your current balance is {balance}")
     elif select=="4":
        my_budget.show_transactions()
     elif select=="5":
        print("Thank you for using the budget tracker,I hope it helped you.")
        break
     else:
        print("Invalid choice !  Please Try again.")
if __name__=="__main__":
 main()

