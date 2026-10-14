import pandas as pd

# Series - One Dimensional
# DataFrame - Two Dimensionals


# Series Example
# marks = pd.Series([76,78,98,56])
# print(marks)

# DataFrame Example
data = {
    "name": ["Faizal","Danish","Marvi"],
    "age": [20,23,24],
    "gender": ["male","female","male"]
}

students = pd.DataFrame(data)

print(students["gender"])