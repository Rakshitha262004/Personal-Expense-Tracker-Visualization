import pandas as pd

def load_data(file_path):

    df = pd.read_csv(file_path)

    print("\n✅ Dataset Loaded Successfully!")

    print(df.head())

    return df