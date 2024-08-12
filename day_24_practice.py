# importing  numpy

import numpy as np

print(np.__version__)
print(np.__dir__)

# creating int numpy array

python_list = [1, 2, 3, 4, 5]
print('Type:', type(python_list))
print(python_list)
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimensional_list)
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)
print()

# creating float numpy array

lst = [1, 2, 3, 4, 5, 6]
np_lst = np.array(lst, dtype=float)
print(np_lst)

# creating boolean numpy array

lst = [1, 2, 3, 4, 5, 6, 0]
np_lst = np.array(lst, dtype=bool)
print(np_lst)
print()

# creating multidimensional array using numpy

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)
print()

# Converting numpy array to list

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# Creating numpy array from tuple

python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))
print('python_tuple: ', python_tuple)
numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print('numpy_array_from_tuple: ', numpy_array_from_tuple)
print()

# Shape of numpy array

nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array.shape)
print()

# Data type of numpy array

int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
print()

# Size of a numpy array

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])
print('The size:', numpy_array_from_list.size)
print('The size:', two_dimensional_list.size)
print()

# Mathematical Operation using numpy

# Addition (+)

# Mathematical Operation
# Addition

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print(ten_plus_original)
print()

# Subtraction (-)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list - 10
print(ten_plus_original)
print()

# Multiplication (*)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list * 10
print(ten_plus_original)
print()

# Division (/)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list / 10
print(ten_plus_original)
print()

# Modules (%)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list % 10
print(ten_plus_original)
print()

# Floor Division(//)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list // 10
print(ten_plus_original)
print()

# Exponential(**)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list ** 10
print(ten_plus_original)
print()

# Checking data types

numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
print()

# converting type

# int to float
numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr)

# float to int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype='int')
print(numpy_int_arr)

# int to boolean
a = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
print(a)

# int to str
a = np.array([1, 2, 3, 4, 5, 6], dtype='str')
print(a)
print()

# Multi-dimensional Arrays

two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)
print()

# Getting items from a numpy array

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)
print()

first_column = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
third_column = two_dimension_array[:, 2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)
print()

# Slicing Numpy array

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
print()

# How to reverse the rows and the whole array?

a = two_dimension_array[::]
print(a)
print()

# Reverse the row and column positions

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_dimension_array[::-1, ::-1])
print()

# How to represent missing values ?

print(two_dimension_array)
two_dimension_array[1, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)
print()

numpy_zeroes = np.zeros((3, 3), dtype=int, order='C')
print(numpy_zeroes)
print()

numpy_ones = np.ones((3, 3), dtype=int, order='C')
print(numpy_ones)
print()

twos = numpy_ones * 2
print(twos)
print()

first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)
print(reshaped)
print()

flattened = reshaped.flatten()
print(flattened)
print()

np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print()

print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
print()

# Generating Random Numbers
random_float = np.random.random()
print(random_float)
print()

random_float = np.random.random(5)
print(random_float)
print()

random_int = np.random.randint(1, 10)
print(random_int)
print()

random_int = np.random.randint(1, 10, size=4)
print(random_int)
print()

random_int = np.random.randint(2, 10, size=(3, 3))
print(random_int)
print()

normal_array = np.random.normal(79, 15, 10)
print(normal_array)
print()

# numpy and statistics

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
plt.hist(normal_array, color='blue', bins=20)
# plt.show()


# matrix in numpy

four_by_four_matrix = np.matrix(np.ones((4, 4), dtype=float))
print(four_by_four_matrix)
print()
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)
print()

lst = range(0, 11, 2)
for i in lst:
    print(i)
print()

whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)
print()

even_number = np.arange(1, 20, 2)
print('even number is : ', even_number)
print()

odd_number = np.arange(2, 20, 2)
print('odd number is : ', odd_number)
print()

# Creating sequence of numbers using line space

print(np.linspace(1.0, 5.0, num=10))
print()
print(np.linspace(1.0, 5.0, num=5, endpoint=False))
print()
print(np.logspace(2, 4.0, num=4))
print()

x = np.array([1, 2, 3], dtype=np.complex128)
print(x)
print()

np_list = np.array([(1, 2, 3), (4, 5, 6)])
print('First row: ', np_list[0])
print('Second row: ', np_list[1])
print(np_list)
print()

print('First column: ', np_list[:, 0])
print('Second column: ', np_list[:, 1])
print('Third column: ', np_list[:, 2])

print()

# NumPy Statistical Functions with Example

np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)

print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ', two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())
print()

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array, axis=0))
print('Column with maximum: ', np.amax(two_dimension_array, axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array, axis=1))
print('Row with maximum: ', np.amax(two_dimension_array, axis=1))
print()

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array, axis=0))
print('Column with maximum: ', np.amax(two_dimension_array, axis=0))
print('=== Row ===')
print('Row with minimum: ', np.amin(two_dimension_array, axis=1))
print('Row with maximum: ', np.amax(two_dimension_array, axis=1))
print()

# How to create repeating sequences?

a = [1, 2, 3]

print('Tile:   ', np.tile(a, 2))
print('Repeat: ', np.repeat(a, 2))
print()

# how to generate random numbers

one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)
print()

r = np.random.random(size=[2, 3])
print(r)
print()

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
print()

rand = np.random.rand(2, 3)
print(rand)
print()

rand2 = np.random.randn(2, 2)
print(rand2)
print()

rand_int = np.random.randint(0, 10, size=[5, 3])
print(rand_int)
print()

from scipy import stats

np_normal_dis = np.random.normal(5, 0.5, 50)
print(np_normal_dis)
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
print()
plt.hist(np_normal_dis, color="grey", bins=21)
# plt.show()
print()

# Linear Algebra

f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
print(np.dot(f, g))
print()

# NumPy Matrix Multiplication with np.matmul()
h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
print(np.matmul(h, i))
print()

print(np.linalg.det(i))
print()

Z = np.zeros((8, 8))
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)
print()

new_list = [x + 2 for x in range(0, 11)]
print(new_list)
print()

np_arr = np.array(range(0, 11))
print(np_arr + 2)
print()

temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5
print(pressure)

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
# plt.show()
print()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
# plt.show()

