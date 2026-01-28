import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_demand_data(start_date, periods, freq='D'):
    """
    Generates synthetic demand data with seasonality, trend, and noise.

    Args:
        start_date (datetime): The starting date for the data.
        periods (int): Number of time steps to generate.
        freq (str): Frequency of the time series (default 'D' for daily).

    Returns:
        pd.DataFrame: A dataframe containing 'date' and 'demand' columns.
    """
    date_range = pd.date_range(start=start_date, periods=periods, freq=freq)
    
    # Base demand
    base_demand = 100
    
    # Trend: slightly upward
    trend = np.linspace(0, 50, periods)
    
    # Seasonality: Weekly (7 days)
    weekly_seasonality = 20 * np.sin(2 * np.pi * date_range.dayofweek / 7)
    
    # Seasonality: Monthly (approx 30 days)
    monthly_seasonality = 15 * np.sin(2 * np.pi * date_range.day / 30)
    
    # Noise
    noise = np.random.normal(0, 5, periods)
    
    demand = base_demand + trend + weekly_seasonality + monthly_seasonality + noise
    
    df = pd.DataFrame({
        'date': date_range,
        'demand': demand
    })
    
    # Ensure demand is non-negative
    df['demand'] = df['demand'].apply(lambda x: max(0, x))
    
    return df

if __name__ == "__main__":
    start_date = datetime(2023, 1, 1)
    df = generate_demand_data(start_date, 730) # 2 years of daily data
    df.to_csv('data/demand_data.csv', index=False)
    print("Synthetic demand data generated and saved to data/demand_data.csv")
