from transformers import pipeline

print("Loading FinBERT model...")

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)

test_news = [
    "Alibaba shares plunge after disappointing results",
    "Tencent reports strong revenue growth",
    "China Mobile shares remain unchanged"
]

results = sentiment_pipeline(test_news)

print("\nFinBERT Results:")

for news, result in zip(test_news, results):
    print("\nNews:", news)
    print("Sentiment:", result["label"])
    print("Confidence:", round(result["score"], 4))
