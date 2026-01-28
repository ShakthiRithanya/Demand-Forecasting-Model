import pandas as pd
import numpy as np
from src.models import BaselineModel, ArimaModel, calculate_metrics
import joblib

def load_processed_data(file_path):
    df = pd.read_csv(file_path, index_col='date', parse_dates=True)
    return df

def split_data(df, test_size=0.2):
    split_idx = int(len(df) * (1 - test_size))
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]
    return train, test

if __name__ == "__main__":
    df = load_processed_data('data/processed_demand_data.csv')
    train, test = split_data(df)
    print(f"Data split into train ({len(train)}) and test ({len(test)}) sets.")
