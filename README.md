# Smart Expense Tracker with ML Prediction

A command-line expense tracking application in Python that logs expenses, generates category-wise summaries and visualizations, and uses machine learning to predict future spending.

## Features

- **Add & view expenses**: Log expenses with date, category, and amount, stored persistently in a CSV file
- **Total & category summaries**: Instantly see total spending or a breakdown by category
- **Visualization**: Bar chart of expenses by category using Matplotlib
- **ML-based prediction**: Uses Linear Regression (scikit-learn) to predict the next likely expense amount based on spending trend

## Tech Stack

- **Language**: Python
- **Libraries**: Pandas (data handling), Matplotlib (visualization), scikit-learn (ML prediction)
- **Storage**: CSV file (auto-created on first run)

## How to run

```bash
pip install pandas matplotlib scikit-learn
python expense_tracker.py
```

## Menu Options

1. Add Expense
2. View Expenses
3. Total Expense
4. Category Summary
5. Expense Chart
6. ML Prediction (requires at least 5 logged expenses)
7. Exit

## Possible Future Improvements

- Switch from CSV to SQLite for more robust storage
- Add a GUI (Tkinter/Streamlit) for easier use
- Use time-series-aware forecasting instead of simple linear regression
