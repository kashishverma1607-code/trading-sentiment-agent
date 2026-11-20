import pandas as pd
from pathlib import Path

folder = Path("data/raw/prices")

for file in folder.glob("*.csv"):
    df = pd.read_csv(file)

    print("\nFile:", file.name)
    print("Rows:", len(df))
    print("Columns:", list(df.columns))

    if "Close" in df.columns:
        print("Latest closing price:", df["Close"].iloc[-1])
