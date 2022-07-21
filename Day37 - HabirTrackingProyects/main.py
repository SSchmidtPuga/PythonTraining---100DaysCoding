import requests
from datetime import datetime, date, timedelta



username= "sebastian2312312"
token =  "Ss12721272!!"
pixela_endpoint = "https://pixe.la/v1/users"



# User_params = {
#     "token": "Ss12721272!!",
#     "username": "sebastian2312312",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# response = requests.post(url=pixela_endpoint, json=User_params)
# print(response.text)


Graph_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1"

graph_config = {
    "id": "graph1",
    "name": "coding tracking",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": token
}
# response = requests.post(url=Graph_endpoint, json = graph_config, headers=headers)
# print(response.text)


time_now = datetime.now()
today =time_now.today()
today = today.strftime("%Y%m%d")

Pixel_config = {
    "date": today,
    "quantity":input("How many minutes you code today? "),
}


response = requests.post(url=Graph_endpoint, json = Pixel_config, headers=headers)
print(response.text)