import requests

# Replace with your own API keys
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
STOCKS_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"

# Example stock and company
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Fetch news related to the company
news_url = f"https://newsapi.org/v2/everything?q={STOCK}&sortBy=popularity&apiKey={NEWS_API_KEY}"
response = requests.get(news_url)
news_data = response.json()
print(news_data)

def get_news():
    """Prints the top 3 news articles related to the stock"""
    articles = news_data.get('articles', [])
    for article in articles[:3]:
        print("Title:", article['title'])
        print("URL:", article['url'])
        print("Published at:", article['publishedAt'])
        print("---")

# Fetch stock data from Alpha Vantage
# Replace the demo API key with your own: https://www.alphavantage.co/support/#api-key
stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCKS_API_KEY}'
r = requests.get(stock_url)
data = r.json()

# Get yesterday's and the day before closing prices (adjust dates as needed)
yesterday_close = float(data["Time Series (Daily)"]["2025-08-14"]["4. close"])
day_before_close = float(data["Time Series (Daily)"]["2025-08-13"]["4. close"])

# Calculate price change
total_change = abs(yesterday_close - day_before_close)
print("Total change:", total_change)

percentage_change = (total_change / day_before_close) * 100
percentage_change = round(percentage_change, 2)
print("Percentage change:", percentage_change, "%")

# If stock moved more than 5%, fetch top 3 news
if percentage_change > 5:
    get_news()
