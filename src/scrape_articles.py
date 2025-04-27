import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_articles(max_articles=5):
    base_url = "https://www.coindesk.com/markets/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    os.makedirs('data', exist_ok=True)

    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    seen_urls = set()
    count = 0

    for link in soup.find_all('a', href=True):
        href = link['href']

        if href.startswith("/markets/"):
            full_url = "https://www.coindesk.com" + href.split("?")[0]

            if full_url in seen_urls:
                continue  # Skip duplicates

            seen_urls.add(full_url)

            article_data = scrape_single_article(full_url, headers)
            if article_data:
                articles.append(article_data)
                count += 1

            if count >= max_articles:
                break

    with open('data/articles.json', 'w') as f:
        json.dump(articles, f, indent=2)

    print(f"Scraped {len(articles)} unique articles from CoinDesk Markets.")

def scrape_single_article(url, headers):
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get title
        title_tag = soup.find('h1')
        title = title_tag.get_text(strip=True) if title_tag else "No Title Found"

        # Get article body
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])

        if len(article_text) < 200:
            return None

        return {
            "url": url,
            "title": title,
            "text": article_text
        }

    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        return None

if __name__ == "__main__":
    scrape_articles(max_articles=5)
