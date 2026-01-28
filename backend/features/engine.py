import pandas as pd
import numpy as np

def create_advanced_features(df):
    """
    Implements:
    - Lag features
    - Rolling stats
    - Temporal encodings
    """
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(['store_id', 'product_id', 'date'])
    
    # 1. Lags
    for lag in [7, 14, 30]:
        df[f'sales_lag_{lag}'] = df.groupby(['store_id', 'product_id'])['sales'].shift(lag)
        
    # 2. Rolling Statistics
    for window in [7, 30]:
        df[f'rolling_mean_{window}'] = df.groupby(['store_id', 'product_id'])['sales'].transform(lambda x: x.shift(1).rolling(window=window).mean())
        df[f'rolling_std_{window}'] = df.groupby(['store_id', 'product_id'])['sales'].transform(lambda x: x.shift(1).rolling(window=window).std())
        
    # 3. Temporal Features
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    
    # Cyclic encoding
    df['dow_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7)
    df['dow_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7)
    df['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)
    df['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)
    
    return df.dropna()
