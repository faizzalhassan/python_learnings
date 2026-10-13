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

