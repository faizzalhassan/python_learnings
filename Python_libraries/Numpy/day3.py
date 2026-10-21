import numpy as np

# Basic level tasks

# Create a 1D array containing five integers & Display the array and its data type.
arr = np.arange(1,6)
print(arr)
print(arr.dtype)

# Create two NumPy arrays: [10, 20, 30] and [2, 4, 6] & Perform addition, subtraction, multiplication, and division.
arr1 = np.array([10,20,30])
arr2 = np.array([2,4,6])

print("Addition:",arr1 + arr2)
print("Subtraction:",arr1 - arr2)
print("Multiplication:",arr1 * arr2)
print("Division:",arr1 / arr2)


# Create an array containing [15, 8, 25, 12, 30] & Find and display the maximum, minimum, and sum of the elements.

arr4 = np.array([15,8,25,12,30])

print("Max:",np.max(arr4))
print("Min:",np.min(arr4))
print("Sum:",np.sum(arr4))


# Create a 2D array with 3 rows and 3 columns & Display the array, its shape, number of dimensions, and total number of elements.
arr2D = np.arange(1,10).reshape(3,3)

print(arr2D)
print("Shape:",arr2D.shape)
print("Dimension:",arr2D.ndim)
print("Size:",arr2D.size)

# Create an array containing numbers from 1 to 10 & Display the first element, last element, and elements from index 2 to index 6.
arr5 = np.arange(1,11)

print("First Element:",arr5[0])
print("Last Element:",arr5[-1])
print("From 2 to 6:",arr5[2:7])