import pandas as pd

# Create a DataFrame with columns Name, Age and Marks for five students.
data = {
    "name": ["Faizal","Danish","Marvi","Jawad","Muzammil"],
    "age": [22,21,21,23,23],
    "marks": [78,82,86,97,87]
}

students = pd.DataFrame(data)
print(students)

# Print only the Name column, then print Name and Marks together.
print(students["name"])
print(students[["name","marks"]])

# Print students who scored more than 85 marks.
updated_students = students[students["marks"] > 85]
print(updated_students)

# Print the highest and lowest marks.
print("Highest:",students["marks"].max())
print("Lowest:",students["marks"].min())

# Create a Passed column: True when Marks are at least 50, otherwise False.
students["passed"] = students["marks"] >= 50
print(students)