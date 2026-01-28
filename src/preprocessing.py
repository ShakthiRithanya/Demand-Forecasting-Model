import pandas as pd
import numpy as np
from src.logger import logger

def load_data(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df

def save_processed_data(df, file_path):
    df.to_csv(file_path)
    logger.info(f"Processed data saved to {file_path}")

def add_date_features(df):
    df['day'] = df.index.day
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofweek'] = df.index.dayofweek
    df['is_weekend'] = df.index.dayofweek.isin([5, 6]).astype(int)
    return df

def add_cyclic_features(df):
    df['day_sin'] = np.sin(2 * np.pi * df.index.day / 31)
    df['day_cos'] = np.cos(2 * np.pi * df.index.day / 31)
    df['month_sin'] = np.sin(2 * np.pi * df.index.month / 12)
    df['month_cos'] = np.cos(2 * np.pi * df.index.month / 12)
    return df

def add_lag_features(df, lags=[1, 7, 30]):
    for lag in lags:
        df[f'lag_{lag}'] = df['demand'].shift(lag)
    return df

def add_rolling_features(df, windows=[7, 30]):
    for window in windows:
        df[f'rolling_mean_{window}'] = df['demand'].rolling(window=window).mean()
        df[f'rolling_std_{window}'] = df['demand'].rolling(window=window).std()
    return df

if __name__ == "__main__":
    logger.info("Starting data preprocessing...")
    df = load_data('data/demand_data.csv')
    df = add_date_features(df)
    df = add_cyclic_features(df)
    df = add_lag_features(df)
    df = add_rolling_features(df)
    
    # Drop rows with NaN values (resulting from lags and rolling windows)
    df.dropna(inplace=True)
    
    save_processed_data(df, 'data/processed_demand_data.csv')
    logger.info("Preprocessing complete.")
