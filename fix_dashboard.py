from pathlib import Path

path = Path("src/dashboard/app.py")
code = path.read_text(encoding="utf-8-sig")

start = code.find('st.title("FinBERT Sentiment Analysis")')

if start == -1:
    raise SystemExit("FinBERT section not found. File unchanged.")

end_marker = 'st.warning("Run FinBERT sentiment analyzer first.")'
end = code.find(end_marker, start)

if end == -1:
    raise SystemExit("FinBERT section end not found. File unchanged.")

end += len(end_marker)

replacement = '''st.divider()

st.title("FinBERT Sentiment Analysis")

if "Confidence" in news.columns:

    st.subheader("Model Confidence")

    avg_confidence = news["Confidence"].mean()

    st.metric(
        "Average FinBERT Confidence",
        f"{avg_confidence:.2%}"
    )

    st.subheader("Overall Sentiment Distribution")

    sentiment_counts = (
        news["Sentiment"]
        .value_counts()
        .reindex(["Positive", "Neutral", "Negative"], fill_value=0)
    )

    st.bar_chart(sentiment_counts)

    st.subheader("Selected Stock Confidence")

    selected_news = news[news["Stock"] == selected_stock]

    if not selected_news.empty:
        stock_confidence = selected_news["Confidence"].mean()
        st.metric("Average Confidence", f"{stock_confidence:.2%}")
    else:
        st.info("No confidence data available for this stock.")

else:
    st.warning("Run FinBERT sentiment analyzer first.")'''

backup = path.with_suffix(".py.bak")
backup.write_text(code, encoding="utf-8")

path.write_text(code[:start] + replacement + code[end:], encoding="utf-8")

print("FinBERT section updated successfully!")
print("Backup saved:", backup)
