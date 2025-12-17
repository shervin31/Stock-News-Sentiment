# 📈 Stock News Sentiment: Business Insights from Financial News

## 📖 Project Overview
This project addresses a key business challenge in the financial sector: understanding market sentiment quickly and accurately to inform investment decisions. By analyzing recent news articles about companies or stocks, our solution provides actionable insights into market perception, helping traders, analysts, and financial managers make data-driven decisions.

The system scrapes financial news, summarizes articles using a transformer-based NLP model, and performs sentiment analysis to generate a concise overview of positive, neutral, and negative market sentiment.

---

## 🎯 Business Objective
Financial markets are highly sensitive to news and public perception. Blindly analyzing headlines manually is time-consuming, prone to bias, and often too slow to act on. This project aims to:

- Quickly quantify market sentiment for specific stocks or sectors  
- Identify shifts in public perception before they are reflected in stock prices  
- Enable data-driven investment or risk management strategies  

By leveraging automated news sentiment analysis, financial professionals can focus on **high-impact decisions** rather than manually tracking news flow.

---

## 📊 Data Sources
The system leverages publicly available financial news articles from multiple sources. Users can input a keyword (e.g., a company or sector) and specify the time window for analysis.

- **Input:** Keyword and number of days to look back  
- **Output:** Summarized news articles with sentiment scores  

The result is both **a detailed DataFrame of articles** and **an aggregated sentiment score**, reflecting overall market perception.

---

## 🛠️ Technical Approach
The project follows a streamlined workflow designed for business users:

1. **Data Collection**
   - Scrape recent news articles from financial websites using Python's `requests` and `BeautifulSoup`.

2. **Text Summarization**
   - Apply a pre-trained transformer NLP model to generate concise summaries of each article, reducing noise and focusing on key information.

3. **Sentiment Analysis**
   - Compute sentiment scores (positive, neutral, negative) for each article.
   - Aggregate scores to produce an overall sentiment metric for the keyword.

4. **Output**
   - Display results in a pandas DataFrame for detailed analysis.
   - Print the **average sentiment score** for quick decision-making.

---

## 🏆 Business Insights
Using this tool, businesses can:

- **Detect Early Market Trends:** Quickly identify positive or negative sentiment swings before they are reflected in stock movements.  
- **Focus on High-Impact News:** Summaries highlight the most relevant content, saving analysts hours of manual reading.  
- **Make Data-Driven Decisions:** Aggregate sentiment scores provide a quantitative measure of market perception, supporting investment or risk strategies.  

---

## 💡 Actionable Recommendations
1. **Integrate into Investment Workflow:** Use sentiment scores alongside other financial indicators to guide portfolio adjustments.  
2. **Monitor Competitors:** Track sentiment for competing firms or sectors to anticipate market shifts.  
3. **Automate Regular Reports:** Generate daily or weekly sentiment summaries to keep executives and traders informed.  
4. **Expand Coverage:** Include additional news sources and sectors for broader market intelligence.  

---

## 🧩 Project Structure

```text
├── main.py            # User input and program execution
├── functions.py       # News scraping, summarization, and sentiment logic
├── README.md          # Project documentation
