import pandas as pd

def resample_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    """
    Resamples daily data to monthly frequency.
    Logic:
    - Open: Price on the first trading day of the month.
    - High: Max price during the month.
    - Low: Min price during the month.
    - Close: Price on the last trading day of the month.
    """
    # Resample to Month End ('ME')
    # Note: 'ME' is the alias for Month End in newer Pandas versions. 
    # If using older pandas, 'M' works too.
    monthly_df = df.resample('ME').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'  # Optional but good practice to sum volume
    })
    
    # Drop rows where data might be missing (e.g., if the resampler created a future date)
    monthly_df.dropna(subset=['close'], inplace=True)
    
    return monthly_df

def calculate_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates SMA and EMA technical indicators based on the Monthly Close price.
    
    Constraint Checklist:
    - SMA 10 & 20
    - EMA 10 & 20
    - EMA Logic: Must use recursive formula (adjust=False) to match the prompt's math.
    """
    
    # 1. Simple Moving Averages (SMA)
    # The mean of the last N months
    df['SMA_10'] = df['close'].rolling(window=10).mean()
    df['SMA_20'] = df['close'].rolling(window=20).mean()
    
    # 2. Exponential Moving Averages (EMA)
    # The prompt specifies the recursive formula: 
    # EMA = (Current - Prev) * Multiplier + Prev
    # In Pandas, this corresponds to adjust=False.
    df['EMA_10'] = df['close'].ewm(span=10, adjust=False).mean()
    df['EMA_20'] = df['close'].ewm(span=20, adjust=False).mean()
    
    return df