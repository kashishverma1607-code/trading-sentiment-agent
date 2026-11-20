import pandas as pd
from pathlib import Path

INPUT_DIR = Path("data/processed")
OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

results = []

for file in INPUT_DIR.glob("*.csv"):

    if file.name == "all_hk_stocks.csv":
        continue

    df = pd.read_csv(file)

    required = ["RSI_14", "MACD", "MACD_Signal"]

    if df.empty or not all(c in df.columns for c in required):
        print("Skipping:", file.name)
        continue

    latest = df.dropna(subset=required).iloc[-1]

    rsi = latest["RSI_14"]
    macd = latest["MACD"]
    signal = latest["MACD_Signal"]

    if rsi < 30 and macd > signal:
        decision = "BUY"
    elif rsi > 70 and macd < signal:
        decision = "SELL"
    else:
        decision = "HOLD"

    results.append({
        "Stock": file.stem,
        "RSI": round(rsi, 2),
        "MACD": round(macd, 4),
        "MACD_Signal": round(signal, 4),
        "Trading_Signal": decision
    })

    print(file.stem, ":", decision)

if results:
    output = pd.DataFrame(results)
    output.to_csv(OUTPUT_DIR / "trading_signals.csv", index=False)
    print("\nTrading signals saved successfully!")
else:
    print("\nNo valid data found. Check previous steps.")
