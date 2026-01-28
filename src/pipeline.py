from src.data_generator import generate_demand_data
from src.preprocessing import add_date_features, add_lag_features, add_rolling_features
from src.train import load_processed_data, split_data
from src.models import RandomForestForecaster, ArimaModel, calculate_metrics
from src.config import DATA_PATH, PROCESSED_DATA_PATH, MODEL_SAVE_PATH
import pandas as pd
import datetime
import os

def run_full_pipeline():
    print("Starting full pipeline...")
    
    # 1. Generate Data
    if not os.path.exists(DATA_PATH):
        print("Generating synthetic data...")
        df = generate_demand_data(datetime.datetime(2023, 1, 1), 730)
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        df.to_csv(DATA_PATH, index=False)
    
    # 2. Preprocess Data
    print("Preprocessing data...")
    df = pd.read_csv(DATA_PATH, index_col='date', parse_dates=True)
    df = add_date_features(df)
    df = add_lag_features(df)
    df = add_rolling_features(df)
    df.dropna(inplace=True)
    df.to_csv(PROCESSED_DATA_PATH)
    
    # 3. Train and Save
    print("Training models...")
    train, test = split_data(df)
    rf = RandomForestForecaster()
    rf.fit(train.drop(columns=['demand']), train['demand'])
    
    # Save
    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
    import joblib
    joblib.dump(rf.model, MODEL_SAVE_PATH)
    print(f"Pipeline complete. Models saved to {MODEL_SAVE_PATH}")

if __name__ == "__main__":
    run_full_pipeline()
