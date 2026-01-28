from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

class XGBoostForecaster:
    def __init__(self):
        self.model = XGBRegressor(
            n_estimators=1000,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
            n_jobs=-1
        )
        
    def train(self, X, y):
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1, shuffle=False)
        self.model.fit(
            X_train, y_train,
            eval_set=[(X_val, y_val)],
            verbose=False
        )
        
    def predict(self, X):
        return self.model.predict(X)
    
    def save(self, path):
        joblib.dump(self.model, path)
        
    def load(self, path):
        self.model = joblib.load(path)
