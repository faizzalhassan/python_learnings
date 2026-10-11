# 01. Check whether a number is positive, negative, or zero

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 02. Find the greatest of three numbers

numbers = [12, 59, 3.8]
greatest = max(numbers)
print("The greatest number is:", greatest)

# 03. Check whether a student passed or failed

marks = int(input("Enter the obtained marks: "))

if marks >= 55:
    print("The student has passed.")
else:
    print("The student has failed.")

# 04. Display grade according to marks

marks = int(input("Enter the obtained marks: "))

if marks >=90:
    print("Grade: A+")
elif marks >= 85:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B+")
elif marks >= 75:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C+")
elif marks >= 55:
    print("Grade: C")
else:
    print("Grade: F")

# 05. Check whether a number is even or odd using nested if

num = int(input("Enter a number: "))

if num % 2 == 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is even.")
else:
    print("The number is odd.")

# 06. Simple calculator using if-elif-else

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    print("Addition:", num1 + num2)
elif operator == "-":
    print("Subtraction:", num1 - num2)
elif operator == "*":
    print("Multiplication:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")

# 07. Display month name using month number

month = int(input("Enter the month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number.")

# 8. Write a function to find the greatest of two numbers.

def find_greatest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal."

result = find_greatest(10, 20)
print("The greatest number is:", result)

# 09. Write a program to create an integer array and find its largest element

arr = [10, 5, 8, 20, 15]
largest = max(arr)
print("The largest element: ", largest)

# 10. Write a program to find the maximum, minimum, and sum of numbers in a list
numbers = [49,32,56,78,65,31,75]

maximum = max(numbers)
minimum = min(numbers)
sumofnumbers = sum(numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", sumofnumbers)


# 11. Write separate functions to perform addition, subtraction, and multiplication.

def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

print("Addition:",addition(10,5))
print("Subtraction:",subtraction(10,5))
print("Multiplication:",multiplication(10,5))