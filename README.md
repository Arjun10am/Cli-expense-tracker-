# Cli-expense-tracker-

# CLI Expense Tracker

A simple and modular **Command-Line Expense Tracker** built with Python.  
This project helps users track daily expenses, store them persistently, and view summaries — all from the terminal.

---

## 📌 Features

- Add expenses with amount, category, and description
- View all recorded expenses
- Calculate total spending
- Persistent storage using JSON
- Clean, modular project structure
- Beginner-friendly and extensible

---

## 🗂 Project Structure

cli-expense-tracker/
├── expense_tracker/
│ ├── init.py
│ ├── main.py # Entry point (CLI menu)
│ ├── expense.py # Expense model
│ ├── storage.py # JSON storage handling
│ └── utils.py # Helper utilities
├── data/
│ └── expenses.json # Expense data (ignored in git)
├── README.md
├── .gitignore
└── venv/ # Virtual environment (Ignored)

---

## ⚙️ Requirements

- Python **3.7+**
- No external dependencies (standard library only)

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Arjun10am/Cli-expense-tracker-.git
cd cli-expense-tracker


Create & activate a virtual environment (recommended)

Windows (PowerShell)

python -m venv venv
.\venv\Scripts\Activate.ps1


Mac / Linux

python3 -m venv venv
source venv/bin/activate

Run the application
python -m expense_tracker.main

🖥 Usage

When the program starts, you’ll see:

Expense Tracker
1. Add Expense
2. View Expenses
3. Total Expenses
4. Exit

➕ Add an Expense

Enter amount

Enter category

Enter description

📋 View Expenses

Lists all saved expenses

💰 Total Expenses

Displays total amount spent

🧠 Design Decisions

Modular architecture for readability and maintainability

Absolute paths for reliable file handling

JSON storage for simplicity and portability

No frameworks to keep the project beginner-friendly

Data Handling

Expense data is stored in data/expenses.json

This file is excluded from version control using .gitignore

🛠 Future Improvements

Category-wise totals

Date-based filtering

CSV export

Unit tests

Argument-based CLI (expense add, expense list)

Packaging as an installable CLI tool


⭐ If you found this project helpful, feel free to star the repository!


```
