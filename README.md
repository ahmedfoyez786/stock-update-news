# Stock Update News

This project checks the daily stock price changes for a specified company and sends relevant news articles to your phone using the Twilio API if there is a significant price change.

## Features

- Retrieve daily stock prices for a specified company using the Alpha Vantage API.
- Calculate the percentage change in stock prices.
- Fetch the latest news articles for the company using the NewsAPI.
- Send SMS alerts with news headlines and descriptions using the Twilio API.

## Requirements

- Python 3.x
- `requests`
- `twilio`

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/ahmedfoyez786/stock-update-news.git
   cd stock-update-news
   ```

2. Install the required libraries:

   ```sh
   pip install requests twilio
   ```

3. Set up your API credentials:

   - Get your Alpha Vantage API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
   - Get your NewsAPI key from [NewsAPI](https://newsapi.org/register).
   - Set up your Twilio account and get your Account SID and Auth Token from [Twilio](https://www.twilio.com/try-twilio).

4. Update the following variables in the script with your credentials:

   ```python
   STOCK_NAME = "TSLA"
   COMPANY_NAME = "Tesla Inc"
   AuthToken = "your_twilio_auth_token"

   STOCK_ENDPOINT_API = "your_alpha_vantage_api_key"
   NEWS_ENDPOINT_API = "your_newsapi_key"

   account_sid = 'your_twilio_account_sid'
   ```

5. Update the phone numbers in the script:
   ```python
   from_='+your_twilio_phone_number'
   to='+your_phone_number'
   ```

## Usage

1. Run the script:

   ```sh
   python stock_update_news.py
   ```

2. The script will:
   - Fetch the daily stock prices for the specified company.
   - Calculate the percentage difference between the last two closing prices.
   - If the percentage difference is greater than or equal to 10%, fetch the latest news articles about the company.
   - Send the top 2 news headlines and descriptions to your phone via SMS.

## Example

```sh
TSLA: 🔺5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC. The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
```
