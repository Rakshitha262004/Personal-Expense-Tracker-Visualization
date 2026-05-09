import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# -----------------------------------
# DATA PATH
# -----------------------------------

DATA_PATH = "data/expense_data.csv"

# -----------------------------------
# LOAD DATA
# -----------------------------------

if os.path.exists(DATA_PATH):

    df = pd.read_csv(DATA_PATH)

else:

    df = pd.DataFrame(
        columns=[
            "Date",
            "Category",
            "Amount",
            "Payment_Method",
            "Note"
        ]
    )

# -----------------------------------
# FIX DATE FORMAT ISSUE
# -----------------------------------

if not df.empty:

    df['Date'] = pd.to_datetime(
        df['Date'],
        format='mixed',
        errors='coerce'
    )

    # Remove invalid dates
    df.dropna(subset=['Date'], inplace=True)

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("💰 Expense Tracker")

st.sidebar.markdown("## ➕ Add Expense")

expense_date = st.sidebar.date_input(
    "Date",
    datetime.today()
)

category = st.sidebar.selectbox(
    "Category",
    [
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Entertainment",
        "Healthcare",
        "Education"
    ]
)

amount = st.sidebar.number_input(
    "Amount",
    min_value=1,
    step=1
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Cash",
        "UPI",
        "Credit Card",
        "Debit Card"
    ]
)

note = st.sidebar.text_input("Note")

# -----------------------------------
# ADD EXPENSE BUTTON
# -----------------------------------

if st.sidebar.button("Add Expense"):

    new_expense = pd.DataFrame({

        "Date": [
            pd.Timestamp(expense_date)
        ],

        "Category": [category],

        "Amount": [amount],

        "Payment_Method": [payment_method],

        "Note": [note]
    })

    df = pd.concat(
        [df, new_expense],
        ignore_index=True
    )

    # Convert all dates properly
    df['Date'] = pd.to_datetime(df['Date'])

    # Save CSV
    df.to_csv(DATA_PATH, index=False)

    st.sidebar.success(
        "✅ Expense Added Successfully!"
    )

# -----------------------------------
# MAIN DASHBOARD
# -----------------------------------

st.title("📊 Personal Expense Tracker Dashboard")

st.markdown("---")

# -----------------------------------
# METRICS
# -----------------------------------

if not df.empty:

    total_expense = df['Amount'].sum()

    average_expense = df['Amount'].mean()

    top_category = df.groupby(
        'Category'
    )['Amount'].sum().idxmax()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "💸 Total Expense",
        f"Rs. {total_expense:,.0f}"
    )

    col2.metric(
        "📈 Average Expense",
        f"Rs. {average_expense:.2f}"
    )

    col3.metric(
        "🏆 Top Category",
        top_category
    )

# -----------------------------------
# FILTERS
# -----------------------------------

st.markdown("## 🔍 Filters")

selected_categories = st.multiselect(
    "Select Categories",
    options=df['Category'].unique(),
    default=list(df['Category'].unique())
)


filtered_df = df[
    df['Category'].isin(
        selected_categories
    )
]

# -----------------------------------
# VISUALIZATIONS
# -----------------------------------

st.markdown("## 📊 Financial Insights")

col1, col2 = st.columns(2)

# -----------------------------------
# CATEGORY CHART
# -----------------------------------

with col1:

    st.subheader("Category-wise Spending")

    category_analysis = filtered_df.groupby(
        'Category'
    )['Amount'].sum()

    fig1, ax1 = plt.subplots(
        figsize=(4, 3)
    )

    category_analysis.plot(
        kind='bar',
        ax=ax1
    )

    plt.xticks(rotation=30)

    st.pyplot(fig1)

# -----------------------------------
# PAYMENT METHOD CHART
# -----------------------------------

with col2:

    st.subheader("Payment Method Usage")

    payment_analysis = filtered_df.groupby(
        'Payment_Method'
    )['Amount'].sum()

    fig2, ax2 = plt.subplots(
        figsize=(4, 3)
    )

    payment_analysis.plot(
        kind='pie',
        autopct='%1.1f%%',
        ax=ax2
    )

    ax2.set_ylabel("")

    st.pyplot(fig2)

# -----------------------------------
# MONTHLY TREND
# -----------------------------------

st.markdown("## 📈 Monthly Spending Trend")

filtered_df['Month'] = filtered_df[
    'Date'
].dt.strftime('%b')

monthly_analysis = filtered_df.groupby(
    'Month'
)['Amount'].sum()

fig3, ax3 = plt.subplots(
    figsize=(7, 3)
)

monthly_analysis.plot(
    marker='o',
    ax=ax3
)

st.pyplot(fig3)

# -----------------------------------
# RECENT EXPENSES
# -----------------------------------

st.markdown("## 📄 Recent Expenses")

recent_df = filtered_df.sort_values(
    by='Date',
    ascending=False
).head(10)

st.dataframe(
    recent_df,
    width='stretch'
)

# -----------------------------------
# DOWNLOAD BUTTON
# -----------------------------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Expense Data",
    data=csv,
    file_name="expense_data.csv",
    mime="text/csv"
)

# -----------------------------------
# SUCCESS MESSAGE
# -----------------------------------

st.success(
    "✅ Dashboard Loaded Successfully!"
)