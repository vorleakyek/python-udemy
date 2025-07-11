# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# way-1
total_temp = 0
for temp in temp_list:
    total_temp = total_temp + temp
average_temp = total_temp/len(temp_list)
# print(average_temp)

# way-2
avg = sum(temp_list) / len(temp_list)

# way-3
# print(data["temp"].mean())

# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])


max_row = data[data.temp == data.temp.max()]
print(max_row.temp)
print((max_row.temp * 1.8) +32)

#Create a dataframe from scratch
data_dict = {
    "students": ["Ash", "James", "Hash"],
    "scores": [73, 56, 79]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
