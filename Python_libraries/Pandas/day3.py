import pandas as pd

data = pd.read_csv("practice.csv")

print(data.head())
# print(data.tail())
# print(data.sample())
# print(data.shape)
# print(data.dtypes)
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())

# print(data[["name","city"]])
# print(data[data["age"] > 20])