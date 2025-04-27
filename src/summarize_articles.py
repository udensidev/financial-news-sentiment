from transformers import pipeline
import json

def summarize_articles():
    print("Summarizing articles...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    with open('data/articles.json') as f:
        articles = json.load(f)
    
    summaries = []
    for article in articles:
        short = summarizer(article['text'], max_length=50, min_length=25, do_sample=False)[0]['summary_text']
        long = summarizer(article['text'], max_length=200, min_length=100, do_sample=False)[0]['summary_text']
        summaries.append({
            "url": article['url'],
            "title": article['title'],
            "short_summary": short, 
            "long_summary": long})
    
    with open('output/summaries.json', 'w') as f:
        json.dump(summaries, f, indent=2)
        
    print(f"Summarized {len(summaries)} articles.")
if __name__ == "__main__":
    summarize_articles()
