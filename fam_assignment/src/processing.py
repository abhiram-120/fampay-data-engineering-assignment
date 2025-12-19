import pandas as pd

def resample_data(df):
    # Resample to month-end frequency
    # using 'ME' because 'M' is deprecated in newer pandas
    monthly = df.resample('ME').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    })
    
    return monthly

def add_indicators(df):
    # Simple Moving Average
    df['SMA_10'] = df['close'].rolling(window=10).mean()
    df['SMA_20'] = df['close'].rolling(window=20).mean()
    
    # Exponential Moving Average
    # adjust=False is needed to match the recursive formula:
    # EMA_today = (Price_today * alpha) + (EMA_yesterday * (1-alpha))
    df['EMA_10'] = df['close'].ewm(span=10, adjust=False).mean()
    df['EMA_20'] = df['close'].ewm(span=20, adjust=False).mean()
    
    return df
