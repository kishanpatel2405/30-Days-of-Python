# 14	Higher Order Functions
from functools import reduce


# 14	Function as a Parameter

def sum_numbers(nums):
    return sum(nums)


def higher_order_function(f, lst):
    summation = f(lst)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)


# 14	Function as a Return Value


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3))
result = higher_order_function('absolute')
print(result(-3))


# 14	Python Closures

def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))


# 14	Python Decorators


# 14	Creating Decorators


def greeting():
    return 'Welcome to Python'


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


g = uppercase_decorator(greeting)
print(g())


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def greeting():
    return 'Welcome to Python'


print(greeting())


# 14	Applying Multiple Decorators to a Single Function


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'


print(greeting())


# 14	Accepting Parameters in Decorator Functions


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))


print_full_name("kishan", "patel", 'india')

# 14	Built-in Higher Order functions

# 14	Python - Map Function


numbers = [1, 2, 3, 4, 5]


def square(x):
    return x ** 2


numbers_squared = map(square, numbers)
print(list(numbers_squared))
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))

numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))

names = ['kishan', 'janvi', 'prem', 'vinesh']


def change_to_upper(name):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

# 14	Python - Filter Function


numbers = [1, 2, 3, 4, 5]


def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))

numbers = [1, 2, 3, 4, 5]


def is_odd(num):
    if num % 2 != 0:
        return True
    return False


odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))

names = ['kishankumar', 'Lidiya', 'Ermias', 'Abraham']


def is_name_long(name):
    if len(name) > 7:
        return True
    return False


long_names = filter(is_name_long, names)
print(list(long_names))

# 14	Python - Reduce Function

numbers_str = ['1', '2', '3', '4', '5']


def add_two_nums(x, y):
    return int(x) + int(y)


total = reduce(add_two_nums, numbers_str)
print(total)

# 14	Exercises: Level 1
# Explain the difference between map, filter, and reduce.
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x ** 2, numbers)

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)

from functools import reduce

numbers = [1, 2, 3, 4]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)


# Explain the difference between higher order function, closure and decorator

# higher_order_function
def apply_function(f, x):
    return f(x)


def square(n):
    return n * n


result = apply_function(square, 5)


# closure
def make_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


double = make_multiplier(2)
print(double(5))


# decorator
def decorator_function(original_function):
    def wrapper_function():
        print("Something is happening before the function is called.")
        original_function()
        print("Something is happening after the function is called.")

    return wrapper_function


@decorator_function
def say_hello():
    print("Hello!")


say_hello()


# Define a call function before map, filter or reduce, see examples.


def double(x):
    return x * 2


numbers = [1, 2, 3, 4]
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))


def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))


def add(x, y):
    return x + y


numbers = [1, 2, 3, 4]
total = reduce(add, numbers)
print(total)

# Use for loop to print each country in the countries list.

country = ['India', 'Japan', 'US', 'UK', 'America']
for i in country:
    print(i)

# Use for to print each name in the names list.

name = ['kishan', 'vinesh', 'prem', 'raj', 'zamir', 'sumi', 'janki']

for n in name:
    print(n)

# Use for to print each number in the numbers list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)

# 14	Exercises: Level 2

# Use map to create a new list by changing each country to uppercase in the countries list

country = ['india', 'japan', 'usa']


def to_upper(country):
    return country.upper()


upper_country = map(to_upper, country)

print(list(upper_country))

# Use map to create a new list by changing each number to its square in the numbers list

numbers = [1, 2, 3, 4, 5]


def to_square(number):
    return number * number


squared_numbers = map(to_square, numbers)
print(list(squared_numbers))

# Use map to change each name to uppercase in the names list

names = ['kishan', 'vinesh', 'uttam', 'khusbu', 'radhika']


def to_upper(name):
    return name.upper()


upper_name = map(to_upper, names)
print(list(upper_name))

# Use filter to filter out countries containing 'land'.

countries = ['Finland', 'Iceland', 'Ireland', 'Sweden', 'Norway', 'New Zealand']


def contain_land(contry):
    return 'land' in contry.lower()


filter_country = filter(contain_land, countries)
print(list(filter_country))

# Use filter to filter out countries having exactly six characters.

countries = ['Finland', 'Iceland', 'Ireland', 'Sweden', 'Norway', 'New Zealand']


def six_char(contry):
    return len(contry) == 6


filter_country = filter(six_char, countries)
print(list(filter_country))

# Use filter to filter out countries containing six letters and more in the country list.

countries = ['finland', 'Iceland', 'Ireland', 'Sweden', 'Norway', 'New Zealand', 'india', 'uk']


