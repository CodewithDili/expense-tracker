import csv
import os
from datetime import datetime
def add_expense(expense_file):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")
    amount = input("Enter the amount: ")
    description = input("Enter a description: ")

    with open(expense_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
        print("Expense added successfully!")
def view_expenses(expense_file):
    if not os.path.exists(expense_file):
        print("No expenses found.")
        return

    with open(expense_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")
def calculate_total(expense_file):
    if not os.path.exists(expense_file):
        print("No expenses found.")
        return

    total = 0
    with open(expense_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            total += float(row[2])

    print(f"Total spending: {total}")
def main():
    expense_file = 'expenses.csv'

    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Spending")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expense_file)
        elif choice == '2':
            view_expenses(expense_file)
        elif choice == '3':
            calculate_total(expense_file)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
