from flask import Flask, render_template, jsonify
import pandas as pd
import os
import joblib
from src.config import MODEL_SAVE_PATH
from src.logger import logger

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    if not os.path.exists(MODEL_SAVE_PATH):
        return jsonify({'error': 'Model not found. Please train the model first.'}), 400
    
    try:
        model = joblib.load(MODEL_SAVE_PATH)
        # For simplicity, we'll just return a mock forecast starting from the last date
        df = pd.read_csv('data/demand_data.csv')
        last_date = pd.to_datetime(df['date'].iloc[-1])
        
        predictions = []
        for i in range(1, 8):
            next_date = last_date + pd.Timedelta(days=i)
            # Mock features here - in real app, you'd generate features for next_date
            # For now, just a dummy prediction based on model if possible, or random
            pred = float(model.predict(np.random.rand(1, 16))[0]) if hasattr(model, 'predict') else 150.0
            predictions.append({'date': next_date.strftime('%Y-%m-%d'), 'demand': pred})
            
        return jsonify(predictions)
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/data')
def get_data():
    df = pd.read_csv('data/demand_data.csv')
    # Return last 30 days
    data = df.tail(30).to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
