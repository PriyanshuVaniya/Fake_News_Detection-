import requests
import pandas as pd
from config import NEWS_API_KEY, NEWS_API_URL

def fetch_news_data(query="news", country="us", page_size=100):
    """Fetches news articles from NewsAPI."""
    params = {
        "q": query,
        "country": country,
        "apiKey": NEWS_API_KEY,
        "pageSize": page_size
    }

    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])

        news_list = []
        for article in articles:
            news_list.append({
                "title": article["title"],
                "source": article["source"]["name"],
                "description": article["description"],
                "url": article["url"],
                "published_at": article["publishedAt"]
            })

        return news_list
    else:
        print("Error fetching data:", response.status_code)
        return []

def save_to_csv(news_list, filename="data/news_data.csv"):
    """Saves news data to a CSV file."""
    df = pd.DataFrame(news_list)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    news_data = fetch_news_data()
    if news_data:
        save_to_csv(news_data)
