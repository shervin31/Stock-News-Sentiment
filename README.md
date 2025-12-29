# StockNewsSentiment 📈

A Python-based NLP tool that analyzes **recent financial news sentiment for stocks** using Yahoo Finance data and a domain-specific language model (FinBERT).

The system fetches live news articles, applies financial sentiment analysis, and aggregates results into a clear, interpretable sentiment signal.

---

## Features

- 📰 Fetches real-time financial news from **Yahoo Finance** (no API key required)
- 🤖 Uses **FinBERT**, a finance-tuned NLP model, for sentiment classification
- 📊 Aggregates article-level sentiment into a single stock sentiment score
- ⏳ Filters articles by a customizable lookback window (days)
- 🧠 Clean, minimal CLI output focused on signal, not noise

---

## Installation

### Clone the repository
```bash
git clone https://github.com/shervin31/StockNewsSentiment.git
cd StockNewsSentiment
```

### Install dependencies
```bash
pip install yfinance transformers pandas torch
```
### Usage
Run the main script:
```bash
python main.py
```

### Example interaction
```bash
Enter a stock ticker (e.g., AAPL, TSLA): TSLA
Enter number of days to look back: 5

===== Sentiment Summary =====
Ticker: TSLA
Articles analyzed: 10
Negative : 6
Neutral  : 3
Positive : 1

Average sentiment score: -0.68
```



