from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    df = pd.read_csv('data/demand_data.csv')
    # Return last 30 days
    data = df.tail(30).to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
