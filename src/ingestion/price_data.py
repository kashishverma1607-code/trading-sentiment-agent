import yfinance as yf
import pandas as pd
from pathlib import Path

from src.config import ASSETS


OUTPUT_DIR = Path("data/raw/prices")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def download_stock_data(ticker, exchange):

    print(f"\nDownloading: {ticker}")

    try:
        data = yf.download(
            ticker,
            period="2y",
            interval="1d",
            auto_adjust=True,
            progress=False
        )

        if data.empty:
            print(f"No data found for {ticker}")
            return False

        # Handle multi-level columns if returned by Yahoo Finance
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        data = data.reset_index()

        # Standardize column names
        data.columns = [str(col).lower().replace(" ", "_") for col in data.columns]

        required_columns = [
            "date", "open", "high", "low", "close", "volume"
        ]

        if not all(col in data.columns for col in required_columns):
            print(f"Required columns missing for {ticker}")
            return False

        data = data[required_columns]

        # Save data
        filename = f"{exchange}_{ticker.replace('.', '_')}.csv"
        filepath = OUTPUT_DIR / filename

        data.to_csv(filepath, index=False)

        print(f"Saved: {filepath}")
        print(f"Records downloaded: {len(data)}")

        return True

    except Exception as error:
        print(f"Error downloading {ticker}: {error}")
        return False


def main():

    print("=" * 55)
    print("STOCK PRICE DATA COLLECTION")
    print("=" * 55)

    successful = 0
    failed = 0

    for exchange, stocks in ASSETS.items():

        print(f"\nExchange: {exchange}")

        for stock in stocks:

            result = download_stock_data(
                stock["ticker"],
                exchange
            )

            if result:
                successful += 1
            else:
                failed += 1

    print("\n" + "=" * 55)
    print("DATA COLLECTION COMPLETED")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print("=" * 55)


if __name__ == "__main__":
    main()
