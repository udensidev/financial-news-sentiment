# 📰 News Sentiment Analysis Project

This project scrapes real-time finance and crypto articles from [CoinDesk](https://www.coindesk.com/markets/), summarizes the articles using free Hugging Face fine-tuned language models, analyzes their sentiment, and ranks the articles based on their estimated relevance.

---

## 📜 Project Overview

The pipeline:
- Scrapes the latest articles from CoinDesk.
- Extracts **Title**, **Publish Date**, and **Full Text**.
- Summarizes each article using a Hugging Face model (`facebook/bart-large-cnn`).
- Analyzes the sentiment of short and long summaries separately (`cardiffnlp/twitter-roberta-base-sentiment`).
- Ranks the articles based on sentiment scores.
- Displays results neatly as a terminal table using `tabulate`.

---

## 🏗️ Folder Structure

```bash
financial-news-sentiment/
├── data/                  # Scraped raw articles (JSON format)
├── outputs/               # Summaries and sentiment scores
├── src/                   # All source Python scripts
│   ├── scrape_articles.py
│   ├── summarize_articles.py
│   ├── sentiment_analysis.py
│   ├── rank_news.py
│   └── main.py             # Master pipeline script
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── launch.sh               # Launch script   
```


---

## 🛠️ Setup Instructions

1. Clone or download this repository.

2. Run the full end-to-end pipeline:

```bash
bash launch.sh
```

✅ This will automatically:
- Check for and install Python dependencies
- Scrape new articles
- Summarize them
- Analyze sentiment
- Rank and display articles

---

## 📚 Technologies Used

- Python 3.10+
- `requests` and `BeautifulSoup` (web scraping)
- Hugging Face `transformers` (`facebook/bart-large-cnn` for summarization, `ProsusAI/finbert` for sentiment anlysis)
- `tabulate` (clean terminal table output)

---

## 📊 Example Terminal Output

```bash
+-----------------------------------------------------+----------------------+-----------------------+
|                      Article                        | Short Sentiment Score | Long Sentiment Score |
+-----------------------------------------------------+----------------------+-----------------------+
|                     Article 1                       |         0.92          |         0.85         |
|                     Article 2                       |         0.81          |         0.75         |
+-----------------------------------------------------+----------------------+-----------------------+
```

---

## 🚀 Features

- Real-time scraping from CoinDesk
- Clean metadata extraction
- Abstractive article summarization
- Sentiment scoring (short vs long summary comparison)
- Automatic article ranking based on sentiment strength
- Professional terminal table display

---

## 📣 Attribution

- Live crypto/finance news is sourced from [CoinDesk](https://www.coindesk.com/markets/).
- Summarization and sentiment models are sourced from Hugging Face open-source repositories.


