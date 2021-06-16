import numpy as np

row_1 = [1,2,3,4,5]
row_2 = [6,7,8,9,10]
row_3 = [11,12,13,14,15]
row_4 = [16,17,18,19,20]
row_5 = [21,22,23,24,25]

test_data = np.array([row_1, row_2, row_3, row_4, row_5])

print(test_data)

#slice
print(test_data[:,2:4:1])

# negative indexing
print(test_data[:,-2:-4:-1])

# boolean
greater_than_five = test_data > 5
print(greater_than_five)
print(test_data[greater_than_five])


# where
drop_under_5_array = np.where(test_data > 5, test_data, 0)
print(drop_under_5_array)

# logical
drop_under_5_and_over_20 = np.logical_and(test_data > 5, test_data < 20)
print(drop_under_5_and_over_20)
print(test_data[drop_under_5_and_over_20])


#advanced indexing
print("Advanced Indexing: \n")

array_a = np.arange(0, 100, 5)
print(array_a)
print(array_a.size)

array_a_reshape = array_a.reshape(4,5)
print(array_a_reshape)

#return every last value
print("Every last value:", array_a_reshape[:,-1])

# boolean
array_a_above_50 = array_a_reshape[array_a_reshape >= 50]
print("Every value Greather than or Equal to 50:", array_a_above_50)

# python slice
print("Every other value above fifty:", array_a_above_50[0:len(array_a_above_50):2])


# slice of a row
print(array_a_reshape)
print("Every other column:\n",array_a_reshape[:, 0:5:2])

# where
print(np.where(array_a_reshape > 50, array_a_reshape * 2, -1))


# Reverse Columns Challenge
print(array_a_reshape)
print(array_a_reshape[:,-1:-6:-1])
