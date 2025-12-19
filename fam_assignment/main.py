import pandas as pd
from src.utils import load_data, save_ticker_data
from src.processing import resample_to_monthly, calculate_technical_indicators

# Define Configuration Paths
INPUT_PATH = 'data/input/stock_prices.csv'
OUTPUT_DIR = 'data/output'

def main():
    print("🚀 Starting Data Pipeline...")
    
    # Step 1: Load the raw data
    try:
        raw_df = load_data(INPUT_PATH)
    except Exception as e:
        print(f"❌ Critical Error: {e}")
        return

    # Step 2: Identify unique stock symbols (Tickers)
    tickers = raw_df['ticker'].unique()
    print(f"📊 Found {len(tickers)} tickers in the dataset: {tickers}")
    
    # Step 3: Loop through each ticker to process them independently
    for ticker in tickers:
        # Filter data for the specific ticker
        ticker_df = raw_df[raw_df['ticker'] == ticker].copy()
        
        # Sort by date is crucial for Rolling Windows/Resampling to work correctly
        ticker_df = ticker_df.sort_values('date')
        
        # Set Date as Index (Required for .resample() to work)
        ticker_df.set_index('date', inplace=True)
        
        # Step 4: Resample Daily -> Monthly
        monthly_df = resample_to_monthly(ticker_df)
        
        # Step 5: Calculate Indicators (SMA/EMA)
        final_df = calculate_technical_indicators(monthly_df)
        
        # ROUNDING: Clean up the output to 2 decimal places for readability
        # (This makes the CSV look professional, though high precision is preserved internally)
        final_df = final_df.round(2)

        # Step 6: Save the result
        save_ticker_data(final_df, ticker, OUTPUT_DIR)
        
    print(f"\n✅ Pipeline Completed Successfully. Results are in '{OUTPUT_DIR}'")

if __name__ == "__main__":
    main()