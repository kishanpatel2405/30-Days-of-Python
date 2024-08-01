#------ 2	Variables

# variable is a name for storage
# it is start with a letter or the underscore character
# cannot start with a number or any alpha character

# Variable names are case-sensitive (a , A ) are Different
# example
firstname = 'kishan'
lastname = 'patel'
age = 21
city = 'Rajkot'
is_married = False
skill = ['python', 'mysql', 'java', 'html']

print(firstname, lastname, age, city, is_married,skill )


#------ 2	Data Types

# string is a immutable in python
string = str

# numeric just like int = 10, float = 10.5, complex = 10j
numeric = int, float, complex

# boolean datatype is True or False
boolean = bool


sequence = list, tuple, range

# list is a collection which is ordered and mutable. it allows duplicate members
l = [10,20,30,40]
print(type(l))
# tuple is a collection which is ordered and unchangeable. it allows duplicate members
t = (10,10,20,20,0,20,20)
print(type(t))
# range
x = range(6)
print(x)

# dictionary is a collection which is ordered and changeable. it is key value pair
mapping = dict
d = {
    'name' : 'kihan',
    'age' : 21
}
print(type(d))
# set is a collection which is unordered and unindexed. it is not allow duplicate members
# set = set
s = {'kishan', 21, 21, 12}
print(type(s))

#------ 2	Numbers

# three type of number in  python
# int
a = 10
print(type(a))
# float
b = 10.23
print(type(b))
# complex
c = 10j
print(type(c))

#------ 2	Built in functions

# abs() #this funcion conver negetive number into positive
# delattr()
# hash()
# memoryview()
# min()
# setattr()
# set()
# all()
# slice()
# next()
# hex()
# dir()
# any()
# ascii()
# divmod()
# id()
# object()
# sorted()
# bin()
# enumerate()
# input()
# oct()
# staticmethod()
# bool()
# eval()
# int()
# open()
# str()
# breakpoint()
# exec()
# isinstance()
# ord()
# sum()
# bytearray()
# filter()
# issubclass()
# pow()
# super()
# bytes()
# float()
# iter()
# print()
# tuple()
# callable()
# format()
# len()
# property()
# type()
# chr()
# frozenset()
# list()
# range()
# vars()
# classmethod()
# getattr()
# locals()
# repr()
# zip()
# compile()
# globals()
# map()
# reversed()
# __import__()
# complex()
# hasattr()
# max()
# round()
# help()
# dict()

#------ 2	Exercises-1
# 1- Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
import os
dir = 'kishann'
day_2 = 'day_2'
file_name = 'variables.py'
os.makedirs(os.path.join(dir, day_2), exist_ok=True)
with open(os.path.join(dir, day_2, file_name), 'w')as file:
    pass

# 2- Write a python comment saying 'Day 2: 30 Days of python programming'

# Day 2: 30 Days of python programming

# 3- Declare a first name variable and assign a value to it

file_name = 'kishan'

# 4- Declare a last name variable and assign a value to it

last_name = 'patel'

# 5- Declare a full name variable and assign a value to it

full_name = 'kishan patel'

# 6- Declare a country variable and assign a value to it

country = 'india'

# 7- Declare a city variable and assign a value to it

city = 'Rajkot'

# 8- Declare an age variable and assign a value to it

age = 21

# 9- Declare a year variable and assign a value to it

year = 2024

# 10- Declare a variable is_married and assign a value to it

is_married = False

# 11- Declare a variable is_true and assign a value to it

is_true = True

# 12- Declare a variable is_light_on and assign a value to it

is_light_on = False

# 13- Declare multiple variable on one line

a,b,c,d = 10,20,30,40




#------ 2	Exercises-2

# 1- Check the data type of all your variables using type() built-in function
a = 10
print(type(a))

b = 20.5
print(type(b))

c = 12j
print(type(c))

d = 'kishan'
print(type(d))

e = False
print(type(e))

f = [1,2,3,]
print(type(f))

g = (1,2,3,4)
print(type(g))

h = {12,3,4,5,6,76}
print(type(h))

i = {'a':'akil',
     'b':'zamir'}
print(type(i))

j = range(19)
print(type(j))

# 2- Using the len() built-in function, find the length of your first name

a = 'KISHAN'
print(len(a))

# 3- Compare the length of your first name and your last name

f = 'kishan'
l = 'patel'

if len(f)>len(l):
    print('first name is big')
elif len(l)>len(f):
    print('last name is big')
else:
    print('first and last both same')



# 4- Declare 5 as num_one and 4 as num_two
num1 = 5
num2 = 4
#     i- Add num_one and num_two and assign the value to a variable total
total = num1 + num2
print('total is : ',total)

#     ii- Subtract num_two from num_one and assign the value to a variable diff
diff = num1 - num2
print('subtraction is : ', diff)

#     iii- Multiply num_two and num_one and assign the value to a variable product
product = num1 * num2
print('multiply is : ', product)

#     iv- Divide num_one by num_two and assign the value to a variable division
division = num1 / num2
print('divide is : ', division)

#     v- Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num1 % num2
print('remainder is : ', remainder)

#     vi- Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num1 ** num2
print('power of this number is : ', exp)

#     vii- Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num1 // num2
print('floor division is : ', floor_division)

# 5- The radius of a circle is 30 meters.
radius = 30
pi = 3.14
#     i- Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pi * radius ** 2
print('area of circle is  ', area_of_circle)

#     ii- Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * pi * radius
print('circum of circle is : ', circum_of_circle)

#     iii-Take radius as user input and calculate the area.
radius_input= float(input('enter radius of circle : '))
area_input = pi*radius_input**2
print('area of given input  is : ', area_input)

# 6- Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('enter your first name : ')
last_name = input('enter your last name : ')
country  = input('enter your country : ')
age = int(input('enter your age : '))
print('first name is : ', first_name)
print('last name is : ', last_name)
print('country is : ', country)
print('agr is : ', age)

# 7- Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
import keyword
print(keyword.kwlist)

