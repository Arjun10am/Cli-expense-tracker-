def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def print_expense(expense):
    print(
        f"Amount: ₹{expense['amount']} | "
        f"Category: {expense['category']} | "
        f"Description: {expense['description']}"
    )
