from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

headers = {
    "Accept-Language": "es-419,es;q=0.9:",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"

}
response = requests.get(url="https://www.amazon.com/DJI-cuatro-h%C3%A9lices-c%C3%A1mara-minutos/dp/B07RKPP1YL/ref=sr_1_1_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=dron&qid=1634913658&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUTRDV05DODlQNlowJmVuY3J5cHRlZElkPUEwNzA3MzAzM1NPMUsyOEdIUDFSRSZlbmNyeXB0ZWRBZElkPUEwMTM2MDgzUlZRREtFR0wwUVBTJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1", headers=headers)
response =response.text

soup = BeautifulSoup(response, "lxml")


Price = soup.find_all(class_ = "a-size-medium a-color-price priceBlockBuyingPriceString")

product_price = 0

for price in Price:
    product_price = (price.getText().split("$")[1])
    product_price2 = int(product_price.split(".")[0])


if product_price2 < 400:
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="Spuga123@gmail.com", password="ss12721272")
            connection.sendmail(from_addr="Spuga123@gmail.com",
                                to_addrs="spuga123@gmail.com",
                                msg="Subject: Compra la wea ctm url = https://www.amazon.com/DJI-cuatro-h%C3%A9lices-c%C3%A1mara-minutos/dp/B07RKPP1YL/ref=sr_1_1_sspa?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=dron&qid=1634913658&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzUTRDV05DODlQNlowJmVuY3J5cHRlZElkPUEwNzA3MzAzM1NPMUsyOEdIUDFSRSZlbmNyeXB0ZWRBZElkPUEwMTM2MDgzUlZRREtFR0wwUVBTJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1}")



