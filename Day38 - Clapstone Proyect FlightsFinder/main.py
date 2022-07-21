import requests
from datetime import datetime, date, timedelta

MIN_STAY= 8
MAX_STAY = 15
#--------------------------------------- Time Module ------------------------------------------------------------------
time_now = datetime.now()
today =time_now.today()
Tommorrow  = date.today() + timedelta(days=1)
Months_6  = Tommorrow + timedelta(days=180)
Tommorrow = Tommorrow.strftime("%d/%m/20%y")
Months_6 = Months_6.strftime("%d/%m/20%y")
#--------------------------------------- Google sheet -----------------------------------------------------------------
URLGOOGLESHEET = "https://api.sheety.co/6a1bf581f50de85747217c93bf41f1da/flightsDeals/prices"
GoogleSheetsFlights = requests.get(url=URLGOOGLESHEET)
GoogleSheetsFlights = GoogleSheetsFlights.json()

#--------------------------------------- Flight Finder ----------------------------------------------------------------

for Countrys in range(int(len(GoogleSheetsFlights["prices"]) -1)):
    FROM = "SCL"
    TO = GoogleSheetsFlights["prices"][Countrys]["iataCode"]
    Lower_price = GoogleSheetsFlights["prices"][Countrys]["lowestPrice"]

    URLFLIGHTSFINDER = F"https://tequila-api.kiwi.com/v2/search?fly_from={FROM}&fly_to={TO}&dateFrom={Tommorrow}&dateTo" \
                       F"={Months_6}&max_stopovers=2&nights_in_dst_from={MIN_STAY}&nights_in_dst_to={MAX_STAY}&flight_type=round&limit=2 "
    Header = {
        'apikey': "yPOAtrtMsUFjABYqH3fdtLdFCXxv4zko",
    }
    FlightDeals = requests.get(url=URLFLIGHTSFINDER, headers=Header)
    FlightDeals = FlightDeals.json()
    New_Price  =  FlightDeals["data"][0]["price"]
    Link = (FlightDeals["data"][0]["deep_link"])
    Depart = FlightDeals["data"][0]["route"][0]["local_departure"].split("T")[0]
    Return = FlightDeals["data"][0]["route"][-2]["local_departure"].split("T")[0]
    if New_Price< Lower_price:
        Mesagge = (f"Hey i found a flight really cheap, {FROM} to {TO}, in  ${New_Price} EUR.\n Dates = {Depart} - {Return} \n Link:{Link} " )
        from twilio.rest import Client
        account_sid = 'AC66384862d688e2cf1af4dbbf22454fa3'
        auth_token = '3c39952128fbf27d2be5573f97af97dd'
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=Mesagge,
            from_='+18482943302',
            to='+56971098674'
        )
        print(message.sid)


