import pandas as pd
import numpy as np
import os
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

    # 3. Random Forest Model
    from src.models import RandomForestForecaster
    X_train = train.drop(columns=['demand'])
    y_train = train['demand']
    X_test = test.drop(columns=['demand'])
    y_test = test['demand']
    
    rf = RandomForestForecaster()
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    rf_metrics = calculate_metrics(y_test, rf_pred)
    print(f"Random Forest Metrics: {rf_metrics}")
    
    # Save the best model (using RF as example)
    os.makedirs('models', exist_ok=True)
    joblib.dump(rf.model, 'models/rf_model.joblib')
    print("Best model saved to models/rf_model.joblib")
