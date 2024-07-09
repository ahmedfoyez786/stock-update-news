from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
AuthToken = "Your auth"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_ENDPOINT_API = "XEHQPPZQZ48O1HBI"
NEWS_ENDPOINT_API = "your endpoint"

parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_ENDPOINT_API
}
response = requests.get(STOCK_ENDPOINT, params=parameter)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterdays_closing_price = float(data_list[0]["4. close"])
print(yesterdays_closing_price)
day_before_yesterdays_closing_price = float(data_list[1]["4. close"])
print(day_before_yesterdays_closing_price)
difference = abs(yesterdays_closing_price - day_before_yesterdays_closing_price)
percent_difference = (difference / yesterdays_closing_price) * 100
print(percent_difference)

if percent_difference < 10:
    news_parms = {
        "apiKey": NEWS_ENDPOINT_API,
        "qInTitle": COMPANY_NAME
    }
    response1 = requests.get(NEWS_ENDPOINT, params=news_parms)
    news_data = response1.json()["articles"]
    news_data_list = [{"title": value["title"], "description": value["description"]} for value in news_data[0:2]]

    account_sid = 'twillo sid'

    client = Client(account_sid, AuthToken)

    for article in news_data_list:
        message = client.messages.create(
            body=article["title"],
            from_='+14058885860',
            to='+8801783678204'
        )




"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


