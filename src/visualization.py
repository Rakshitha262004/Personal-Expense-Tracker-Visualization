import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations(
    category_result,
    monthly_result,
    payment_result,
    daily_result
):

    os.makedirs("images", exist_ok=True)

    sns.set_style("whitegrid")

    # Category-wise Bar Chart
    plt.figure(figsize=(10, 6))

    category_result.plot(kind='bar')

    plt.title('Category-wise Spending')

    plt.tight_layout()

    plt.savefig("images/category_spending.png")

    plt.close()

    # Monthly Trend Chart
    plt.figure(figsize=(10, 6))

    monthly_result.plot(marker='o')

    plt.title('Monthly Spending Trend')

    plt.tight_layout()

    plt.savefig("images/monthly_trend.png")

    plt.close()

    # Payment Method Pie Chart
    plt.figure(figsize=(8, 8))

    payment_result.plot(
        kind='pie',
        autopct='%1.1f%%'
    )

    plt.ylabel('')

    plt.title('Payment Method Distribution')

    plt.tight_layout()

    plt.savefig("images/payment_method.png")

    plt.close()

    # Daily Spending Trend
    plt.figure(figsize=(12, 6))

    daily_result.plot()

    plt.title('Daily Spending Trend')

    plt.tight_layout()

    plt.savefig("images/daily_spending.png")

    plt.close()

    print("\n✅ Charts Generated!")