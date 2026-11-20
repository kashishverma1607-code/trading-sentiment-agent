import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Trading Sentiment Agent", page_icon="📈", layout="wide")

st.title("📈 Trading Sentiment Agent")
st.caption("Hong Kong Stock Market Intelligence Dashboard")

report_file = Path("reports/combined_trading_report.csv")
news_file = Path("data/processed/news_sentiment.csv")

if not report_file.exists() or not news_file.exists():
    st.error("Required files missing")
    st.stop()

df = pd.read_csv(report_file)
news = pd.read_csv(news_file)

st.subheader("Stock Market Overview")

c1, c2, c3 = st.columns(3)
c1.metric("Stocks Tracked", len(df))
c2.metric("Total News Articles", int(df["Total_News"].sum()))
c3.metric("Average News Sentiment", round(news["Sentiment_Score"].mean(), 3))

st.divider()

st.subheader("Individual Stock Analysis")

selected_stock = st.selectbox(
    "Select a Hong Kong Stock",
    sorted(df["Stock"].unique())
)

stock_data = df[df["Stock"] == selected_stock].iloc[0]
stock_news = news[news["Stock"] == selected_stock].copy()

c1, c2, c3 = st.columns(3)
c1.metric("RSI", round(stock_data["RSI"], 2))
c2.metric("MACD", round(stock_data["MACD"], 4))
c3.metric("Trading Signal", stock_data["Trading_Signal"])

st.metric("Average News Sentiment", round(news[news["Stock"] == selected_stock]["Sentiment_Score"].mean(), 4))

st.subheader("News Sentiment Distribution")

counts = stock_news["Sentiment"].value_counts().reindex(
    ["Positive", "Neutral", "Negative"], fill_value=0
)
st.bar_chart(counts)

st.subheader("Latest News Headlines")

for _, article in stock_news.head(10).iterrows():
    st.write("**" + str(article["Title"]) + "**")
    st.caption(str(article["Sentiment"]) + " | " + str(article["Published"]))

    if pd.notna(article["Link"]):
        st.markdown("[Read article](" + str(article["Link"]) + ")")

    st.divider()

st.success("Individual stock analysis loaded successfully!")

st.divider()
st.title("🤖 AI Trading Recommendations")

ai_file = Path("reports/ai_recommendations.csv")

if ai_file.exists():
    ai_df = pd.read_csv(ai_file)
    st.dataframe(ai_df, width="stretch")
    st.success("AI recommendations loaded successfully!")
else:
    st.warning("Run recommendation_engine first.")


st.divider()
st.title("🧠 FinBERT Sentiment Analysis")

if "Confidence" in news.columns:

    st.subheader("Model Confidence")

    avg_confidence = news["Confidence"].mean()

    st.metric(
        "Average FinBERT Confidence",
        f"{avg_confidence:.2%}"
    )

    st.subheader("Overall Sentiment Distribution")

    sentiment_counts = news["Sentiment"].value_counts()

    st.bar_chart(sentiment_counts)

    st.subheader("Selected Stock Confidence")

    selected_news = news[news["Stock"] == selected_stock]

    if not selected_news.empty:
        stock_confidence = selected_news["Confidence"].mean()

        st.metric(
            "Average Confidence",
            f"{stock_confidence:.2%}"
        )
else:
    st.warning("Run FinBERT sentiment analyzer first.")



