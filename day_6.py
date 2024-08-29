# 6	Creating a Tuple
t = ()
t = tuple()
tpl = (10,20,30,40,50,60,70,)

# 6	Tuple length
print(len(tpl))

# 6	Accessing Tuple Items
print(tpl[0])
print(tpl[1])
print(tpl[2])
print(tpl[3])
print(tpl[4])
print(tpl[5])
print(tpl[6])
print(tpl[-1])
print(tpl[-2])

# 6	Slicing tuples
print(tpl[0:4])
print(tpl[-4:])
print(tpl[2:7])

# 6	Changing Tuples to Lists
lst = list(tpl)
print(lst)

# 6	Checking an Item in a Tuple
tpl = (10,20,30,40,50,60,70,)
a =32 in tpl
print(a)

# 6	Joining Tuples
tpl1 = (2,4,6,8)
tpl2 = (3,5,7,9)
print(tpl1+tpl2)

# 6	Deleting Tuples
del tpl1
del tpl2

# 6	Exercises: Level 1
# Create an empty tuple
tpl = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('rushil','vinesh', 'prince', 'navdip', 'chetan')
sisters = ('krupali', 'kavita', 'ankita', 'komal')

# Join brothers and sisters tuples and assign it to siblings
siblings = (brothers + sisters)
print(siblings)


# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
father_name = 'jayantibhai'
mother_name = 'varshaben'
family_members.append(father_name)
family_members.append(mother_name)
print(family_members)

# 6	Exercises: Level 2


# Unpack siblings and parents from family_members

siblings, father_name, mother_name = family_members[:-2], family_members[-2], family_members [-1]
print(siblings)
print(father_name)
print(mother_name)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('apple', 'banana', 'cherry')
vegetables = ('Carrot', 'Onion')
animals = ('lion', 'tiger', 'monkey')
food_stuff_tp = (fruits + vegetables + animals)
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middle = len(food_stuff_tp)//2
middle_items = food_stuff_lt[middle] if len(food_stuff_lt) % 2 != 0 else food_stuff_lt[middle-1:middle+1]
print(middle_items)

# Slice out the first three items and the last three items from food_staff_lt list

first3 = food_stuff_tp[:3]
print(first3)
last3 = food_stuff_tp[-3:]
print(last3)

# Delete the food_staff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp)


# Check if an item exists in tuple:

country = ('india', 'USA', 'UK', 'Africa', 'Estonia', 'Iceland')
print(country)
    # Check if 'Estonia' is a nordic country

a = 'Estonia' in country
print(a)

    # Check if 'Iceland' is a nordic country

b = 'Iceland' in country
print(b)























