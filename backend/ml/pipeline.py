from backend.ml.data_generator import generate_enterprise_data
from backend.features.engine import create_advanced_features
from backend.ml.xgboost_model import XGBoostForecaster
from backend.ml.evaluation import EvaluationEngine
from backend.inventory.optimizer import InventoryOptimizer
from src.logger import logger
import pandas as pd
import os

def run_enterprise_pipeline():
    logger.info("Initializing Enterprise Demand Intelligence Pipeline...")
    
    # 1. Generate Data (5 stores, 20 products for demo)
    if not os.path.exists('data/enterprise_demand_data.csv'):
        df = generate_enterprise_data(num_stores=5, num_products=20)
    else:
        df = pd.read_csv('data/enterprise_demand_data.csv')
    
    # 2. Feature Engineering
    logger.info("Running Advanced Feature Engineering...")
    df_feat = create_advanced_features(df)
    
    # 3. Model Training (Example: XGBoost on first product)
    logger.info("Training Forecasting Models...")
    # Filter for one SKU for demonstration speed
    sku_df = df_feat[df_feat['product_id'] == 'PROD_0000']
    X = sku_df.drop(columns=['sales', 'date', 'store_id', 'product_id'])
    y = sku_df['sales']
    
    forecaster = XGBoostForecaster()
    forecaster.train(X, y)
    
    # 4. Inference
    preds = forecaster.predict(X)
    
    # 5. Evaluation
    metrics = EvaluationEngine.calculate_all_metrics(y.values, preds)
    logger.info(f"Model Performance Metrics (WAPE): {metrics['WAPE']}%")
    
    # 6. Inventory Optimization
    opt = InventoryOptimizer()
    rop = opt.calculate_reorder_point(lead_time_days=7, daily_demand_mean=y.mean(), daily_demand_std=y.std())
    logger.info(f"Recommended Reorder Point for PROD_0000: {round(rop, 2)} units")

if __name__ == "__main__":
    run_enterprise_pipeline()
