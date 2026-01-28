from backend.ml.prophet_model import ProphetForecaster
from backend.ml.xgboost_model import XGBoostForecaster
import numpy as np

class EnsembleForecaster:
    def __init__(self, models=None):
        self.models = models or []
        
    def add_model(self, model):
        self.models.append(model)
        
    def weighted_forecast(self, X_inputs, weights=None):
        """
        X_inputs: List of inputs appropriate for each model in self.models
        weights: List of weights (summing to 1)
        """
        if not weights:
            weights = [1.0/len(self.models)] * len(self.models)
            
        final_forecast = None
        
        for model, input_data, weight in zip(self.models, X_inputs, weights):
            pred = model.predict(input_data)
            if final_forecast is None:
                final_forecast = pred * weight
            else:
                final_forecast += pred * weight
                
        return final_forecast
