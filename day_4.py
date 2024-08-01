# 4	String - Creating a String

# creating a string in python single or double quotation marks.
print('kishan')
print("kishan")
print('i am kishan"s kishan')
a = 'kihan'
print(a)
aa = """Aparagraph is a series of sentences that are organized and coherent, 
and are all related to a single topic.
Almost every piece of writing you do that is longer than a few sentences should be organized into paragraphs."""
# print(a)
print(aa[1])
# for x in aa:
#     print(x)


# 4	String - String Concatenation

f = "kishan "
l = "patel"
print(f+l)

# 4	String - Escape Sequences in Strings

# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

a = ('hi,\nwhat is your name?')
print(a)
a = ('hi,\thow are you')
print(a)
a = ('hi\\hello')
print(a)
a = "hi kishan\'s brother"
print(a)
a = "hi kishan\"s brother"
print(a)

# 4	String - String formatting

f = 'kishan'
l = 'patel'
print('my first name %s and my last name %s' %(f,l))

# 4	String - Python Strings as Sequences of Characters

language = 'Python'
print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
print(language[0:6])
print(language[1:4])
print(language[2:3])
print(language[::-1])

# 4	String - String Methods

a = 'hi what are you doingggggg?'
b = 12
print(a.capitalize())
print(a.count('a'))
print(a.endswith('ing'))
# print(a.expandtabs(10))
print(a.find('you'))
print(a.rfind('you'))
print(a.index('d'))
print(a.isalnum())
# print(a.isalpha())
print(a.islower())
print(a.isupper())
print(a.strip())
print(a.title())

# 4	Exercises


#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

a = 'Thirty '
b = 'Days '
c = 'Of '
d = 'Python'
result = a+b+c+d

print(result)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

a = 'Coding'
b = 'for'
c = 'All'
result = f"{a} {b} {c}"
print(result)

#3 Declare a variable named company and assign it to an initial value "Coding For All".

company = "Coding For All"

#4 Print the variable company using print().

print(company)

#5 Print the length of the company string using len() method and print().

print(len(company))

#6 Change all the characters to uppercase letters using upper() method.

print(company.upper())

#7 Change all the characters to lowercase letters using lower() method.

print(company.lower())

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string.

print(company[0:6])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.

word = 'Coding'
print(company.index(word))
position = company.find(word)
print(position)

#11 Replace the word coding in the string 'Coding For All' to Python.

print(company[::-1])

#12 Change Python for Everyone to Python for All using the replace method or other methods.

new_company = company.replace('All', 'Everyone')
print(new_company)

#13 Split the string 'Coding For All' using space as the separator (split()) .

print(company.split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

text = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(text.split())

#15 What is the character at index 0 in the string Coding For All.

print(company[0])

#16 What is the last index of the string Coding For All.

print(company[-1])

#17 What character is at index 10 in "Coding For All" string.

print(company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.

text = 'Python For Everyone'
acconym = ''.join(word[0].upper() for word in text.split())
print(acconym)

#19 Create an acronym or an abbreviation for the name 'Coding For All'.

text = 'Coding For All'
acconym = ''.join(word[0].lower() for word in text.split())
print(acconym)

#20 Use index to determine the position of the first occurrence of C in Coding For All.

a = 'Coding For All'
position = a.index('C')
print(position)

#21 Use index to determine the position of the first occurrence of F in Coding For All.

position = a.index('F')
print(position)

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.

position = a.rfind('l')
print(position)

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

text = "You cannot end a sentence with because because because is a conjunction"
position = text.find('because')
print(position)

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

position = text.rindex('because')
print(position)

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(text[31:55])

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

position = text.find('because')
print(position)

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(text[31:55])

#28 Does ''Coding For All' start with a substring Coding?

text = 'Coding For All'
substring = 'Coding'
position = text.startswith(substring)
print(position)

#29 Does 'Coding For All' end with a substring coding?

substring = 'All'
position = text.endswith(substring)
print(position)

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.

t = text.strip()
print(t)

#31 Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python

v1 = '30DaysOfPython'
v2 = 'thirty_days_of_python'
print(v1.isidentifier())
print(v2.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
j = ' # '.join(libraries)
print(j)


#33 Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

sentence = 'I am enjoing this challenge.\nI just  wonder what is next'
print(sentence)


#34 Use a tab escape sequence to write the following lines.

# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki

s = ('Name\tAge\tCountry\tCity\nAsabneh\t250\tSinland\tHelsinki')
print(s)


#35 Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.

radius = 10
area = 3.14 * radius ** 2
stri = f"The area of a circle is {radius} is {area} meter square"
print(stri)

# 36 Make the following using string formatting methods:

# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} ** {} = {}".format(a, b, a ** b))
print("{} // {} = {}".format(a, b, a // b))
