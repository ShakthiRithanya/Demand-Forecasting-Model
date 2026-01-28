from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

class EvaluationEngine:
    @staticmethod
    def calculate_all_metrics(y_true, y_pred):
        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        
        # MAPE (Mean Absolute Percentage Error) - handle zero y_true
        mask = y_true != 0
        mape = np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100
        
        # WAPE (Weighted Absolute Percentage Error)
        wape = np.sum(np.abs(y_true - y_pred)) / np.sum(y_true) * 100
        
        return {
            "MAE": round(mae, 4),
            "RMSE": round(rmse, 4),
            "MAPE": round(mape, 2),
            "WAPE": round(wape, 2)
        }
    
    @staticmethod
    def get_leaderboard(product_metrics):
        """
        product_metrics: list of dicts {model_name, metrics}
        """
        return sorted(product_metrics, key=lambda x: x['metrics']['WAPE'])
