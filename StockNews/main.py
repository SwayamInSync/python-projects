import requests
from twilio.rest import Client
from bs4 import BeautifulSoup

account_sid = "your twilio account_sid"
auth_token = "<your twilio auth_tooken>"
is_up = ""


def make_sms(message):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = message,
        from_='<your twilio no>',
        to='<verified num at twilio>')
    print(message.status)


def clean_text(raw_html):
    cleantext = BeautifulSoup(raw_html, "lxml").text
    return cleantext


def show_news():
    news_api = "<your newsapi api>"
    news_url = "https://newsapi.org/v2/everything"

    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": news_api,

    }

    res = requests.get(url=news_url, params=news_parameters)
    for n in range(0, 3):
        title = clean_text(res.json()["articles"][n]["title"])
        description = clean_text(res.json()["articles"][n]["description"])
        body = f"{STOCK} : {is_up} {difference_percent}\nHeadline: {title}\nBrief: {description}"
        make_sms(body)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

url = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "JFAL19NYUU8OYQT8",
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
days = list(response.json()["Time Series (Daily)"])
yesterday = days[0]
before_yesterday = days[1]

yesterday_closing = response.json()["Time Series (Daily)"][yesterday]["4. close"]
before_yesterday_closing = response.json()["Time Series (Daily)"][before_yesterday]["4. close"]

difference = float(yesterday_closing) - float(before_yesterday_closing)

if difference > 0:
    is_up = "🔺"
else:
    is_up = "🔻"

difference_percent = round(abs((difference / float(yesterday_closing)) * 100),2)

if difference_percent >= 0:
    show_news()


