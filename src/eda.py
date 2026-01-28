import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_eda(file_path):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    # 1. Plot the demand over time
    plt.figure(figsize=(12, 6))
    plt.plot(df['demand'])
    plt.title('Demand Over Time')
    plt.xlabel('Date')
    plt.ylabel('Demand')
    plt.grid(True)
    plt.savefig('notebooks/demand_over_time.png')
    
    # 2. Distribution of demand
    plt.figure(figsize=(10, 6))
    sns.histplot(df['demand'], kde=True)
    plt.title('Distribution of Demand')
    plt.savefig('notebooks/demand_distribution.png')
    
    # 3. Monthly demand
    plt.figure(figsize=(12, 6))
    df['month'] = df.index.month
    sns.boxplot(x='month', y='demand', data=df)
    plt.title('Monthly Demand Distribution')
    plt.savefig('notebooks/monthly_demand.png')
    
    # 4. Day of week demand
    plt.figure(figsize=(12, 6))
    df['day_of_week'] = df.index.dayofweek
    sns.boxplot(x='day_of_week', y='demand', data=df)
    plt.title('Day of Week Demand Distribution')
    plt.savefig('notebooks/daily_demand.png')
    
    # 5. Correlation Heatmap
    plt.figure(figsize=(12, 10))
    # Filter only numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Feature Correlation Heatmap')
    plt.savefig('notebooks/correlation_heatmap.png')
    
    logger.info("EDA completed. Visualizations saved to notebooks/ folder.")

if __name__ == "__main__":
    run_eda('data/demand_data.csv')
