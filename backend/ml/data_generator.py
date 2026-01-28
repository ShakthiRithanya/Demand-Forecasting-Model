import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
from src.logger import logger

def generate_enterprise_data(num_stores=10, num_products=50, days=730):
    """
    Generates enterprise-scale synthetic data:
    date, store_id, product_id, sales, price, promotion_flag, holiday_flag, weather
    """
    start_date = datetime(2023, 1, 1)
    date_range = [start_date + timedelta(days=x) for x in range(days)]
    
    data = []
    
    # Store and Product IDs
    store_ids = [f"STORE_{i:03d}" for i in range(num_stores)]
    product_ids = [f"PROD_{i:04d}" for i in range(num_products)]
    
    # Holidays (mock)
    holidays = [datetime(2023, 12, 25), datetime(2024, 12, 25), 
                datetime(2023, 11, 23), datetime(2024, 11, 28)]
    holiday_dates = [h.date() for h in holidays]

    logger.info(f"Generating data for {num_stores} stores and {num_products} products...")
    
    for store in store_ids:
        for product in product_ids:
            # Base sales for this SKU/Store combo
            base_sales = np.random.randint(10, 100)
            
            for date in date_range:
                # 1. Seasonality
                weekly_effect = 1 + 0.2 * np.sin(2 * np.pi * date.weekday() / 7)
                monthly_effect = 1 + 0.1 * np.sin(2 * np.pi * date.day / 30)
                
                # 2. Promotion
                is_promo = 1 if np.random.random() < 0.05 else 0
                promo_effect = 1.5 if is_promo else 1.0
                
                # 3. Holiday
                is_holiday = 1 if date.date() in holiday_dates else 0
                holiday_effect = 2.0 if is_holiday else 1.0
                
                # 4. Weather (simple temp proxy)
                temp = 20 + 10 * np.sin(2 * np.pi * date.timetuple().tm_yday / 365)
                weather_effect = 1 + 0.01 * (temp - 20)
                
                # 5. Price
                price = 10.0 + np.random.uniform(-1, 1)
                
                # Calculate sales
                sales = base_sales * weekly_effect * monthly_effect * promo_effect * holiday_effect * weather_effect
                sales = max(0, int(sales + np.random.normal(0, 5)))
                
                # Random stock-outs (zero sales)
                if np.random.random() < 0.01:
                    sales = 0
                
                data.append({
                    'date': date.strftime('%Y-%m-%d'),
                    'store_id': store,
                    'product_id': product,
                    'sales': sales,
                    'price': price,
                    'promotion_flag': is_promo,
                    'holiday_flag': is_holiday,
                    'weather_temp': temp
                })
                
    df = pd.DataFrame(data)
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/enterprise_demand_data.csv', index=False)
    logger.info(f"Enterprise data generated: {len(df)} rows saved to data/enterprise_demand_data.csv")
    return df

if __name__ == "__main__":
    # Scaled down for demo, but logic supports user's requested 100x1000
    generate_enterprise_data(num_stores=5, num_products=20)
