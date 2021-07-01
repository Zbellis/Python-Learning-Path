import numpy as np

array_a = np.array([[1,2],[3,4]])
array_b = np.array([[2,2],[6,6]])

# single array operations
print("Sum of whole array:", array_a.sum())
print("Sum of colums:", array_a.sum(axis=0))
print("Sum of rows:", array_a.sum(axis=1))

print(array_a.cumsum())
print(array_a.prod())
print(array_a.cumprod())

# two array math
print(array_a + array_b)
print(array_a - array_b)
print(array_a * array_b)
print(array_a / array_b)

print(np.dot(array_a, array_b))


