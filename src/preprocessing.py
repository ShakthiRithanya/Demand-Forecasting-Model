import pandas as pd
import numpy as np

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df

def save_processed_data(df, file_path):
    df.to_csv(file_path)
    print(f"Processed data saved to {file_path}")

if __name__ == "__main__":
    df = load_data('data/demand_data.csv')
    save_processed_data(df, 'data/processed_demand_data.csv')
