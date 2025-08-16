# Stock and News Checker

This Python script checks daily stock price changes using the Alpha Vantage API.  
If the stock price changes more than 5%, it fetches the top 3 related news articles from NewsAPI.

## Features
- Fetch stock daily closing prices
- Calculate percentage change between days
- Get related news if stock movement > 5%

## Requirements
- Python 3.x
- `requests` library

Install requirements:
```bash
pip install requests
