from transformers import pipeline
import requests
from datetime import datetime, timedelta
import pandas as pd

def fetch_news_articles(keyword, days_back):
    API_KEY = "59b56e303c1246efb26e118156b60af0"
    pipe = pipeline("text-classification", model="ProsusAI/finbert")
    
    date_from = (datetime.now() - timedelta(days=days_back)).strftime('%Y-%m-%d')
    url = (
        'https://newsapi.org/v2/everything?'
        f'q={keyword}&'
        f'from={date_from}&'
        'sortBy=popularity&'
        f'apiKey={API_KEY}'
    )

    response = requests.get(url)

    return response, pipe


def summarize_articles(response, pipe, keyword):

    articles = response.json()['articles']
    articles = [
        article for article in articles
        if keyword.lower() in (article.get('title') or '').lower() 
        or keyword.lower() in (article.get('description') or '').lower()
    ]
    
    total_score = 0
    num_articles = 0
    data_list = []
 
    for i, article in enumerate(articles):

        sentiment = pipe(article['content'])[0]
        article_dict = {
            "Title": article.get('title'),
            "Link": article.get('url'),
            "Published": article.get('publishedAt'),
            "Label": sentiment['label'],
            "Sentiment": sentiment['score']
        }

        data_list.append(article_dict)

        if sentiment['label'] == 'positive': 
            total_score += sentiment['score']
            num_articles += 1
        elif sentiment['label'] == 'negative':
            total_score -= sentiment['score']
            num_articles += 1

    results_df = pd.DataFrame(data_list)

    average_score = total_score / num_articles if num_articles > 0 else 0

    return results_df, average_score