import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
from datetime import datetime

# Connect to the database (creates the file if it doesn't exist yet)
conn = sqlite3.connect("expensedb")
cursor = conn.cursor()

# Create the expenses table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS expense(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
category TEXT,
amount REAL
)
''')

conn.commit()


# Adds a new expense to the database, with today's date attached automatically
def add_expense(category, amount):
    category = category.title()  # standardizes category name (e.g. "food" -> "Food")
    date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute(
        "INSERT INTO expense (date, category, amount) VALUES (?, ?, ?)",
        (date, category, amount)
    )
    conn.commit()


# Deletes an expense from the database by its ID
def delete_expense(id):
    cursor.execute("DELETE FROM expense WHERE id = ?", (id,))
    conn.commit()


# Prints every expense currently stored in the database
def view_expense():
    cursor.execute("SELECT * FROM expense")
    rows = cursor.fetchall()
    print("\n---- ALL EXPENSES ----")
    for row in rows:
        print(f"{row[0]} - {row[1]} - {row[2]} - Rs.{row[3]}")


# Calculates and prints the total amount spent across all expenses
def total_spent():
    cursor.execute("SELECT SUM(amount) FROM expense")
    total = cursor.fetchone()[0]
    print(f"\nTotal spent: Rs.{total if total else 0}")


# Prints all expenses matching a specific category
def filter_by_category(category):
    cursor.execute("SELECT * FROM expense WHERE category = ?", (category,))
    rows = cursor.fetchall()
    print(f"\n---- EXPENSES FOR {category} ----")
    for row in rows:
        print(f"{row[0]} - {row[1]} - {row[2]} - Rs.{row[3]}")


# --- Demonstration: adding sample expenses and testing each feature ---

add_expense("Food", 500)
add_expense("Transport", 200)
add_expense("Entertainment", 350)

view_expense()
total_spent()
filter_by_category("Food")

# Load all expenses into a DataFrame for analysis
df = pd.read_sql_query("SELECT * FROM expense", conn)
df["category"] = df["category"].str.title()

# Show total spending grouped by category
print(df.groupby("category")["amount"].sum())

# Visualize spending by category as a bar chart
df.groupby("category")["amount"].sum().plot(kind="bar")
plt.show()
