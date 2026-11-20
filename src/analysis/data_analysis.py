import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path


DATA_DIR = Path("data/raw/prices")
REPORT_DIR = Path("reports/charts")

REPORT_DIR.mkdir(parents=True, exist_ok=True)


def analyze_stock(filepath):

    print("\n" + "=" * 55)
    print(f"ANALYSING: {filepath.name}")
    print("=" * 55)

    df = pd.read_csv(filepath)

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Remove duplicates
    df = df.drop_duplicates(subset=["date"])

    # Sort by date
    df = df.sort_values("date")

    # Check missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Handle missing numeric values
    numeric_columns = [
        "open", "high", "low", "close", "volume"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove rows without closing price
    df = df.dropna(subset=["close"])

    # Calculate daily returns
    df["daily_return"] = df["close"].pct_change() * 100

    # Save cleaned data
    output_path = Path("data/processed") / filepath.name
    df.to_csv(output_path, index=False)

    # Statistics
    print("\nBasic statistics:")
    print(df[["open", "high", "low", "close", "volume"]].describe())

    print("\nTotal records:", len(df))
    print("Average daily return:", df["daily_return"].mean())

    # Plot closing price
    plt.figure(figsize=(12, 5))

    plt.plot(
        df["date"],
        df["close"],
        label="Closing Price",
        color="blue"
    )

    plt.title(filepath.stem + " - Historical Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    chart_path = REPORT_DIR / f"{filepath.stem}.png"

    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    print("\nCleaned data saved:", output_path)
    print("Chart saved:", chart_path)


def main():

    files = list(DATA_DIR.glob("*.csv"))

    print("TOTAL STOCK FILES:", len(files))

    for filepath in files:
        analyze_stock(filepath)

    print("\nDATA ANALYSIS COMPLETED!")


if __name__ == "__main__":
    main()
