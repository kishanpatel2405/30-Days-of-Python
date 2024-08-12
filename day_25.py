# 25	Pandas

# 25	Installing Pandas

# pip install pandas

# 25	Importing Pandas

import pandas as pd
import numpy as np
from pandas import DataFrame

# 25	Creating Pandas Series with Default Index

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)
print()

# 25	Creating Pandas Series with custom index

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)
print()

fruits = ['apple', 'banana', 'mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)
print()

# 25	Creating Pandas Series from a Dictionary

dct = {'name': 'kishan', 'age': 25, 'country': 'China'}
dct = pd.Series(dct)
print(dct)
print()

# 25	Creating a Constant Pandas Series

a = pd.Series(10, index=[1, 2, 3, 4, 5])
print(a)
print()

# 25	Creating a Pandas Series Using Linspace

s = pd.Series(np.linspace(5, 20, 10))
print(s)
print()

# 25	DataFrames
# 25	Creating DataFrames from List of Lists

data = [
    ['kishan', 'india', 'rajkot'],
    ['janki', 'india', 'junagadh'],
    ['sumi', 'america', 'stoke home']
]
df = pd.DataFrame(data, columns=['name', 'country', 'City'])
print(df)
print()

# 25	Creating Data Frame Using Dictionary

data = {
    'name': ['kishan', 'mansi', 'gopi'],
    'age': [21, 18, 19],
    'country': ['China', 'India', 'Japan']
}
df = DataFrame(data)
print(df)
print()

# 25	Creating DataFrames from a List of Dictionaries

data = [
    {'name': 'kishan', 'age': 21, 'country': 'China'},
    {'name': 'surbhi', 'age': 10, 'country': 'india'},
    {'name': 'shruti', 'age': 22, 'country': 'India'}
]
df = DataFrame(data)
print(df)
print()

# 25	Reading CSV File Using Pandas

import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
print()

# 25	Data Exploration

print(df.head())
print()

print(df.tail())
print()

print(df.shape)
print()

print(df.columns)
print()

heights = df['Height']
print(heights)

weights = df['Weight']
print(weights)
print()

print(weights)

print(len(heights) == len(weights))
print()

print(heights.describe())
print()

# 25	Modifying a DataFrame
# 25	Creating a DataFrame

import pandas as pd

data = [
    {'name': 'kishan', 'age': 21, 'city': 'rajkot'},
    {'name': 'Mannat', 'age': 21, 'city': 'rajkot'},
    {'name': 'radhika', 'age': 21, 'city': 'rajkot'}
]
df = pd.DataFrame(data)
print(df)
print()

# 25	Adding a New Column

weights = [74, 78, 69]
df['Weight'] = weights
print(df)
print()

heights = [173, 169, 170]
df['Height'] = heights
print(df)
print()

# 25	Modifying column values

df['Height'] = df['Height'] * 0.01
print(df)
print()


def calculate_bmi():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w, h in zip(weights, heights):
        b = w / (h * h)
        bmi.append(b)
    return bmi
bmi = calculate_bmi()
df['BMI'] = bmi
print(df)
print()

# 25	Formating DataFrame columns

df['BMI'] = round(df['BMI'], 1)
print(df)
print()

birth_year = ['2003', '2003', '2003']
current_year = pd.Series(2024, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
print(df)
print()

# 25	Checking data types of Column values

print(df.Weight.dtype)
print()

df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype)
print()

ages = df['Current Year'] - df['Birth Year']
print(ages)

df['Ages'] = ages
print(df)
print()

mean = (35 + 30)/ 2
print('Mean: ',mean)
print()

# 25	Boolean Indexing

print(df[df['Ages'] > 12])
print()
print()

# 25	Exercises: Day 25

# Read the hacker_news.csv file from data directory

import pandas as pd

df = pd.read_csv('hacker_news.csv')
print(df)

# Get the first five rows
print(df.head())
print()

# Get the last five rows
print(df.tail())
print()

# Get the title column as pandas series

title_series = df['title']
print(title_series)
print()

# Count the number of rows and columns

print(df.shape)
print()
print()
print()

# Filter the titles which contain python

title_series = df['title']
filtered_titles = title_series[title_series.str.contains('python', case=False, na=False)]
print(filtered_titles)

# Filter the titles which contain JavaScript
filtered_titles = title_series[title_series.str.contains('JavaScript', case=False, na=False)]
print(filtered_titles)
print()
print()
print()

# Explore the data and make sense of it
print("\nDataframe info:")
print(df.info())
print()
print()

print("\nSummary statistics:")
print(df.describe(include='all'))
print()
print()

print("\nChecking for missing values:")
print(df.isnull().sum())
