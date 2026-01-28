from prophet import Prophet
import pandas as pd

class ProphetForecaster:
    """
    Wrapper for Facebook Prophet with Store/Product intelligence
    """
    def __init__(self, holidays=None):
        self.model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=False,
            holidays=holidays
        )
        
    def train(self, df):
        """
        Prophet requires columns 'ds' and 'y'
        """
        train_df = df[['date', 'sales']].rename(columns={'date': 'ds', 'sales': 'y'})
        self.model.fit(train_df)
        
    def forecast(self, periods=30):
        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
