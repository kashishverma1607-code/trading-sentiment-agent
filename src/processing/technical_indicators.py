import pandas as pd
from pathlib import Path
from ta.momentum import RSIIndicator
from ta.trend import MACD

INPUT_DIR = Path("data/raw/prices")
OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for file in INPUT_DIR.glob("*.csv"):

    if file.name == "all_hk_stocks.csv":
        continue

    df = pd.read_csv(file)

    if df.empty or "Close" not in df.columns:
        print("Skipping:", file.name)
        continue

    close = pd.to_numeric(df["Close"], errors="coerce")

    df["RSI_14"] = RSIIndicator(close, window=14).rsi()

    macd = MACD(close)
    df["MACD"] = macd.macd()
    df["MACD_Signal"] = macd.macd_signal()
    df["MACD_Diff"] = macd.macd_diff()

    df.to_csv(OUTPUT_DIR / file.name, index=False)

    print("Processed:", file.name)

print("\nTechnical indicators completed!")
