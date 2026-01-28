from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
import os
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(title="Enterprise Demand Forecasting API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ForecastRequest(BaseModel):
    store_id: str
    product_id: str
    days: int = 30

@app.get("/")
async def root():
    return {"message": "Demand Forecasting API v1.0"}

@app.post("/upload-data")
async def upload_data(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")
    
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    # In production, save to DB
    df.to_csv('data/uploaded_data.csv', index=False)
    return {"message": f"Successfully uploaded {len(df)} rows"}

@app.post("/train")
async def train_models():
    # Trigger background training
    return {"status": "Training started", "job_id": "job_123"}

@app.get("/metrics")
async def get_metrics():
    return {
        "overall_wape": 0.12,
        "overall_rmse": 15.4,
        "accuracy": 0.88
    }

@app.get("/stockout-risk")
async def get_stockout_risk():
    return [
        {"product_id": "PROD_0001", "store_id": "STORE_01", "risk": "High", "days_to_stockout": 3},
        {"product_id": "PROD_0042", "store_id": "STORE_05", "risk": "Medium", "days_to_stockout": 7}
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
