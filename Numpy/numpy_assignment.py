import numpy as np

# Part 1: Creating NumPy Arrays
# 1. Using Built-in Methods:
# An array of numbers from 0 to 20 with a step of 2.
print("Part one Question 1 A: \n")
array_0_to_20 = np.arange(0,21,2)
print (array_0_to_20)
print('------------------- ')

# A 3x3 identity matrix.
print("Part one Question 1 B: \n")
identity_matrix = np.eye(3,3)
print(identity_matrix)
print('------------------- ')

# A 4x4 array filled with ones.
print("Part one Question 1 C: \n")
array_ones = np.ones((4,4))
print(array_ones)
print('-------------------')

# An array of 10 equally spaced numbers between 5 and 50.
print("Part one Question 1 D: \n")
array_5_50 = np.linspace(5,50,10)
print(array_5_50)

print('------------------------------------------------------------')

# 2. Creating Arrays from Lists
# Convert a Python list [10, 20, 30, 40, 50] into a NumPy array.
print("Part one Question 2 A: \n")
list1 = [10, 20, 30, 40, 50]
array_list1 = np.array(list1)
print(array_list1)
print('-------------------')
# Generate a 3x3 matrix of random numbers using rand(), randn(), and randint().
print("Part one Question 2 B: \n")
print("3x3 matrix of random numbers using rand()")
rand1 = np.random.rand(3,3)
print(rand1)
print('\n')
print("3x3 matrix of random numbers using randn()")
randn1 = np.random.randn(3,3)
print(randn1)
print('\n')
print("3x3 matrix of random numbers using randint()")
randiant1 = np.random.randint(0,10,(3,3))
print(randiant1)

print('------------------------------------------------------------')

# 3.Array Attributes
# Print the shape, size, and data type of an array you created in the previous steps.
print("Part one Question 3 A: \n")
print("Size of array is ",array_list1.size)
print("Shape of array is ",array_list1.shape)
print("Type of array is ",array_list1.dtype)


print('------------------------------------------------------------')
# Part 2: Indexing and Selection
# 1.Basic Indexing and Selection
''' Create a NumPy array [5, 10, 15, 20, 25, 30]. Select and print:The first element.
The last three elements.The elements at index positions 1 to 4.'''

print("Part two Question 1: \n")
array2 = np.array([5, 10, 15, 20, 25, 30]) 
print('The first element:',array2[0])
print('The last three elements:',array2[-3:])
print('The elements at index positions 1 to 4:',array2[1:5])

print('-------------------')
# 2. Slicing and Views
'''Create a 3x3 matrix from np.arange(1, 10).reshape(3, 3) and: Select the second row. 
Select the first two columns.Extract a sub-matrix of shape (2,2).'''

print("Part two Question 2: \n")
matrix3_3 = np.arange(1,10).reshape(3,3)
print(matrix3_3)
print('\n')
print('Select the second row:\n',matrix3_3[1:2])
print('Select the first two columns:\n',matrix3_3[:,0:2])
print('Extract a sub-matrix of shape (2,2):\n',matrix3_3[0:2,0:2])

print('-------------------')
# 3. Broadcasting
#Create a 3x3 matrix and add 10 to every element. Multiply the first column by 2.

print("Part two Question 3: \n")

matrix2 = np.arange(1,10).reshape(3,3)
print(matrix2)
print('\n')

matrix2_add_10 = matrix2.copy() + 10 
print('Add 10 to every element:\n', matrix2_add_10) 

matrix2_multi_2 = matrix2.copy()
matrix2_multi_2[:, 0] = matrix2_multi_2[:, 0] * 2
print('Multiply the first column by 2: \n',matrix2_multi_2)

print('-------------------')
# 4.Copying Arrays
# Create a NumPy array and demonstrate the difference between shallow and deep copies.+

print("Part two Question 4: \n")

array3 = np.array([1, 2, 3, 4])
shallow_copy = array3
deep_copy = array3.copy()
shallow_copy[0] = 100

print("After modifying shallow copy:")
print("Original array:", array3)
print("Shallow copy:", shallow_copy)
print("Deep copy (unchanged):", deep_copy)


deep_copy[1] = 200

print("\nAfter modifying deep copy:")
print("Original array (unchanged):", array3)
print("Shallow copy (reflects original):", shallow_copy)
print("Deep copy:", deep_copy)

print('-------------------')
# 5.Fancy Indexing
# Given arr = np.arange(10, 101, 10), select elements at index [0, 3, 5].

arr = np.arange(10, 101, 10)
print('Select elements at index [0, 3, 5]:',arr[[0,3,5]])

print('------------------------------------------------------------')
# Part 3: NumPy Operations
# 1. Mathematical Functions
# Find the maximum, minimum, index of max, and index of min for the array [3, 7, 2,9, 12, 5, 10].

print("Part three Question 1: \n")

array4 = np.array([3, 7, 2,9, 12, 5, 10])

max_val , index_max = array4.max() , array4.argmax()
min_val , index_min = array4.min() , array4.argmin()

print('The maximum and index of max:', max_val , index_max)
print('The minimum and index of min:', min_val , index_min)

print('-------------------')
# 2. Universal Array Functions
'''
1. Given arr = np.array([1, 2, 3, 4, 5]), apply the following functions:

a. Square root (sqrt())
b. Exponential (exp())
c. Sine (sin())
d. Logarithm (log())'''

print("Part three Question 2: \n")
arr2 = np.array([1, 2, 3, 4, 5])
print('Square root:',np.sqrt(arr2))
print('Exponential:' , np.exp(arr2))
print('Sine:' , np.sin(arr2))
print('Logarithm:' , np.log(arr2))
