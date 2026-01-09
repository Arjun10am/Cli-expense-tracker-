import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "expenses.json")


def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
