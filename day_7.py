# 7	Creating a Set

s = set()
s1 = {1, 2, 3, 4, 4, 4}
# 7	Getting Set's Length
print(s1)

# 7	Accessing Items in a Set

# 7	Checking an Item

print(s1)
print(4 in s1)

# 7	Adding Items to a Set

s1.add(5)
print(s1)

# 7	Removing Items from a Set

s1.remove(4)
print(s1)

# 7	Clearing Items in a Set

s1.clear()
print(s1)

# 7	Deleting a Set

st = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
del st
# print(st)

# 7	Converting List to Set

l = [1, 2, 3, 4, 4, 4]
l = set(l)
print(l)

# 7	Joining Sets

st = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
st1 = {1, 2, 3, 4, 4, 4}
st2 = st1.union(st)
print(st2)

# 7	Finding Intersection Items

s1 = {'kishan', 'vinesh', 'prem'}
s2 = {'kishan', 'fogg', 'silentmary'}
print(s1.intersection(s2))

# 7	Checking Subset and Super Set

print(s2.issubset(s1))
print(s1.issuperset(s2))

whole_number = {1, 3, 5, 7, 9}
even_number = {2, 4, 6, 8}
print(whole_number.issubset(even_number))
print(even_number.issubset(whole_number))

# 7	Checking the Difference Between Two Sets

print(whole_number.difference(even_number))
print(even_number.difference(whole_number))

# 7	Finding Symmetric Difference Between Two Sets

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.symmetric_difference(st1))

# 7	Joining Sets

s1 = {1, 2, 34, 5}
s = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
print(s2.isdisjoint(s1))

# 7	Exercises: Level 1
# Find the length of the set it_companies

it_companies = {'deftBox', 'Google', 'IBM'}
print(len(it_companies))

# Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies

update_cmp = {'ks', 'dev', 'coursera'}
it_companies.update(update_cmp)
print(it_companies)

# Remove one of the companies from the set it_companies

it_companies.clear()
print(it_companies)

# What is the difference between remove and discard

num = {1, 2, 3, 45, 45}
print(num.discard(3))
print(num)

num = {12, 23, 4, 42}
num.remove(12)
print(num)

# 7	Exercises: Level 2

# Join A and B

a = {12, 21, 23, 24, 55, 3, 6}
b = {6, 653, 25, 134, 32, 53, 3}
c = a.union(b)
print(c)

# Find A intersection B

z = a.intersection(b)
print(z)

# Is A subset of B

c = b.issubset(a)
print(c)

# Are A and B disjoint sets

c = a.isdisjoint(b)
print(c)

# Join A with B and B with A

a = {12, 21, 23, 24, 55, 3, 6}
b = {6, 653, 25, 134, 32, 53, 3}
print(a.union(b))
print(b.union(a))

# What is the symmetric difference between A and B

# Define sets A and B
A = {1, 2, 3}
B = {3, 4, 5}

symmetric_difference = A.symmetric_difference(B)
print(symmetric_difference)

# Delete the sets completely

del a
del b
# print(a)

# 7	Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?

ages_list = [25, 30, 25, 40, 30, 50, 40, 60]
ages_set = set(ages_list)
list_length = len(ages_list)
set_length = len(ages_set)

if list_length > set_length:
    print("The list is bigger in length.")
elif list_length < set_length:
    print("The set is bigger in length.")
else:
    print("The list and the set have the same length.")

# Explain the difference between the following data types: string, list, tuple and set

# sting is immutable
my_string = "Hello, World!"
# list is ordered and mutable datatype
my_list = [1, 2, 3, "apple", 4.5]
# tuple is ordered and immutable datatype
my_tuple = (1, 2, 3, "apple", 4.5)
# set is unordered and unique elements access
my_set = {1, 2, 3, "apple", 4.5}


# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

s = 'I am a teacher and I love to inspire and teach people.'

char = s.split()
print(char)
unique_chars = set(char)
print(unique_chars)