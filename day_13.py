# 13	List Comprehension
language = 'PYTHON'
lst = list(language)
print(type(lst))
print(lst)


name = 'KISHAN'
lst = [i for i in name]
print(type(lst))
print(lst)


even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)


odd_number = [i for i in range(10) if i % 2 != 0]
print(odd_number)



numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)


list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)

# 13	Lambda Function
# 13	Creating a Lambda Function

# using simple function
def add_two_nums(a, b):
    return a + b
print(add_two_nums(2, 3))

# using lambda function
add_two_nums = lambda a, b: a +b
print(add_two_nums(2, 3))


# Self invoking lambda function
(lambda a, b: a + b)(2,3)



square = lambda x : x ** 2
print(square(3))
cube = lambda x : x ** 3
print(cube(3))


multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))


# 13	Lambda Function inside Another Function

def power(x):
    return lambda n : x ** n
cube = power(2)(3)
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)


# 13	Exercises: Day 13

# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

positive_numbers = [i for i in numbers if i >= 0]
print(positive_numbers)


# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [number for sublist in list_of_lists for inner_list in sublist for number in inner_list]

print(flattened_list)


# Using list comprehension create the following list of tuples:

list_of_lists = [(i,1,i**1, i**2, i**3, i**4, i**5)for i in range(11)]
print(list_of_lists)


# Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
def get_abbreviation(name):
    return name[:3].upper()
output = [
    [name.upper(), get_abbreviation(name), capital.upper()]
    for sublist in countries
    for (name, capital) in sublist
]
print(output)


# Change the following list to a list of dictionaries:


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [
    {'country': name.upper(), 'city': capital.upper()}
    for sublist in countries
    for (name, capital) in sublist
]
print(output)


# Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [first + ' ' + last for sublist in names for (first, last) in sublist]

print(output)


# Write a lambda function which can solve a slope or y-intercept of linear functions.


slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda m, x, y: y - m * x

x1, y1 = 1, 2
x2, y2 = 3, 4
m = slope(x1, y1, x2, y2)

print(f"Slope: {m}")

x, y = 1, 2
b = y_intercept(m, x, y)

print(f"Y-intercept: {b}")

