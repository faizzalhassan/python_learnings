# Dictionary 

student = {
    "Name": "faizal hassan",
    "rollno": 2312240,
    "semester": 6,
    "age": 22,
    "gpa": 3.8
}

# displaying the dictionary
print(student)

# accessing the name
print("Name:",student["Name"])

# adding a new key-value pair
student["department"] = "Computer Science"
print(student)

# updating an existing value
student["gpa"] = 3.9
print(student)

# deleting a key-value pair
del student["age"]
print(student)

