import subprocess
import sys
from datetime import datetime

steps = [
    "src.news.news_collector",
    "src.news.sentiment_analyzer",
    "src.processing.technical_indicators",
    "src.processing.signal_generator",
    "src.reports.combined_report",
    "src.processing.recommendation_engine",
    "src.notifications.trading_alerts",
]

print("TRADING SENTIMENT AGENT")
print("Starting automated pipeline...")
print("Time:", datetime.now())

for step in steps:
    print(f"\nRunning: {step}")

    result = subprocess.run(
        [sys.executable, "-m", step]
    )

    if result.returncode != 0:
        print(f"\nFAILED: {step}")
        sys.exit(result.returncode)

print("\nAll pipeline steps completed!")
print("Telegram alerts sent successfully!")
