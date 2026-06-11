# 📈 Stock Market News Alert

A Python automation script that monitors Tesla (TSLA) stock price movements and delivers breaking news directly to your WhatsApp. When the stock price changes by more than 5% between two consecutive days, the app fetches the top news articles about Tesla and sends them as WhatsApp messages via Twilio.

## Features

- Fetches daily closing prices for Tesla (TSLA) using the Alpha Vantage API
- Calculates the percentage change between the previous two closing prices
- Triggers a news fetch from the News API when the change exceeds 5%
- Sends the top 3 Tesla news headlines and summaries to WhatsApp via Twilio
- Each message includes an up 🔺 or down 🔻 indicator based on price direction

## How to Run

**Requirements:** Python 3.x with `requests` installed.

```bash
pip install requests
python main.py
```

## Setup

You will need API keys and credentials from the following services:

| Service | Purpose | Link |
|---|---|---|
| Alpha Vantage | Stock price data | https://www.alphavantage.co |
| News API | Tesla news headlines | https://newsapi.org |
| Twilio | WhatsApp messaging | https://www.twilio.com |

Add your credentials directly in `main.py` or store them as environment variables:

```python
STOCK_API_KEY = "your_alpha_vantage_key"
NEWS_API_KEY = "your_news_api_key"
TWILIO_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"
YOUR_WHATSAPP_NUMBER = "whatsapp:+your_number"
```

## Example WhatsApp Message

```
TSLA 🔺 5.5%
Headline: Tesla beats Q3 earnings expectations
Brief: Tesla reported record deliveries in Q3, exceeding analyst forecasts by 10%.
```

## Project Structure

```
stock-news-alert/
│
└── main.py        # All logic in a single procedural script
```

## About

Built as part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**. This project covers working with REST APIs, JSON data parsing, environment variables, and sending automated WhatsApp messages using the Twilio API.
