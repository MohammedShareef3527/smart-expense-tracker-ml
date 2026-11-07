<div align="center">

# Smart Expense Tracker with ML Prediction

**A command-line expense tracker that summarises spending, charts it, and predicts the next expense with linear regression.**

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=3776AB)
![pandas](https://img.shields.io/badge/pandas-0d1117?style=flat-square&logo=pandas&logoColor=E70488)
![Matplotlib](https://img.shields.io/badge/Matplotlib-0d1117?style=flat-square)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0d1117?style=flat-square&logo=scikitlearn&logoColor=F7931E)

</div>

---

## Overview

A menu-driven Python application for recording day-to-day expenses. Every expense is saved to a CSV file, so the data is still there next time. The app can show all expenses, the total, a category-wise summary and a bar chart, and it uses a **Linear Regression** model from scikit-learn to estimate the next expense amount from the spending trend.

## Problem Statement

Students and young earners often don't know where their money goes each month. A lightweight tracker that needs no account or internet, shows spending by category, and gives a simple forecast makes it easier to notice patterns and plan ahead.

## Features

- **Add expenses** with a date, category and amount
- **Persistent storage** in `expenses.csv`, created automatically on first run
- **View all expenses** as a table
- **Total expense** across all records
- **Category summary** showing the total spent per category
- **Bar chart** of spending by category with Matplotlib
- **ML prediction** of the next expense amount using Linear Regression (needs at least 5 expenses)

## Sample Session

Real output after adding five expenses (Food 250, Travel 120, Food 300, Books 450, Food 280). The repeated menu is trimmed:

```text
====== SMART EXPENSE TRACKER ======
1. Add Expense
2. View Expenses
3. Total Expense
4. Category Summary
5. Expense Chart
6. ML Prediction
7. Exit
Enter Choice: 3

Total Expense = 1400.0

Enter Choice: 4

Expense by Category:
Category
Books     450.0
Food      830.0
Travel    120.0
Name: Amount, dtype: float64

Enter Choice: 6

Predicted Next Expense Amount = 397.0
```

## Tech Stack

- **Language:** Python 3
- **Data handling:** pandas
- **Visualisation:** Matplotlib
- **Machine learning:** scikit-learn (`LinearRegression`)
- **Storage:** CSV file

## Project Structure

```text
smart-expense-tracker-ml/
├── expensetracker.py   # the complete application
├── requirements.txt
├── .gitignore          # ignores expenses.csv, so personal data is never committed
└── README.md
```

## Installation and Setup

```bash
git clone https://github.com/MohammedShareef3527/smart-expense-tracker-ml.git
cd smart-expense-tracker-ml
pip install -r requirements.txt
python expensetracker.py
```

Then choose an option from the menu:

| Option | Action |
|---|---|
| 1 | Add Expense (date as `YYYY-MM-DD`, category, amount) |
| 2 | View Expenses |
| 3 | Total Expense |
| 4 | Category Summary |
| 5 | Expense Chart |
| 6 | ML Prediction (needs at least 5 expenses) |
| 7 | Exit |

## Configuration

No configuration or API keys are needed. Data is stored in `expenses.csv` in the folder you run the program from. To use a different file, change `FILE_NAME` at the top of `expensetracker.py`.

## How It Works

1. **Storage.** On start-up the app creates `expenses.csv` with the columns `Date`, `Category` and `Amount` if it doesn't exist. New expenses are appended as rows.
2. **Analysis.** Each menu option reads the CSV into a pandas DataFrame. The total uses `df["Amount"].sum()`, and the category summary and chart use `df.groupby("Category")["Amount"].sum()`.
3. **Prediction.** The model treats the order of entries as time: entry number `0, 1, 2, …` is the input and the amount is the output. `LinearRegression` fits a straight line through these points, and the prediction for the next entry number is shown as the expected next expense.

## Limitations

- The prediction follows the overall trend in the order expenses were entered. It doesn't use the dates or categories, so treat it as a rough estimate.
- Inputs aren't validated: a non-numeric amount stops the program, and dates are stored exactly as typed.

## Future Improvements

These are planned ideas, not current features:

- Validate dates and amounts, and allow editing or deleting entries
- Monthly summaries and budget alerts
- Move from CSV to SQLite
- Predict monthly totals per category with date-aware time-series forecasting
- A GUI with Tkinter or a web dashboard with Streamlit

## Learning Outcomes

- Reading, appending and aggregating tabular data with pandas
- Visualising grouped data with Matplotlib
- Framing a simple prediction problem and training a scikit-learn regression model
- Building a menu-driven command-line program with persistent storage

## Author

**Mohammed Shamsul Qhadri Shareef**
GitHub: [@MohammedShareef3527](https://github.com/MohammedShareef3527)
