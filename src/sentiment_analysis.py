from transformers import pipeline
import json

def analyze_sentiment():
    print("Analyzing sentiments...")
    sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    with open('output/summaries.json') as f:
        summaries = json.load(f)
    
    sentiments = []
    for summary in summaries:
        short_sentiment = sentiment_model(summary['short_summary'])[0]
        long_sentiment = sentiment_model(summary['long_summary'])[0]
        sentiments.append(
            {
            "url": summary['url'],
            "title": summary['title'],
            "short_summary_sentiment": short_sentiment,
            "long_summary_sentiment": long_sentiment
        }
            )

    with open('output/sentiment_scores.json', 'w') as f:
        json.dump(sentiments, f, indent=2)
        
    print(f"Analyzed sentiments for {len(sentiments)} articles.")

if __name__ == "__main__":
    analyze_sentiment()
