def clean_data(df):

    # Convert date
    df['Date'] = df['Date'].astype('datetime64[ns]')

    # Remove missing values
    df.dropna(inplace=True)

    # Create month column
    df['Month'] = df['Date'].dt.month_name()

    print("\n✅ Data Cleaning Completed!")

    return df