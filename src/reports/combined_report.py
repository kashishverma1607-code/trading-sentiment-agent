import pandas as pd
from pathlib import Path

NEWS_FILE = Path("data/processed/news_sentiment.csv")
SIGNAL_FILE = Path("data/processed/trading_signals.csv")

OUTPUT_DIR = Path("reports")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

news = pd.read_csv(NEWS_FILE)
signals = pd.read_csv(SIGNAL_FILE)

summary = news.groupby("Stock").agg(
    Total_News=("Title", "count"),
    Average_Sentiment=("Sentiment_Score", "mean")
).reset_index()

sentiment_counts = pd.crosstab(
    news["Stock"], news["Sentiment"]
).reset_index()

summary = summary.merge(
    sentiment_counts,
    on="Stock",
    how="left"
)

combined = signals.copy()

ticker_map = {
    "0005_HK": "HSBC",
    "0700_HK": "Tencent",
    "0941_HK": "China Mobile",
    "3690_HK": "Meituan",
    "9988_HK": "Alibaba"
}

combined["Stock"] = combined["Stock"].map(ticker_map).fillna(
    combined["Stock"]
)

final_report = combined.merge(
    summary,
    on="Stock",
    how="left"
)

output = OUTPUT_DIR / "combined_trading_report.csv"
final_report.to_csv(output, index=False)

print("\nCombined report generated!")
print(final_report.to_string(index=False))
print("\nSaved:", output)
