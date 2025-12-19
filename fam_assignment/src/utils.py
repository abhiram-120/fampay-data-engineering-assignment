import pandas as pd
import os

def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file missing: {path}")
        
    # Parsing dates on load is faster
    return pd.read_csv(path, parse_dates=['date'])

def save_to_csv(df, ticker, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"result_{ticker}.csv"
    path = os.path.join(output_dir, filename)
    
    # Default index=True keeps the Date column, which we want
    df.to_csv(path)
    print(f"Saved {ticker} to {path}")
