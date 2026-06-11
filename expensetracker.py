import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"


# Create CSV if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE_NAME, index=False)


def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    new_data = pd.DataFrame([[date, category, amount]],
                            columns=["Date", "Category", "Amount"])

    new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)

    print("Expense Added Successfully")


def view_expenses():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No Expenses Found")
    else:
        print(df)


def total_expense():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No Data Available")
        return

    print("\nTotal Expense =", df["Amount"].sum())


def category_summary():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No Data Available")
        return

    print("\nExpense by Category:")
    print(df.groupby("Category")["Amount"].sum())


def expense_chart():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No Data Available")
        return

    category_data = df.groupby("Category")["Amount"].sum()

    category_data.plot(kind="bar")

    plt.title("Expense By Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()


def ml_prediction():
    df = pd.read_csv(FILE_NAME)

    if len(df) < 5:
        print("Add at least 5 expenses for ML prediction.")
        return

    X = [[i] for i in range(len(df))]
    y = df["Amount"]

    model = LinearRegression()
    model.fit(X, y)

    next_expense = model.predict([[len(df)]])[0]

    print("\nPredicted Next Expense Amount =", round(next_expense, 2))


while True:
    print("\n====== SMART EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Expense Chart")
    print("6. ML Prediction")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        expense_chart()

    elif choice == "6":
        ml_prediction()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

    