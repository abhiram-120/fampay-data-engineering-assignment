import pandas as pd
import os

def load_data(filepath: str) -> pd.DataFrame:
    """
    Loads stock data from a CSV file.
    Ensures the 'date' column is converted to datetime objects.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Input file not found at: {filepath}")
    
    # Read CSV and parse the 'date' column immediately
    df = pd.read_csv(filepath, parse_dates=['date'])
    return df

def save_ticker_data(df: pd.DataFrame, ticker: str, output_dir: str):
    """
    Saves the processed dataframe to a CSV file.
    Filename format: result_{SYMBOL}.csv
    """
    # Create the folder if it doesn't exist (Safety check)
    os.makedirs(output_dir, exist_ok=True)
    
    filename = f"result_{ticker}.csv"
    filepath = os.path.join(output_dir, filename)
    
    # Save to CSV. We do not include the index (date) as a separate column 
    # unless you want the date to be the first column. 
    # Usually, keeping the index is good for time series.
    df.to_csv(filepath)
    print(f"✅ Saved: {filename}")