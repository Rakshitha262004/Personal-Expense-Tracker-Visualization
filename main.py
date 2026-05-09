from src.data_generator import generate_expense_data
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analysis import (
    category_analysis,
    monthly_analysis,
    payment_analysis,
    daily_spending_analysis
)
from src.visualization import create_visualizations
from src.report_generator import generate_report

# Generate synthetic dataset
generate_expense_data()

# Load data
df = load_data("data/expense_data.csv")

# Clean data
df = clean_data(df)

# Perform analysis
category_result = category_analysis(df)
monthly_result = monthly_analysis(df)
payment_result = payment_analysis(df)
daily_result, avg_daily = daily_spending_analysis(df)

# Generate charts
create_visualizations(
    category_result,
    monthly_result,
    payment_result,
    daily_result
)

# Generate reports
generate_report(
    df,
    category_result,
    payment_result,
    avg_daily
)

print("\n✅ PROJECT EXECUTED SUCCESSFULLY!")