APP_ID= "2d931518"
API_KEY = "e93092a2069eb9b8312b4d69d5afa880"



from datetime import datetime, date, timedelta
import requests

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
url = f"https://trackapi.nutritionix.com/v2/natural/exercise/"

exerecise = input("What did you do today? ")


parameters = {
 "query":exerecise,
 "gender":"fMale",
 "weight_kg":89,
 "height_cm": 179,
 "age":23
}

response = requests.post(url=url ,json=parameters,  headers=headers)
response.raise_for_status()
response = response.json()

#

GOOGLEURL = "https://api.sheety.co/6a1bf581f50de85747217c93bf41f1da/copiaDeMyWorkouts/workouts"

response2 = requests.get(url=GOOGLEURL)
response2.raise_for_status()
response2 = response2.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


new_workout = {
  'workout': {
      'date': today_date,
      'time': now_time,
      'exercise': response['exercises'][0]["user_input"].title(),
      'duration': response['exercises'][0]['duration_min'],
      'calories': response['exercises'][0]['nf_calories']
  }

}

response3 = requests.post(url=GOOGLEURL, json=new_workout)
print(response3.text)
