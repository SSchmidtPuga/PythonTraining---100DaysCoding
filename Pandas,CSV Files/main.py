# with open("weather_data.csv") as data:
#     data = data.readlines()



# import csv
# with open("weather_data.csv") as data:
#       data = csv.reader(data)
#       temperature =[]
#       for raw in data:
#           if raw[1] != "temp":
#             temperature.append(int(raw[1]))
#
# print(temperature)



# data = pandas.read_csv("weather_data.csv")
#
# # data_colum_temperature_mean  = data["temp"].mean()
# data_colum_temperature_max = data["temp"].max()
# #
# # print(data_colum_temperature_mean)
# # print(data_colum_temperature_max)
#
# max_raw = data[data.temp == data_colum_temperature_max ]
#
# monday = data[data.day == "Monday"]
#
# farenheit = (monday.temp * 9/5) +32
# print(farenheit)
# print(max_raw)

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_squirrel = data["Primary Fur Color"]


colors =["Black","Gray", "Red"]


color_squirrel_numbers_black = len(data[color_squirrel == "Black"])
color_squirrel_numbers_gray = len(data[color_squirrel == "Gray"])
color_squirrel_numbers_cinnamon = len(data[color_squirrel == "Cinnamon"])


diccionarie_of_squirrle = {
    "Primary Fur Color" : ["Black", "Gray", "Cinnamon"],
    "Count" : [color_squirrel_numbers_black,  color_squirrel_numbers_gray,color_squirrel_numbers_cinnamon ]


}

df = pd.DataFrame(diccionarie_of_squirrle)
df.to_csv("Squirrle_count.csv")


print(color_squirrel_numbers_black)

numbers_of_colors = data.pivot_table(columns=['Primary Fur Color'], aggfunc='size')
print(numbers_of_colors)

