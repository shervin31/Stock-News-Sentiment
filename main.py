from functions import fetch_news_articles, summarize_articles 
from IPython.display import display

def main():
    keyword = input("Enter a stock/company to search news for: ").strip().lower()
    days = int(input("Enter number of days to look back: ").strip())


    response, pipe = fetch_news_articles(keyword, days)
    df, avg_score = summarize_articles(response, pipe, keyword)

    print(f"Average sentiment score: {avg_score:.2f}")


if __name__ == "__main__":
    main()