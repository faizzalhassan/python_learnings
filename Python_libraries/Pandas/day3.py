import pandas as pd

data = pd.read_csv("practice.csv")

# print(data.head()) # Returns top 5 rows
# print(data.tail()) # Returns last 5 rows
# print(data.sample()) # Returns Randomly One Row
# print(data.shape) # Tells Number of rows and columns
# print(data.dtypes) # Tell Datatypes 
# print(data.info()) # Gives Info of each column and its not null count
# print(data.describe()) # It describes count,mean,std,max,min of all the numerical columns
# print(data.isnull().sum()) # Counts all the not null rows in each column

# print(data[["name","city"]]) # Prints Name and City Column only
# print(data[data["age"] > 20]) # Prints only those rows which satisfy the condition

# Print Those students who live in Karachi and Age is more than 20
# print(data[(data["city"] == 'Karachi') & (data['age'] > 22)])


# Print those rows which contains "Khan" word in name
# print(data[data["name"].str.contains("Khan")])

print(data.dropna()) # It drops all the rows having null values somewhere
print(data.isnull().sum())