# ===== Numpy Library Array Related Tasks ===== 

# Create an array containing 10, 20, 30, 40 and 50. Print its sum, average, maximum and minimum
import numpy as np

numbers = np.array([10,20,30,40,50])

print("Sum:",np.sum(numbers),
      "\nAverage:",np.average(numbers),
      "\nMaximum:",np.max(numbers),
      "\nMinimum:",np.min(numbers))


# Create an array of five students marks. Add 10 to every mark and print the updated array.

marks = np.array([55,60,65,70,75,80])
updated_marks = marks + 10

print("Updated Marks:",updated_marks)


# Create an array of 12, 45, 67, 23, 89, 34 and 76. Print only values greater than 40 using NumPy.

numbers = np.array([12,45,67,23,89,34,76])
greater = np.where(numbers > 40)

print("Greater than 40:",numbers[greater])

# Create a 3 × 3 NumPy array and print its number of dimensions, shape

data = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Dimension:",data.ndim)
print("Shape:",data.shape)
print("Size:",data.size)