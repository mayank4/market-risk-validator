"""
fetch_data.py
Pulls daily market data for a set of tickers using yfinance.
Saves to CSVs for offline validation.
"""
import os
import yfinance as yf
import pandas as pd
from datetime import datetime
TICKERS = {
"equities": ["SPY", "QQQ", "IWM", "AAPL", "MSFT"],
"fx": ["EURUSD=X", "JPY=X", "GBPUSD=X"],
"rates": ["^TNX", "^FVX"], # 10-year and 5-year Treasury yields
} START_DATE =
"
2023-01-01"
END_DATE = datetime.today().strftime("%Y-%m-%d")
OUTPUT_DIR = "data"
def fetch_and_save():
  os.makedirs(OUTPUT_DIR, exist_ok=True)
  for asset_class, tickers in TICKERS.items():
    for ticker in tickers:
      print(f"Fetching {asset_class}: {ticker}")
      df = yf.download(ticker, start=START_DATE, end=END_DATE, progress=False)
    if df.empty:
        print(f" WARNING: no data for {ticker}")
        continue
    safe_name = ticker.replace("=", "_").replace("^", "")
    df.to_csv(f"{OUTPUT_DIR}/{asset_class}_{safe_name}.csv")
    print(f" Saved {len(df)} rows")
if __name__ == "__main__":
fetch_and_save()
