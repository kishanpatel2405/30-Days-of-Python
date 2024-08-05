# 9	Conditionals

# 9	If Condition

a = 12
if a > 0:
    print('a is a big number compare to the zero')

# 9	If Else

if a < 0:
    print('a is a big number compare to the o')
else:
    print('zero is small number compare to the a')

# 9	If Elif Else

a = 0
if a < 0:
    print('a is a big number compare to the o')
elif a == 0:
    print('both the value is equal')
else:
    print('zero is small number compare to the a')

# 9	Short Hand

a = 10
b = 5
print('a is positive') if a > b else print('a is negative')

# 9	Nested Conditions

a = 0
if a > 0:
    if a % 2 == 0:
        print('a is positive and even number')
    else:
        print('a is positive')
elif a == 0:
    print('a is zero')
else:
    print('a is negative number')

# 9	If Condition and Logical Operators

a = 0
if a > 0 and a % 2 == 0:
    print('a is positive and even number')
elif a < 0 and a % 2 != 0:
    print('a is positive')
elif a == 0:
    print('a is zero number')
else:
    print('a is negative')

# 9	If and Or Logical Operators

user = 'kishan'
level = 3
if user == 'kishan' or level >= 4:
    print('access')
else:
    print('no access')

# 9	Exercises
# 9	Exercises: Level 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years. Output:

# age = int(input('how old are you? : '))
age = 30
if age >= 18:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”)
# to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for
# bigger differences, and a custom text if my_age = your_age.

# my_age = int(input('Enter your age: '))
# your_age = int(input('Enter your age: '))
my_age = 32
your_age = 33

if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print("You are 1 year older than your friend.")
    else:
        print(f"You are {difference} years older than your friend.")
elif my_age < your_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than your friend.")
    else:
        print(f"You are {difference} years older than your friend.")
else:
    print('you and my friend age are same')

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b
# return a is smaller than b, else a is equal to b.

# a = int(input('enter a number: '))
# b = int(input('enter another number: '))
a = 4
b = 3
if a > b:
    print('a is greater then b')
elif a < b:
    print('b is greater then a')
else:
    print('a is equal to b')

# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

# score = int(input('Enter your score: '))
score = 80
if 80 <= score <= 100:
    print('A')
elif 70 <= score <= 80:
    print('B')
elif 60 <= score <= 70:
    print('C')
elif 50 <= score <= 60:
    print('D')
else:
    print('F')

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November,
# the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is
# Spring June, July or August, the season is Summer


# month = input('Enter a month: ').strip().lower()
month = 'march'
if month in ['september', 'october', 'november']:
    print('Season is Autumn')
elif month in ['december', 'january', 'february']:
    print('Season is Winter')
elif month in ['march', 'april', 'may']:
    print('Season is Spring')
elif month in ['june', 'july', 'august']:
    print('Season is Summer')
else:
    print('Invalid month')

# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

# add_fruits = input('Enter the fruits you want to add: ')
add_fruits = 'watermelon'
if add_fruits in fruits:
    print('it is already exist in the list')
else:
    fruits.append(add_fruits)
    print(fruits)

# Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# *Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    middle_skill = skills[middle_index]
    print(middle_skill)
else:
    print('skill in not in dictionary')


# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if 'skills' in person:
    skills = person['skills']
    if 'python' in skills:
        print("person's skills are python")
    else:
        print("person's skills are not python")
else:
    print('no skills in dictionary')

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has
# Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB,
# Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can
# be nested!

if 'skills' in person:
    skills = person['skills']
    skills_set = set(skills)
    if skills_set == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("He is a fullstack developer")
    else:
        print("Unknown title")
else:
    print('No skills key in dictionary')

# If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

if 'is_marred' and 'address'=='Finland' in person['is_marred']:
    print('Asabeneh Yetayeh lived in finland. he is married')
else:
    print('Asabeneh Yetayeh lived in not married. he is not married')