import requests
from crewai.tools import tool
import os

@tool("Stock News Fetch Tool")
def get_stock_news(stock_symbol: str) -> list:
    """
    Fetch recent financial news headlines for a stock symbol.
    """

    API_KEY = os.getenv("NEWS_API_KEY")

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={stock_symbol}&"
        f"sortBy=publishedAt&"
        f"language=en&"
        f"pageSize=5&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    if "articles" not in data:
        return []

    headlines = [
        article["title"]
        for article in data["articles"]
        if article.get("title")
    ]

    return headlines

