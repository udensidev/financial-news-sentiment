from scrape_articles import scrape_articles
from summarize_articles import summarize_articles
from sentiment_analysis import analyze_sentiment
from rank_news import rank_articles

if __name__ == "__main__":
    scrape_articles()
    summarize_articles()
    analyze_sentiment()
    rank_articles()
