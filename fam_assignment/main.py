import pandas as pd
from src.utils import load_data, save_to_csv
from src.processing import resample_data, add_indicators

# Config
INPUT_FILE = 'data/input/stock_prices.csv'
OUTPUT_DIR = 'data/output'

def main():
    print("Reading master dataset...")
    df = load_data(INPUT_FILE)
    
    # Get unique tickers
    tickers = df['ticker'].unique()
    print(f"Found {len(tickers)} symbols.")

    for ticker in tickers:
        # Filter for current stock
        # Copy is needed to avoid Setting WithCopy warnings later
        stock_df = df[df['ticker'] == ticker].copy()
        
        # Date must be index for resampling
        stock_df = stock_df.set_index('date').sort_index()
        
        # 1. Resample to Monthly
        monthly_df = resample_data(stock_df)
        
        # 2. Add Indicators (SMA/EMA)
        final_df = add_indicators(monthly_df)
        
        # 3. Save
        save_to_csv(final_df, ticker, OUTPUT_DIR)

    print("Job complete.")

if __name__ == "__main__":
    main()
