import yfinance as yf
import pandas as pd
from pathlib import Path

TICKERS = {
    "Tencent": "0700.HK",
    "Alibaba": "9988.HK",
    "Meituan": "3690.HK",
    "HSBC": "0005.HK",
    "China_Mobile": "0941.HK"
}

OUTPUT_DIR = Path("data/raw/prices")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

all_data = []

for name, ticker in TICKERS.items():

    print(f"\nDownloading {name} ({ticker})...")

    try:
        data = yf.download(
            ticker,
            period="1y",
            interval="1d",
            auto_adjust=False,
            progress=False
        )

        if data.empty:
            print(f"No data received for {ticker}")
            continue

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        data = data.reset_index()
        data["Ticker"] = ticker
        data["Asset"] = name

        output_file = OUTPUT_DIR / f"{ticker.replace('.', '_')}.csv"
        data.to_csv(output_file, index=False)

        all_data.append(data)

        print(f"Saved: {output_file}")
        print(f"Rows: {len(data)}")

    except Exception as error:
        print(f"Download failed for {ticker}: {error}")

if all_data:
    combined = pd.concat(all_data, ignore_index=True)
    combined.to_csv(
        OUTPUT_DIR / "all_hk_stocks.csv",
        index=False
    )

    print("\nAll stocks downloaded successfully!")
    print("Total rows:", len(combined))
    print("Output folder:", OUTPUT_DIR)
else:
    print("\nNo stock data downloaded. Check internet connection.")

