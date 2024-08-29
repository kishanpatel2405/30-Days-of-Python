# 18	Regular Expressions
# find patterns in data.

# 18	The re Module

import re

# 18	Methods in re Module
# re.match()
# re.search()
# re.findall()
# re.split()
# re.sub()

# 18	Match

import re

txt = 'hello my name is kisan'
match = re.match('hello', txt, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

# 18	Search

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search('python is the most beautiful', txt, re.I)
print(match)
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

# 18	Searching for All Matches Using findall

import re

txt = '''Python language is the most beautiful language that a human being has ever created.
I recommend python language for a first programming language'''
matches = re.findall('language', txt, re.I)
print(matches)
matches = re.findall('python', txt, re.I)
print(matches)

# 18	Replacing a Substring

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_replace = re.sub('Python|python', 'java', txt, re.I)
print(match_replace)

txt = 'he%%%llo my name i%%%%%s kish%%%%%%%%%%%%%%%%an'
replace = re.sub('%', '', txt)
print(replace)

# 18	Splitting Text Using RegEx Split

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))

# 18	Writing RegEx Patterns

import re

regex_pattern = 'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)
matches = re.findall(regex_pattern, txt, re.I)
print(matches)
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)

# 18	Square Bracket

txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
patter = '[Aa]pple'
find = re.findall(patter, txt, re.I)
print(find)

# 18	Escape character(\) in RegEx

regex_pattern = '\d'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# 18	One or more times(+)

regex_pattern = '\d+'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# 18	Period(.)

regex_pattern = '[a].'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)
regex_pattern = '[a].+'
matches = re.findall(regex_pattern, txt)
print(matches)

# 18	Zero or more times(*)

regex_pattern = r'[a].*'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)

# 18	Zero or one time(?)

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'
matches = re.findall(regex_pattern, txt)
print(matches)

# 18	 Quantifier in RegEx

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'
matches = re.findall(regex_pattern, txt)
print(matches)
print()
print()
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'
matches = re.findall(regex_pattern, txt)
print(matches)

# 18	Cart ^

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = '^This'
matches = re.findall(regex_pattern, txt)
print(matches)

# 18	Exercises: Level 1

# What is the most frequent word in the following paragraph?
paragraph = ('''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love 
something which can give you all the capabilities to develop an application what else can you love.''')

match = re.findall('love', paragraph, re.I)
print(match)
match = re.findall('you', paragraph, re.I)
print(match)
match = re.findall('can', paragraph, re.I)
print(match)
match = re.findall('what', paragraph, re.I)
print(match)
match = re.findall('teaching', paragraph, re.I)
print(match)
match = re.findall('not', paragraph, re.I)
print(match)
match = re.findall('else', paragraph, re.I)
print(match)
match = re.findall('do', paragraph, re.I)
print(match)
match = re.findall('I', paragraph, re.I)
print(match)
match = re.findall('which', paragraph, re.I)
print(match)
match = re.findall('to', paragraph, re.I)
print(match)
match = re.findall('the', paragraph, re.I)
print(match)
match = re.findall('something', paragraph, re.I)
print(match)
match = re.findall('if', paragraph, re.I)
print(match)
match = re.findall('give', paragraph, re.I)
print(match)
match = re.findall('develop', paragraph, re.I)
print(match)
match = re.findall('capabilities', paragraph, re.I)
print(match)
match = re.findall('application', paragraph, re.I)
print(match)
match = re.findall('an', paragraph, re.I)
print(match)
match = re.findall('all', paragraph, re.I)
print(match)
match = re.findall('python', paragraph, re.I)
print(match)
match = re.findall('if', paragraph, re.I)
print(match)

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction,
# 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance
# between the two furthest particles.

import re
text = """
The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.
"""
positions = re.findall(r'-?\d+', text)
positions = list(map(int, positions))
min_point = min(positions)
max_point = max(positions)
distance = max_point - min_point
print(f"The distance between the two furthest particles is {distance}.")

# 18	Exercises: Level 2

# Write a pattern which identifies if a string is a valid python variable

import re


def is_valid_variable(name):
    pattern = r'^[a-zA-Z_]\w*$'
    return re.match(pattern, name) is not None

print(is_valid_variable('first_name'))
print(is_valid_variable('first-name'))
print(is_valid_variable('1first_name'))
print(is_valid_variable('firstname'))

# 18	Exercises: Level 3

# Clean the following text. After cleaning, count three most frequent words in the string.

import re
def clean_text(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text


def most_frequent_words(text):
    text = text.lower()

    words = text.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

    return sorted_words[:3]

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)

print(most_frequent_words(cleaned_text))




























