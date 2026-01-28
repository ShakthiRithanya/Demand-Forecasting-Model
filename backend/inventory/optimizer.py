import numpy as np
import pandas as pd

class InventoryOptimizer:
    def __init__(self, service_level=0.95):
        # Z-score for service level (0.95 -> 1.645)
        self.z_score = 1.645 if service_level == 0.95 else 1.96 # simplified
        
    def calculate_reorder_point(self, lead_time_days, daily_demand_mean, daily_demand_std):
        """
        Reorder Point = LeadTimeDemand + SafetyStock
        SafetyStock = Z * StdDev * sqrt(LeadTime)
        """
        lead_time_demand = daily_demand_mean * lead_time_days
        safety_stock = self.z_score * daily_demand_std * np.sqrt(lead_time_days)
        
        return lead_time_demand + safety_stock
    
    def recommend_quantity(self, current_stock, reorder_point, target_stock):
        if current_stock <= reorder_point:
            return max(0, target_stock - current_stock)
        return 0

    def simulate_inventory(self, initial_stock, demand_forecast, lead_time, reorder_qty):
        """
        Simulates inventory over time given a forecast
        """
        stock_levels = []
        current_stock = initial_stock
        pending_orders = [] # list of (arrival_day, qty)
        
        for day, demand in enumerate(demand_forecast):
            # Check for arrivals
            for order in pending_orders[:]:
                if order[0] == day:
                    current_stock += order[1]
                    pending_orders.remove(order)
            
            # Satisfy demand
            current_stock -= demand
            stock_levels.append({
                'day': day,
                'stock': max(0, current_stock),
                'stockout': 1 if current_stock < 0 else 0
            })
            
            # Reorder logic (simplified)
            if current_stock < 50 and not pending_orders: # threshold 50
                pending_orders.append((day + lead_time, reorder_qty))
                
        return stock_levels
