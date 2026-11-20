import pandas as pd
from pathlib import Path
from transformers import pipeline

INPUT_FILE = Path("data/raw/news/stock_news.csv")
OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "news_sentiment.csv"

print("Loading FinBERT model...")

model = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)

df = pd.read_csv(INPUT_FILE)

if "Title" not in df.columns:
    raise ValueError("Title column missing from news CSV")

texts = df["Title"].fillna("").astype(str).tolist()

print("Analyzing", len(texts), "news articles...")

results = model(
    texts,
    batch_size=16,
    truncation=True,
    max_length=512
)

labels = []
scores = []
confidence = []

for result in results:
    label = result["label"].capitalize()
    score = float(result["score"])

    labels.append(label)
    confidence.append(score)

    if label == "Positive":
        scores.append(score)
    elif label == "Negative":
        scores.append(-score)
    else:
        scores.append(0.0)

df["Sentiment"] = labels
df["Sentiment_Score"] = scores
df["Confidence"] = confidence

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)

print("\nFinBERT sentiment analysis completed!")

print("\nSentiment distribution:")
print(df["Sentiment"].value_counts())

print("\nCompany-wise sentiment:")
print(df.groupby(["Stock", "Sentiment"]).size())

print("\nAverage confidence:", round(df["Confidence"].mean(), 4))

print("\nSaved:", OUTPUT_FILE)
