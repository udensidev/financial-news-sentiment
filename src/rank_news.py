import json
from tabulate import tabulate
def rank_articles():
    print("Getting you your most relevant articles...")
    with open('output/sentiment_scores.json') as f:
        sentiments = json.load(f)
    
    table = []
    
    for article in sentiments:
        title = article['title']
        short_score = article['short_summary_sentiment']['score']
        long_score = article['long_summary_sentiment']['score']
        table.append([title, short_score, long_score])

    # Sort by short summary sentiment score descending
    table = sorted(table, key=lambda x: x[1], reverse=True)

    # Define table headers
    headers = ["Article", "Short Sentiment Score", "Long Sentiment Score"]

    # Print nicely using tabulate
    print(tabulate(table, headers=headers, tablefmt="pretty"))
if __name__ == "__main__":
    rank_articles()

