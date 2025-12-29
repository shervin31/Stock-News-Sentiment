import yfinance as yf
t = yf.Ticker("AAPL")
print("keys:", t.get_info().keys() if hasattr(t, "get_info") else "no get_info")
print("news:", t.news)
