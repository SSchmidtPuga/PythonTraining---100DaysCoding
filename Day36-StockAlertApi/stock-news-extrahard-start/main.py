STOCK = "TSLA"
COMPANY_NAME = "Bitcoin"
from datetime import datetime, date, timedelta
import requests

#Time
time_now = datetime.now()
yesterday = date.today() - timedelta(days=1)
before_yesterday = yesterday - timedelta(days=1)


#Stock variation
#
#.
URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey=5BR9Z18ORRL4JYL1"
response = requests.get(url=URL)
response.raise_for_status()
Tesla_info = response.json()
price_yesterday = float(Tesla_info['Time Series (Daily)'][yesterday.strftime('%Y-%m-%d')]['4. close'])
price_beforeyesterday = float(Tesla_info['Time Series (Daily)'][before_yesterday.strftime('%Y-%m-%d')]['4. close'])
delta = ((price_yesterday - price_beforeyesterday)/ price_beforeyesterday ) *100
delta  = round(delta,2)



#News of the stock
APIKEY = "465b8d49929642bda3e6148b1882e6ce"
URLNEWS =  f"https://newsapi.org/v2/top-headlines?q={COMPANY_NAME}&from={time_now.date()}&sortBy=popularity&apiKey={APIKEY}"

response2 = requests.get(url=URLNEWS)
response2.raise_for_status()
Tesla_news = response2.json()

news1 = Tesla_news["articles"][0]["title"]
news2 = Tesla_news["articles"][1]["title"]
news3 = Tesla_news["articles"][2]["title"]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if delta >1:
    from twilio.rest import Client
    account_sid = 'AC66384862d688e2cf1af4dbbf22454fa3'
    auth_token = '3c39952128fbf27d2be5573f97af97dd'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f" {STOCK}: {delta}% \n Headline1: {news1} Headline2: {news2} Headline3: {news3}",
        from_='+18482943302',
        to='+56978046798'
    )
    print(message.sid)

#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