def six_or_more(contry):
    return len(contry) >= 6


filter_country = filter(six_or_more, countries)
print(list(filter_country))

# Use filter to filter out countries starting with an 'E'


countries = ['finland', 'Iceland', 'Ireland', 'Sweden', 'Norway', 'New Zealand', 'india', 'uk', 'Enn', "EUMS"]


def start_e(contry):
    return contry.startswith('E')


filter_country = filter(start_e, countries)
print(list(filter_country))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
sums = map(lambda x, y: x + y, numbers1, numbers2)
filtered_sums = filter(lambda x: x > 25, sums)
product = reduce(lambda x, y: x * y, filtered_sums)
print(product)


# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.


def get_string_lists(lst):
    return [item for item in lst if isinstance(item, str)]


ex_lst = [12, 'kihn', 'kris', 'ksnjk', 32]
str_lst = get_string_lists(ex_lst)
print(str_lst)

# Use reduce to sum all the numbers in the numbers list.


from functools import reduce

numbers = [1, 2, 3, 4, 5]


def add(x, y):
    return x + y


total_sum = reduce(add, numbers)
print(total_sum)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries


from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

concatenated_countries = reduce(
    lambda acc, country: f"{acc}, {country}" if acc else country,
    countries
)
if len(countries) > 1:
    final_sentence = concatenated_countries.rsplit(', ', 1)
    final_sentence = f"{final_sentence[0]}, and {final_sentence[1]} are north European countries"
else:
    final_sentence = concatenated_countries + " are north European countries"
print(final_sentence)



# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can
# find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

def categorize_countries(countries, pattern):
    return [country for country in countries if pattern.lower() in country.lower()]

countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
    'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
    'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo',
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark',
    'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador',
    'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji',
    'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece',
    'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
    'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
    'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North',
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
    'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia',
    'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',
    'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
    'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau',
    'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
    'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore',
    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain',
    'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria',
    'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago',
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
    'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
    'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

pattern = 'land'
filtered_countries = categorize_countries(countries, pattern)
print(filtered_countries)


# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.


def count_countries_by_initial(countries):
    letter_count = {}
    for country in countries:
        if country:
            initial_letter = country[0].upper()
            if initial_letter in letter_count:
                letter_count[initial_letter] += 1
            else:
                letter_count[initial_letter] = 1
    return letter_count
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
    'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
    'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo',
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark',
    'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador',
    'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji',
    'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece',
    'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
    'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
    'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North',
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
    'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia',
    'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',
    'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
    'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau',
    'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
    'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore',
    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain',
    'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria',
    'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago',
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
    'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
    'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]
letter_counts = count_countries_by_initial(countries)
print(letter_counts)

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.


def get_first_ten_countries(countries):
    return countries[:10]

countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
    'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
    'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo',
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark',
    'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador',
    'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji',
    'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece',
    'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
    'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
    'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North',
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
    'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia',
    'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',
    'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
    'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau',
    'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
    'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore',
    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain',
    'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria',
    'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago',
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
    'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
    'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

firtst_10 = get_first_ten_countries(countries)
print(firtst_10)

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.


def get_last_ten_countries(countries):
    return countries[-10:]

countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
    'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
    'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo (Brazzaville)', 'Congo',
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark',
    'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador',
    'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji',
    'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece',
    'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
    'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
    'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North',
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
    'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia',
    'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',
    'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
    'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau',
    'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
    'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
    'Senegal', 'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore',
    'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain',
    'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria',
    'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago',
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
    'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
    'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]


result = get_last_ten_countries(countries)
print(result)

# 14	Exercises: Level 3



# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
    # Sort countries by name, by capital, by population


from countries_data import countries_data

sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
# print(sorted_by_name)
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])
# print(sorted_by_capital)
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
# print(sorted_by_population)


    # Sort out the ten most spoken languages by location.

from collections import Counter
all_languages = [language for country in countries_data for language in country['languages']]
language_counts = Counter(all_languages)
most_common_languages = language_counts.most_common(10)
print(most_common_languages)


    # Sort out the ten most populated countries.


def get_top_ten_populated_countries(countries):
    sorted_by_population = sorted(countries, key=lambda x: x['population'], reverse=True)
    top_ten_populated_countries = sorted_by_population[:10]
    return top_ten_populated_countries
top_ten_countries = get_top_ten_populated_countries(countries_data)
print("Top ten most populated countries:")
for country in top_ten_countries:
    print(f"{country['name']} - Population: {country['population']}")



