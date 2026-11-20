from pathlib import Path

path = Path("src/dashboard/app.py")
lines = path.read_text(encoding="utf-8-sig").splitlines()

# Backup
Path("src/dashboard/app.py.backup").write_text(
    "\n".join(lines) + "\n",
    encoding="utf-8"
)

# Replace broken section from line 84 onwards
new_section = '''
st.divider()

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
    st.warning("Run FinBERT sentiment analyzer first.")
'''.strip()

path.write_text(
    "\n".join(lines[:83]) + "\n\n" + new_section + "\n",
    encoding="utf-8"
)

print("FinBERT section repaired!")
print("Backup created successfully!")
