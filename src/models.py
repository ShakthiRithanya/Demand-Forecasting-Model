import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def calculate_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    return {'MSE': mse, 'MAE': mae, 'RMSE': rmse}

from statsmodels.tsa.arima.model import ARIMA

class ArimaModel:
    def __init__(self, order=(5, 1, 0)):
        self.order = order
    
    def fit_predict(self, train_data, test_data_len):
        model = ARIMA(train_data, order=self.order)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=test_data_len)
        return forecast

class BaselineModel:
    def __init__(self, window=7):
        self.window = window
    
    def predict(self, df):
        # Simply use the rolling mean of the last 'window' days as the prediction
        return df['demand'].rolling(window=self.window).mean().shift(1)

if __name__ == "__main__":
    df = pd.read_csv('data/demand_data.csv', index_col='date', parse_dates=True)
    
    baseline = BaselineModel(window=7)
    df['baseline_pred'] = baseline.predict(df)
    
    # Evaluate (avoiding NaNs)
    eval_df = df.dropna()
    metrics = calculate_metrics(eval_df['demand'], eval_df['baseline_pred'])
    print(f"Baseline Metrics (7-day Moving Average): {metrics}")
