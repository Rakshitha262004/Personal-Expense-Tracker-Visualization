import os

def generate_report(
    df,
    category_result,
    payment_result,
    avg_daily
):

    os.makedirs("reports", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    highest_category = category_result.idxmax()

    report = f"""
PERSONAL EXPENSE TRACKER REPORT
====================================

Total Expense: Rs.{df['Amount'].sum()}

Highest Spending Category: {highest_category}

Average Daily Spending: Rs.{avg_daily:.2f}

Top Categories:
{category_result.head()}

Payment Method Summary:
{payment_result}
"""

    # IMPORTANT FIX → encoding='utf-8'
    with open(
        "reports/expense_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    # Save CSV outputs
    category_result.to_csv(
        "outputs/category_analysis.csv"
    )

    payment_result.to_csv(
        "outputs/payment_analysis.csv"
    )

    print("\n✅ Reports Generated Successfully!")