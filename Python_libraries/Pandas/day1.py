import pandas as pd

# Series - One Dimensional
# DataFrame - Two Dimensionals

# Series Example
marks = pd.Series([76,78,98,56])
print(marks)

# DataFrame Example
data = {
    "name": ["Faizal","Danish","Marvi","Jawad","Muzammil"],
    "age": [20,23,24,20,19],
    "gender": ["male","male","female","male","male"]
}

students = pd.DataFrame(data)

# Print all Rows and Columns
print(students)

# Print particular Column
print(students["name"])

# Print Multiple Columns
print(students[["name","gender"]])

# Filtering rows 
adults = students[students["age"] < 21]
print(adults)

males = students[students["gender"] == "male"]
print(males)

# adding new column
students["dept"] = "Computer Science"

print(students)