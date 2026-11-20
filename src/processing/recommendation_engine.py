import pandas as pd
from pathlib import Path

SIGNAL_FILE = Path("data/processed/trading_signals.csv")
NEWS_FILE = Path("data/processed/news_sentiment.csv")

OUTPUT_DIR = Path("reports")
OUTPUT_DIR.mkdir(exist_ok=True)

if not SIGNAL_FILE.exists() or not NEWS_FILE.exists():
    raise FileNotFoundError("Required input files are missing")

signals = pd.read_csv(SIGNAL_FILE)
news = pd.read_csv(NEWS_FILE)

ticker_map = {
    "0005_HK": "HSBC",
    "0700_HK": "Tencent",
    "0941_HK": "China Mobile",
    "3690_HK": "Meituan",
    "9988_HK": "Alibaba"
}

signals["Stock"] = signals["Stock"].map(ticker_map).fillna(
    signals["Stock"]
)

news_summary = news.groupby("Stock").agg(
    Average_Sentiment=("Sentiment_Score", "mean"),
    Positive_News=("Sentiment", lambda x: (x == "Positive").sum()),
    Negative_News=("Sentiment", lambda x: (x == "Negative").sum()),
    Total_News=("Sentiment", "count")
).reset_index()

df = signals.merge(news_summary, on="Stock", how="left")

def generate_recommendation(row):
    score = 0

    if row["RSI"] < 30:
        score += 1
    elif row["RSI"] > 70:
        score -= 1

    if row["MACD"] > row["MACD_Signal"]:
        score += 1
    else:
        score -= 1

    if row["Average_Sentiment"] > 0.05:
        score += 1
    elif row["Average_Sentiment"] < -0.05:
        score -= 1

    if score >= 2:
        return "BUY"
    elif score <= -2:
        return "SELL"
    return "HOLD"

df["AI_Recommendation"] = df.apply(
    generate_recommendation, axis=1
)

output = OUTPUT_DIR / "ai_recommendations.csv"
df.to_csv(output, index=False)

print("\nAI Recommendation Engine completed!")
print(df[[
    "Stock",
    "RSI",
    "Average_Sentiment",
    "AI_Recommendation"
]].to_string(index=False))

print("\nSaved:", output)
