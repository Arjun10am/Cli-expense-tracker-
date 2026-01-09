from expense_tracker.expense import Expense
from expense_tracker.storage import load_expenses, save_expenses
from expense_tracker.utils import get_float_input, print_expense


def add_expense():
    amount = get_float_input("Enter amount: ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = Expense(amount, category, description)

    expenses = load_expenses()
    expenses.append(expense.to_dict())
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print_expense(expense)


def total_expenses():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spent: ₹{total}")


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
