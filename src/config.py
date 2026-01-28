# Configuration settings for Demand Forecasting Model

DATA_PATH = 'data/demand_data.csv'
PROCESSED_DATA_PATH = 'data/processed_demand_data.csv'
MODEL_SAVE_PATH = 'models/rf_model.joblib'

# Model Hyperparameters
RF_PARAMS = {
    'n_estimators': 100,
    'max_depth': 10,
    'random_state': 42
}

ARIMA_ORDER = (5, 1, 0)
TEST_SIZE = 0.2
