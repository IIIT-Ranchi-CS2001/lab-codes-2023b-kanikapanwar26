import pandas as pd
import numpy as np

# Load the dataset
file_path = r"C:\Users\kanik\OneDrive\Desktop\Exam\AQI_Data (1).csv"
data = pd.read_csv(file_path)

# Display the first 8 rows
print("First 8 rows:")
print(data.head(8))

# Display the last 5 rows
print("\nLast 5 rows:")
print(data.tail(5))

# Show data types and count of null values in each column
print("\nData types and null values:")
print(data.dtypes)
print("\nNull values in each column:")
print(data.isnull().sum())

# Group by city and calculate the desired statistics
grouped_data = data.groupby('City')

mean_aqi = grouped_data['AQI'].mean()
max_pm25 = grouped_data['PM2.5'].max()
min_pm10 = grouped_data['PM10'].min()

# Display the results
print("\nMean AQI for each city:")
print(mean_aqi)

print("\nMax PM2.5 for each city:")
print(max_pm25)

print("\nMin PM10 for each city:")
print(min_pm10)