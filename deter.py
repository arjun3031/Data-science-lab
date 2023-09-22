import numpy as np
import math
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("Enter the matrix elements row-wise:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = float(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        row.append(element)
    matrix.append(row)
matrix_np = np.array(matrix)
determinant = np.linalg.det(matrix_np)
print(f"The determinant of the matrix is: {math.ceil(determinant)}")
