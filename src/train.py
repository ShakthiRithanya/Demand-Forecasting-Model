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
    
    # 1. Baseline Model
    baseline = BaselineModel(window=7)
    test_copy = test.copy()
    test_copy['baseline_pred'] = baseline.predict(df).iloc[train.shape[0]:]
    
    baseline_metrics = calculate_metrics(test_copy['demand'], test_copy['baseline_pred'])
    print(f"Baseline Metrics: {baseline_metrics}")

    # 2. ARIMA Model
    arima = ArimaModel()
    arima_pred = arima.fit_predict(train['demand'], len(test))
    arima_metrics = calculate_metrics(test['demand'], arima_pred)
    print(f"ARIMA Metrics: {arima_metrics}")
