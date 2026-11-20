# Hong Kong Stock Market Intelligence & Trading Sentiment Agent

## Project Overview
This project is a Python-based stock market intelligence and trading sentiment analysis system. It combines financial news analysis, AI-based sentiment detection and technical indicators to generate trading insights.

## Project Objectives
- Analyze financial news sentiment.
- Monitor stock market trends.
- Generate BUY, SELL and HOLD signals.
- Display market insights through an interactive dashboard.
- Send automated Telegram alerts.

## Key Features

### 1. Stock Market Data Collection
- Collect and process historical stock price data.
- Store stock data in CSV files.
- Track selected Hong Kong stocks.

### 2. Financial News Analysis
- Collect financial news related to stocks.
- Process and analyze news headlines.
- Store collected news for further analysis.

### 3. FinBERT Sentiment Analysis
- Use FinBERT for financial text sentiment analysis.
- Classify news as Positive, Negative or Neutral.
- Calculate sentiment scores and confidence levels.

### 4. Technical Analysis
- RSI (Relative Strength Index).
- MACD (Moving Average Convergence Divergence).
- Analyze market trends and momentum.

### 5. Trading Signal Generation
- Generate BUY, SELL and HOLD signals.
- Combine sentiment and technical indicators.
- Generate stock-wise trading recommendations.

### 6. Interactive Dashboard
- Built using Streamlit.
- Display stocks tracked and total news articles.
- Show average market sentiment.
- Display stock-wise sentiment and latest headlines.
- Show RSI, MACD and trading signals.
- Display FinBERT confidence scores.

### 7. Telegram Notifications
- Integrate Telegram Bot API.
- Send automated trading alerts and notifications.

### 8. Automation and Reports
- Automated execution using Python scripts.
- Generate trading reports and recommendations.
- Save processed data and reports in CSV format.
- Support scheduled execution using Windows Task Scheduler.

## Technologies Used
- Python
- Streamlit
- FinBERT
- Pandas
- NumPy
- Telegram Bot API
- Technical Indicators
- CSV
- Windows Task Scheduler

## Project Structure
- data/: Raw and processed stock market data.
- src/analysis/: Data analysis modules.
- src/dashboard/: Streamlit dashboard.
- src/ingestion/: Data collection modules.
- src/news/: News collection and sentiment analysis.
- src/notifications/: Telegram alerts.
- src/processing/: Indicators and trading signals.
- src/reports/: Report generation.
- reports/: Generated reports and charts.
- tests/: Project testing files.

## Installation and Execution

1. Clone the repository:

   git clone https://github.com/kashishverma1607-code/trading-sentiment-agent.git

2. Open the project directory:

   cd trading-sentiment-agent

3. Create a virtual environment:

   python -m venv venv

4. Activate the environment:

   .\venv\Scripts\Activate.ps1

5. Install dependencies:

   pip install -r requirements.txt

6. Configure required API credentials in a local .env file. Never upload real API keys or tokens to GitHub.

7. Run the dashboard:

   python -m streamlit run src/dashboard/app.py

## Future Scope
- Real-time market data integration.
- Advanced stock prediction models.
- Portfolio tracking.
- Additional technical indicators.
- Cloud deployment and automation.

## Disclaimer
This project is developed for educational and research purposes only. Trading signals are not financial advice. Users should conduct their own research before making investment decisions.

## Author
Kashish Verma

## GitHub Repository
https://github.com/kashishverma1607-code/trading-sentiment-agent
