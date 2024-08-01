# 3	Booleans

# it can hold two possible value
a = True
b = False
# it"s used for conditional statement, loop, decision-making

# 3	Assignment Operators

x = 10
print(x)
x += 3
print(x)
x -= 3
print(x)
x *= 3
print(x)
x /= 3
print(x)
x %= 2
print(x)
x //= 3
print(x)
x **= 3
print(x)

# 3	Arithmetic Operators

a = 10
b = 10
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
floor_division = a // b
exponentiation = a ** b
print('addition is : ', addition)
print('subtraction is : ', subtraction)
print('multiplication is : ', multiplication)
print('division is : ', division)
print('modulus is : ', modulus)
print('exponentiation is : ', exponentiation)
print('floor_division is : ', floor_division)

# 3	Comparison Operators

a = 10
b = 11
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 3	Logical Operators
# and
# or
# not

x = 100
print(x > 50 and x > 80)  # return true when both the condition is true
print(x < 150 or x > 90)  # return true when any one condition is true
print(not (50 < x < 150))  # return the false if the condition is true

# 3	Exercises

# 1 Declare your age as integer variable

age = 21

# 2 Declare your height as a float variable

height = 5.5

# 3 Declare a variable that store a complex number

com = 10j

# 4 Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).


# base = float(input('Enter a base value : '))
# height = float(input('Enter a height value : '))
# area = 0.5 * base * height
# print('the area of triangle is : ', area)

# 5 Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

# side_a = int(input('enter a side a : '))
# side_b = int(input('enter a side b : '))
# side_c = int(input('enter a side c : '))
# perimeter = side_a + side_b + side_c
# print('perimeter of the triangle is : ', perimeter)

# 6 Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

# length = int(input('enter a length : '))
# width = int(input('enter a width : '))
# area = length * width
# perimeter = 2 * (length + width)
# print('area of rectangle is : ', area)
# print('perimeter of rectangle is : ', perimeter)

# 7 Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

# radius = int(input('enter a radius of a circle : '))
# pi = 3.14
# area = pi * radius * radius
# circumference = 2 * pi * radius
# print('the area of circle is : ', area)
# print('the circumference of circle is : ', circumference)

# 8 Calculate the slope, x-intercept and y-intercept of y = 2x -2

m = 2
b = -2
slope = m
y_intercept = b
x_intercept = -b / m
print('slope : ', slope)
print('y_intercept : ', y_intercept)
print('x_intercept : ', x_intercept)

# 9 Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1, y1 = 2, 2
x2, y2 = 6, 10
slope_task9 = (y2 - y1) / (x2 - x1)
x_diff_squared = (x2 - x1) ** 2
y_diff_squared = (y2 - y1) ** 2
sum_of_squares = x_diff_squared + y_diff_squared
guess = sum_of_squares
num_iterations = 10
for _ in range(num_iterations):
    guess = (guess + sum_of_squares / guess) / 2
distance = guess ** 0.5
print('slope : ', slope)
print('distance : ', distance)

# 10 Compare the slopes in tasks 8 and 9.

slope_task8 = 2
y_intercept_task8 = -2
x_intercept_task8 = 1
print("Task #8 Results:")
print("Slope:", slope_task8)
print("Y-intercept:", y_intercept_task8)
print("X-intercept:", x_intercept_task8)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_task9 = (y2 - y1) / (x2 - x1)
x_diff_squared = (x2 - x1) ** 2
y_diff_squared = (y2 - y1) ** 2
sum_of_squares = x_diff_squared + y_diff_squared
guess = sum_of_squares
num_iterations = 10
for _ in range(num_iterations):
    guess = (guess + sum_of_squares / guess) / 2
distance_task9 = guess ** 0.5
print("\nTask #9 Results:")
print("Slope:", slope_task9)
print("Euclidean Distance:", distance_task9)
print("\nTask #10 Comparison:")
if slope_task8 == slope_task9:
    print("The slopes are the same.")
else:
    print("The slopes are different.")

# 11 Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
for x in x_values:
    y = x ** 2 + 6 * x + 9
    print("For x = {}, y = {}".format(x, y))
    if y == 0:
        print("The value of x where y = 0 is:", x)
        break

# 12 Find the length of 'python' and 'dragon' and make a falsy comparison statement.

p = 'python'
d = 'dragon'
print(len(p))
print(len(d))
if len(p) == len(d):
    print('both the length are same')
else:
    print('both length are not same')

# 13 Use and operator to check if 'on' is found in both 'python' and 'dragon'

p = 'python'
d = 'dragon'
if 'on' in p and d:
    print('yes')
else:
    print('np')

# 14 I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

s = 'I hope this course is not full of jargon'
print('jargon' in s)

# 15 There is no 'on' in both dragon and python

p = 'python'
d = 'dragon'
print(not ('on' in p and d))

# 16 Find the length of the text python and convert the value to float and convert it to string

p = 'python'
print(len(p))
print(float(len(p)))
print(p)

# 17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

n = 11
if n % 2 == 0:
    print('even')
else:
    print('odd')

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

f = 7 // 3
convert = int(f)
equal = f == convert
print('floor division value is : ', f)
print('converted value is : ', convert)
print('equal value is : ', equal)

# 19 Check if type of '10' is equal to type of 10

a = '10'
b = 10
print(type(a))
print(type(b))
if a == b:
    print('both type are same')
else:
    print('Not same')

# 20 Check if int('9.8') is equal to 10

if 9.0 == 10:
    print('yes')
else:
    print('no')

# 21 Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

# hours = float(input('enter hours : '))
# rate = float(input('enter rate : '))
# pay = hours * rate
# print('total pay is : ', pay)21

# 22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

live = 100
years = int(input('enter a years : '))
remaining_year = live - years
second = remaining_year * 365 * 86400
print('total second remaining is : ', second)

# 23 Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

n = 5
for i in range(1, n + 1):
    first = i
    second = 1
    third = i
    fourth = i * 1
    fifth = i * i * i
    s = str(first) + ' ' + str(second) + ' ' + str(third) + ' ' + str(fourth) + ' ' + str(fifth)
    print(s)