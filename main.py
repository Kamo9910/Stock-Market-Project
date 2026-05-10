import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
News_Api_key = os.environ.get("NEWS_API_KEY")

OWNM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key =  os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameter = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey":"0ELFQOZFWKB8JIDH"
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


response = requests.get(url= STOCK_ENDPOINT,params=parameter)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday['4. close']
print(day_before_yesterday_closing_price)

difference = float(yesterday_closing_price)- float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference/float(yesterday_closing_price))*100)
print(diff_percent)

if abs(diff_percent) >1:
    news_params = {
        "apikey": News_Api_key,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT,params=news_params)
    articles =  news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formated_articles =[f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]

    client = Client(account_sid,auth_token)

    for articles in formated_articles :
        message = client.messages.create(
            from_= f"whatsapp:{os.environ.get("VITUAL_NO")}",
            body=articles,
            to= f"whatsapp:{os.environ.get("OWN_API_KEY")}"
        )

        print(message.status)
print(OWN_API_KEY)
