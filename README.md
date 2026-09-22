# Expense Tracker

A simple command-line expense tracker built with Python and SQLite, with data analysis using pandas and matplotlib.

## Features
- Add expenses with category and amount (date recorded automatically)
- View all recorded expenses
- Filter expenses by category
- Calculate total spending
- Visualize spending by category with a bar chart

## Technologies Used
- Python
- SQLite (via `sqlite3`)
- pandas
- matplotlib

## How to Run
1. Open the notebook in Google Colab or any Python environment
2. Run all cells
3. The demonstration section shows adding sample expenses, viewing totals, and generating a chart

## 📊 Example Output

When you execute the tracker, the application processes your data and prints a structured summary directly to your terminal:

```text
======================================
       EXPENSE TRACKER SUMMARY        
======================================
 Total Spent: Rs. 1050.00
--------------------------------------
 Category Breakdown:
 🍔 Food:          Rs. 500.00  (47.6%)
 🎬 Entertainment: Rs. 350.00  (33.3%)
 🚌 Transport:     Rs. 200.00  (19.1%)
======================================
```
*Note: A matplotlib window will automatically pop up displaying a bar chart breakdown of these categories.*

