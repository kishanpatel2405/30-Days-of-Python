# 8	Creating a Dictionary
d = {}
print(type(d))
d = {'name' : 'kishan'}
print(d)
# 8	Dictionary Length
print(len(d))

# 8	Accessing Dictionary Items

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['country'])
print(person['is_marred'])
print(person['skills'])
print(person['skills'][0])
print(person['skills'][1])
print(person['address']['street'])
# print(person['city'])



# 8	Adding Items to a Dictionary

dct = {1 : 'kishan',
       2 : 'zamir',
       3 : 'prem',
       4 : 'vinesh',}
print(dct)
dct['job'] = 'python_developer'
print(dct)
person['skills'].append('HTML')
print(person)

# 8	Modifying Items in a Dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
print(dct)

# 8	Checking Keys in a Dictionary

print('key2' in dct)


# 8	Removing Key and Value Pairs from a Dictionary

dct.pop('key1')
print(dct)

# 8	Changing Dictionary to a List of Items

print(dct.items())

# 8	Clearing a Dictionary

print(dct.clear())

# 8	Deleting a Dictionary

del dct
# 8	Copy a Dictionary

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct2 = dct.copy()
print(dct2)

# 8	Getting Dictionary Keys as a List

keys = dct.keys()
print(keys)

# 8	Getting Dictionary Values as a List

values = dct.values()
print(values)

# 8	Exercises

# Create an empty dictionary called dog

dog = {}

# Add name, color, breed, legs, age to the dog dictionary

dog = {
    'name' : 'rony',
    'color' : 'black',
    'breed' : 'dKFDVD',
    'legs' : 'dscb',
    'age' : 2
}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {
    'first_name' : 'kishan',
    'last_name' : 'patel',
    'gender' : 'male',
    'age' : 21,
    'marital_status' : 'married',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country' : 'india',
    'city' : 'Rajkot',
    'address' : 'padek Road'
}
print(student)

# Get the length of the student dictionary

print(len(student))

# Get the value of skills and check the data type, it should be a list

print(student['skills'])
print(type(student['skills']))

# Modify the skills values by adding one or two skills

add = 'java', 'devops'
student['skills'] = add
print(student)

# Get the dictionary keys as a list
student = {
    'first_name' : 'kishan',
    'last_name' : 'patel',
    'gender' : 'male',
    'age' : 21,
    'marital_status' : 'married',
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country' : 'india',
    'city' : 'Rajkot',
    'address' : 'padek Road'
}
a = student.keys()
print(a)


# Get the dictionary values as a list

a = student.values()
print(a)

# Change the dictionary to a list of tuples using items() method

a = student.items()
print(a)

# Delete one of the items in the dictionary

student.clear()
print(student)

# Delete one of the dictionaries
del student
