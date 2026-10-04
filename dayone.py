# Write a Python program demonstrating each of the following list methods:
# 1. append(), insert(), remove(), pop()


# Using append() method
students = ["Faizal","Hassan","Danish","Jawad"]
students.append("Marvi")

for i in students:
    print(i,end=" ")

#using insert() method
subjects = ["CNDC","OS","DBMS","AI/ML"]
subjects.insert(2,"FOP")

print()
for i in subjects:
    print(i,end=" ")

# using remove() method
fruites = ["Apple","Banana","Mango","Grapes"]
fruites.remove("Mango")

print()
for i in fruites:
    print(i,end=" ")

# using pop() method
numbers = [1,2,3,4,5]
numbers.pop()

print()
for i in numbers:
    print(i,end=" ")


