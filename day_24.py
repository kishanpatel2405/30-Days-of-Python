# 24	Python for Statistical Analysis
# 24	Statistics
# 24	Data
# 24	Statistics Module
# 24	NumPy
# 24	Importing NumPy

import numpy as np

print(np.__version__)
print(dir(np))

# 24	Creating int numpy arrays

# Creating python List
python_list = [1, 2, 3, 4, 5]
print('Type:', type(python_list))
print(python_list)
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(two_dimensional_list)
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# 24	Creating float numpy arrays

lst = [12, 13, 14, 15, 16]
num_lst = np.array(lst, dtype=float)
print(num_lst)

# 24	Creating Boolean numpy arrays

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

# 24	Creating multidimensional array using numpy

lst = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
lst_np = np.array(lst)
print(lst_np)
print(type(lst_np))

# 24	Converting numpy array to list

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', lst_np.tolist())

# 24	Creating numpy array from tuple

tpl = (10, 20, 30, 40, 50)
print(type(tpl))
print(tpl)
np_tpl = np.array(tpl)
print(np_tpl)
print(type(np_tpl))
print()

# 24	Shape of numpy array

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
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

# 24	Data type of numpy array

int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
print()

# 24	Size of a numpy array

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])
print('The size:', numpy_array_from_list.size)
print('The size:', two_dimensional_list.size)
print()

# 24	Mathematical Operation using numpy

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modules (%)
# Floor Division(//)
# Exponential(**)

# 24	Addition

lst = [1, 2, 3, 4, 5]
num_lst = np.array(lst)
ten_plus = num_lst + 10
print(ten_plus)
print()

# 24	Subtraction

lst = [1, 2, 3, 4, 5]
num_lst = np.array(lst)
ten_plus = num_lst - 10
print(ten_plus)
print()

# 24	Multiplication

lst = [1, 2, 3, 4, 5]
num_lst = np.array(lst)
ten_plus = num_lst * 10
print(ten_plus)
print()

# 24	Division

lst = [1, 2, 3, 4, 5]
num_lst = np.array(lst)
ten_plus = num_lst / 10
print(ten_plus)
print()

# 24	Modulus

lst = [1, 2, 3, 4, 5]
num_lst = np.array(lst)
ten_plus = num_lst % 3
print(ten_plus)
print()

# 24	Floor Division

lst = [1, 2, 3, 4, 5]
num_lst = np.array(lst)
ten_plus = num_lst // 10
print(ten_plus)
print()

# 24	Exponential

lst = [1, 2, 3, 4, 5]
num_lst = np.array(lst)
ten_plus = num_lst ** 2
print(ten_plus)
print()

# 24	Checking data types

numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')
print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
print()

# 24	Converting types

# int to float
arr = np.array([1, 2, 3, 4, 5], dtype=float)
print(arr)
print()

# float to int
arr = np.array([1.2, 21.32, 23.00], dtype=int)
print(arr)
print()

# int to bool
arr = np.array([0, -1, -2, 0, 1], dtype=bool)
print(arr)
print()

# int to str
arr = np.array([23, 3, 53, 41], dtype=str)
print(arr)
print()

# 24	Multi-dimensional Arrays

two_dimension_array = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(type(two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)
print()

# 24	Getting items from a numpy array

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print(first_row)
print(second_row)
print(third_row)
print()

# 24	Slicing Numpy array

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
print()

# 24	How to reverse the rows and the whole array?

a = two_dimension_array[::]
print(a)
print()

# 24	Reverse the row and column positions

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = two_dimension_array[::-1, ::-1]
print(a)
print()

# 24	How to represent missing values ?

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

# 24	Generating Random Numbers

rnd_float = np.random.random()
print(rnd_float)
print()

rnd_float = np.random.random(5)
print(rnd_float)
print()

rnd_float = np.random.randint(0, 10)
print(rnd_float)
print()

rnd_int = np.random.randint(0, 10, 5)
print(rnd_int)
print()

rnd_int = np.random.randint(2, 10, size=(3, 3))
print(rnd_int)
print()

# 24	Generating Random Numbers

arr = np.random.normal(12, 42, 53)
print(arr)
print()

# 24	Numpy and Statistics

arr = np.random.normal(12, 42, 53)
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
plt.hist(arr, color="grey", bins=50)
print()

# 24	Matrix in numpy

four = np.matrix(np.ones((4, 4), dtype=float))
print(four)
print()

np.asarray(four)[2] = 2
print(np.asarray(four))
print()

# 24	Numpy numpy.arange()
# 24	What is Arrange?

lst = range(0, 11, 2)
for i in lst:
    print(i)
print()

whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)
print()

natural_numbers = np.arange(1, 20, 1)
print(natural_numbers)
print()

odd = np.arange(1, 20, 2)
print(odd)
print()

even = np.arange(2, 20, 2)
print(even)
print()

# 24	Creating sequence of numbers using line space

a = np.linspace(1.0, 5.0, num=10)
print(a)
print()

a = np.linspace(1.0, 5.0, num=5, endpoint=False)
print(a)
print()

a = np.logspace(2, 4.0, num=4)
print(a)
print()

x = np.array([1, 2, 3], dtype=np.complex128)
print(x)
print()

np_list = np.array([(1, 2, 3), (4, 5, 6)])
print(np_list)
print('First row: ', np_list[0])
print('Second row: ', np_list[1])
print('First column: ', np_list[:, 0])
print('Second column: ', np_list[:, 1])
print('Third column: ', np_list[:, 2])
print()

# 24	NumPy Statistical Functions with Example

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
print('=================================== Row =================================')
print('Row with minimum: ', np.amin(two_dimension_array, axis=1))
print('Row with maximum: ', np.amax(two_dimension_array, axis=1))
print()

# 24	How to create repeating sequences?

a = [1, 2, 3]
print('Tile:   ', np.tile(a, 2))
print('Repeat: ', np.repeat(a, 2))
print()

r = np.random.random(size=[2, 3])
print(r)
print()

# 24	How to generate random numbers?

one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)
print()

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
print()

rand = np.random.rand(2, 2)
print(rand)
rand2 = np.random.randn(2, 2)
print(rand2)
print()

rand_int = np.random.randint(0, 10, size=[5, 3])
print(rand_int)
print()

from scipy import stats

np_normal_dis = np.random.normal(5, 0.5, 1000)
print(np_normal_dis)
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
print()

# 24	Linear Algebra

f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
print(np.dot(f, g))
print()

# 24	NumPy Matrix Multiplication with np.matmul()

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
print()

plt.plot(temp, pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
print()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x)
ax.set(xlabel="x", ylabel='y')
plt.show()
print()

# 24	Summery

# 24	Exercises: Day 24

# Arrays support vectorized operations, while lists don’t.
# Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
# Every array has one and only one dtype. All items in it should be of that dtype.
# An equivalent numpy array occupies much less space than a python list of lists.
# numpy arrays support boolean indexing.

# Repeat all the examples



