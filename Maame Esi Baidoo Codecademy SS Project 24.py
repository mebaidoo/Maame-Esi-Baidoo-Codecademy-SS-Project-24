import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data
#Inspecting the dataframe
#print(london_data.head()
#print(london_data.iloc[100:200])
print(len(london_data))
#Selecting the temperature column
temp = london_data["TemperatureC"]
#Calculating the average temperature of temp
average_temp = np.average(temp)
print(average_temp)
#Calculating the variance of temp
temperature_var = np.var(temp)
print(temperature_var)
#Calculating the standard deviation of temp
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)
print(london_data.head())
#Selecting only rows with month == 6 and 7, that is June and July to find the best month to plan a trip
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
#Calculating the mean temperature for June and July
print(np.average(june))
print(np.average(july))
#Calculating the standard deviation of temperature for June and July
print(np.std(june))
print(np.std(july))
#Calculating the mean and standard deviation of each month
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month " + str(i) + " is " + str(np.average(month)))
  print("The standard deviation of temperature in month " + str(i) + " is " + str(np.std(month))+ "\n")
#Selecting the humidity column based on the hour column to find what hours are more or less rainy using the mean and standard deviation
print(london_data.tail())
for i in range(0, 24):
  hour = london_data.loc[london_data["hour"] == i]["Humidity"]
  print("The mean humidity in hour " + str(i) + " is " + str(np.average(hour)))
  print("The standard deviation of humidity in hour " + str(i) + " is " + str(np.std(hour))+ "\n")