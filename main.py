import sqlite3
import matplotlib.pyplot as plt
connection = sqlite3.connect("finance.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL
)
""")


def add_transaction():
    date = input("Date (YYYY-MM-DD): ")
    description = input("Description: ")
    category = input("Category: ")
    amount = float(input("Amount: "))

    cursor.execute("""
    INSERT INTO transactions (date, description, category, amount)
    VALUES (?, ?, ?, ?)
    """, (date, description, category, amount))

    connection.commit()

    print("Transaction added successfully!")


def view_transactions():
    cursor.execute("SELECT * FROM transactions")

    transactions = cursor.fetchall()

    print("\n--- Transactions ---")

    for transaction in transactions:
        print(
            f"ID: {transaction[0]} | "
            f"Date: {transaction[1]} | "
            f"Description: {transaction[2]} | "
            f"Category: {transaction[3]} | "
            f"Amount: €{transaction[4]:.2f}"
        )


def analyze_expenses():
    cursor.execute("SELECT SUM(amount) FROM transactions")

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print("\n--- Expense Analysis ---")
    print(f"Total expenses: €{total:.2f}")

    if total == 0:
        print("No expenses to analyze.")
        return

    cursor.execute("""
    SELECT category, SUM(amount)
    FROM transactions
    GROUP BY category
    ORDER BY SUM(amount) DESC
    """)

    category_expenses = cursor.fetchall()

    print("\nExpenses by category:")

    categories = []
    amounts = []

    for category, amount in category_expenses:
        percentage = (amount / total) * 100

        print(f"{category}: €{amount:.2f} ({percentage:.1f}%)")

        categories.append(category)
        amounts.append(amount)

    plt.figure(figsize=(8, 5))

    plt.bar(categories, amounts)

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (€)")

    plt.tight_layout()
    plt.show()
    cursor.execute("""
        SELECT date, SUM(amount)
        FROM transactions
        GROUP BY date
        ORDER BY date
        """)

    daily_expenses = cursor.fetchall()

    dates = []
    daily_amounts = []

    for date, amount in daily_expenses:
        dates.append(date)
        daily_amounts.append(amount)

    plt.figure(figsize=(8, 5))

    plt.plot(dates, daily_amounts, marker="o")

    plt.title("Daily Expenses")
    plt.xlabel("Date")
    plt.ylabel("Amount (€)")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def main_menu():
    while True:
        print("\n--- Finance Tracker ---")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Exit")
        print("4. Analyze expenses")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            print("Goodbye!")
            break

        elif choice == "4":
            analyze_expenses()

        else:
            print("Invalid choice. Please try again.")



main_menu()

connection.close()
