# 17	Exception Handling

try:
    print(100 + 500)
except:
    print('something went wrong')

try:
    name = 'kishan'
    born = 2003
    age = name - born
except:
    print('something went wrong')

try:
    name = 'kishan'
    year_born = 2003
    age = 2024 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occurred')
except ValueError:
    print('Value error occurred')
except ZeroDivisionError:
    print('zero division error occurred')

try:
    name = 'kishan'
    year_born = 2003
    age = 2024 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')

try:
    name = 'kishan'
    year_born = 2003
    age = 2024 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)


# 17	Packing and Unpacking Arguments in Python

# 17	Unpacking Lists

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e


lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

numbers = range(2, 7)
print(list(numbers))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)


# 17	Unpacking Dictionaries

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'


dct = {'name': 'kishan', 'country': 'india', 'city': 'Rajkot', 'age': 21}
print(unpacking_person_info(**dct))


# 17	Packing
# 17	Packing Lists


def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))


# 17	Packing Dictionaries

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs


print(packing_person_info(name="kishan",
                          country="India", city="Rajkot", age=21))

# 17	Spreading in Python

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)


# 17	Enumerate

for index, item in enumerate([20, 30, 40]):
    print(index, item)

for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

# 17	Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)


# 17	Exercises: Day 17


# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries
# and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.


names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
nordic_countries = names[:5]
es = names[5]
ru = names[6]
print("Nordic countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)
