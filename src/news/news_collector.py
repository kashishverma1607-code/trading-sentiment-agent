import feedparser
import pandas as pd
from pathlib import Path
from urllib.parse import quote

STOCKS = {
    "Tencent": "Tencent stock Hong Kong",
    "Alibaba": "Alibaba stock Hong Kong",
    "Meituan": "Meituan stock Hong Kong",
    "HSBC": "HSBC stock",
    "China Mobile": "China Mobile stock Hong Kong"
}

OUTPUT_DIR = Path("data/raw/news")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

all_news = []

for stock, query in STOCKS.items():

    print(f"\nCollecting news for {stock}...")

    url = (
        "https://news.google.com/rss/search?q="
        + quote(query)
        + "&hl=en-HK&gl=HK&ceid=HK:en"
    )

    try:
        feed = feedparser.parse(url)

        for entry in feed.entries:

            all_news.append({
                "Stock": stock,
                "Title": entry.get("title", ""),
                "Link": entry.get("link", ""),
                "Published": entry.get("published", ""),
                "Source": entry.get("source", {}).get("title", "")
            })

        print("Articles found:", len(feed.entries))

    except Exception as error:
        print("Error:", error)

if all_news:
    df = pd.DataFrame(all_news)
    df = df.drop_duplicates(subset=["Link"])

    output_file = OUTPUT_DIR / "stock_news.csv"
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print("\nNews collection completed!")
    print("Total articles:", len(df))
    print("Saved:", output_file)
else:
    print("\nNo news collected. Check internet connection.")
