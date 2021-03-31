# import csv
#
# with open("weather_data.csv", mode="r") as f:
#     datas = csv.reader(f)
#     temperatures = []
#     print(datas)
#     for d in datas:
#         print(d)
#         if d[1] != "temp":
#             temperatures.append(int(d[1]))
#     print(temperatures)

import pandas

FILE_PATH = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

data = pandas.read_csv(FILE_PATH)
# print(data["temp"])
# data_dict = data.to_dict()
# data_list = data["temp"].to_list()
# print(data_dict)
# print(data_list)
#
#
# def get_average(datas):
#     avrg = 0
#     for d in datas:
#         avrg += d
#     avrg = avrg / len(datas)
#     return avrg
#
#
# test = get_average(data_list)
#
# print(test)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
#
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(data[data.temp == data["temp"].max()])
# data_dict = {
#     "students": ["Louis", "Hanane", "Louise"],
#     "scores": [76, 56, 65]
# }
# data2 = pandas.DataFrame(data_dict)
# print(data2)
# data2.to_csv("new_data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

