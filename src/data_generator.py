import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_expense_data():

    os.makedirs("data", exist_ok=True)

    categories = [
        'Food',
        'Travel',
        'Shopping',
        'Bills',
        'Entertainment',
        'Healthcare',
        'Education'
    ]

    payment_methods = [
        'Cash',
        'UPI',
        'Credit Card',
        'Debit Card'
    ]

    notes = [
        'Lunch',
        'Movie',
        'Books',
        'Medicine',
        'Groceries',
        'Fuel',
        'Shopping'
    ]

    data = []

    start_date = datetime(2025, 1, 1)

    for _ in range(200):

        random_date = start_date + timedelta(days=random.randint(0, 120))

        data.append([
            random_date.strftime('%Y-%m-%d'),
            random.choice(categories),
            random.randint(100, 5000),
            random.choice(payment_methods),
            random.choice(notes)
        ])

    df = pd.DataFrame(data, columns=[
        'Date',
        'Category',
        'Amount',
        'Payment_Method',
        'Note'
    ])

    df.to_csv("data/expense_data.csv", index=False)

    print("✅ Expense dataset created!")