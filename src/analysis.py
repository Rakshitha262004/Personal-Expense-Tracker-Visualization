def category_analysis(df):

    result = df.groupby('Category')['Amount'].sum().sort_values(
        ascending=False
    )

    print("\n📊 Category-wise Analysis")

    print(result)

    return result


def monthly_analysis(df):

    result = df.groupby('Month')['Amount'].sum()

    print("\n📈 Monthly Analysis")

    print(result)

    return result


def payment_analysis(df):

    result = df.groupby('Payment_Method')['Amount'].sum()

    print("\n💳 Payment Method Analysis")

    print(result)

    return result


def daily_spending_analysis(df):

    result = df.groupby('Date')['Amount'].sum()

    avg_daily = result.mean()

    print(f"\n💰 Average Daily Spending: ₹{avg_daily:.2f}")

    return result, avg_daily