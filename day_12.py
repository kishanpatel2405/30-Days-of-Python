# 12	What is a Module


# 12	Creating a Module

# 12	Importing a Module

import my_module

print(my_module.generate_full_name('kishan', 'patel'))

# 12	Import Functions from a Module
# 12	Import Functions from a Module and Rena
# 12	Import Built-in Modules
# 12	OS Module
# 12	Sys Module
# 12	Statistics Module

from statistics import *

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# 12	Math Module

import math

print(math.pi)
print(math.sqrt(2))
print(math.pow(2, 3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))

from math import pi as PI

print(PI)

# 12	String Module

import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# 12	Random Module

import random

print(random.randint(1, 100))

# 12	Exercises: Level 1

# Writ a function which generates a six digit/character random_user_id.

import random
import string


def random_user_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

print(random_user_id())

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters, but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_id_gen_by_user():
    # num = int(input('Enter a number: '))
    # num_id = int(input('enter a number of id :  '))
    num = 16
    num_id = 5

    characters = string.ascii_letters + string.digits

    for _ in range(num_id):
        random_user_id = ''.join(random.choice(characters) for _ in range(num))
        print(random_user_id)
user_id_gen_by_user()



# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

import random
def rgb_color_gen():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red, green, blue)

print(rgb_color_gen())

# 12	Exercises: Level 2

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal
# numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the
# alphabet, a-f. Check the task 6 for output examples).

import random

def list_of_hexa_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        colors.append(color)
    return colors

print(list_of_hexa_colors(5))


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random
def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        colors.append((red, green, blue))
    return colors
print(list_of_rgb_colors(5))


# Write a function generate_colors which can generate any number of hexa or rgb colors.

import random
def generate_colors(color_type, num_colors):
    colors = []
    for _ in range(num_colors):
        if color_type == 'hexa':
            color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        elif color_type == 'rgb':
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            color = f'rgb({red}, {green}, {blue})'
        else:
            raise ValueError("Invalid color type. Use 'hexa' or 'rgb'.")
        colors.append(color)
    return colors

generate_colors('hexa', 3)
generate_colors('hexa', 1)
generate_colors('rgb', 3)
generate_colors('rgb', 1)


# 12	Exercises: Level 3

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

lst = ['apple', 'banana', 'mango']
print(shuffle_list(lst))


# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

import random
def unique_numbers():
    return random.sample(range(10), 7)
print(unique_numbers())
