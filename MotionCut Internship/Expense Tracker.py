# expense.py
class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount


# storage.py
import csv

def load_expenses(filename="expenses.csv"):
    expenses = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                expenses.append(Expense(row[0], row[1], row[2], float(row[3])))
    except FileNotFoundError:
        pass  # Ignore if file doesn't exist
    return expenses


def save_expenses(expenses, filename="expenses.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Description", "Amount"])  # Header row
        for expense in expenses:
            writer.writerow([expense.date, expense.category, expense.description, expense.amount])


# main.py
def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (DD-MM-YYYY): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            while True:
                try:
                    amount = float(input("Enter amount: "))
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")

            new_expense = Expense(date, category, description, amount)
            expenses.append(new_expense)
            save_expenses(expenses)
            print("Expense added successfully!")

        elif choice == "2":
            if not expenses:
                print("No expenses found.")
            else:
                print("{:<15}{:<20}{:<20}{:>10}".format("Date", "Category", "Description", "Amount"))
                for expense in expenses:
                    print(
                        "{:<15}{:<20}{:<20}{:>10.2f}".format(
                            expense.date, expense.category, expense.description, expense.amount
                        )
                    )

        elif choice == "3":
            # Implement monthly summary functionality (using libraries like pandas)
            print("Monthly summary functionality not yet implemented.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
