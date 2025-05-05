from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import json

def analyze_sentiment():
    """Analyze the sentiment of article summaries using a pre-trained model."""
    print("Analyzing sentiments...")
    
    model_name = "ProsusAI/finbert"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    sentiment_model = pipeline("sentiment-analysis",model=model, tokenizer=tokenizer)
    
    with open('output/summaries.json') as f:
        summaries = json.load(f)
    
    sentiments = []
    label_map = {"positive": 1, "neutral": 1, "negative": -1}
    
    for summary in summaries:
        # Analyze sentiment for short and long summaries
        short_sentiment_result = sentiment_model(summary['short_summary'])[0]
        short_sentiment_score = label_map[short_sentiment_result['label']] * short_sentiment_result['score']
        
        long_sentiment_result = sentiment_model(summary['long_summary'])[0]
        long_sentiment_score = label_map[long_sentiment_result['label']] * long_sentiment_result['score']
        
        sentiments.append(
            {
            "url": summary['url'],
            "title": summary['title'],
            "short_summary_sentiment": {
                "label": short_sentiment_result['label'],
                "score": short_sentiment_score
            },
            "long_summary_sentiment": {
                "label": long_sentiment_result['label'],
                "score": long_sentiment_score
            }
        }
            )

    with open('output/sentiment_scores.json', 'w') as f:
        json.dump(sentiments, f, indent=2)
        
    print(f"Analyzed sentiments for {len(sentiments)} articles.")

if __name__ == "__main__":
    analyze_sentiment()
