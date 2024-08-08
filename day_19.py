# 19	File Handling

# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


# 19	Opening Files for Reading
#
# f = open('read_file_ex.txt')
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()


# f = open('read_file_ex.txt')
# txt = f.read(10)
# print(type(txt))
# print(txt)
# f.close()

# f = open('read_file_ex.txt')
# txt = f.readlines()
# print(type(txt))
# print(txt)
# f.close()

# f = open('read_file_ex.txt')
# lines = f.read().splitlines()
# print(type(lines))
# print(lines)
# f.close()

# with open ('read_file_ex.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)

# 19	Opening Files for Writing and Updating

# with open ('read_file_ex.txt', 'a') as f:
#     f.write('This text has to be appended at the end')
#     f.close()

# 19	Deleting Files

# import os
# os.remove('read_file_ex.txt')

# 19	File Types

# 19	File with txt Extension

# 19	File with json Extension

# 19	Changing JSON to Dictionary

import json

# JSON
person_json = '''{
    "name": "kishan",
    "country": "india",
    "city": "rajkot",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# 19	Changing Dictionary to JSON

import json

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# dict convert it to  json
person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)

# 19	Saving as JSON File

import json

person = {
    "name": "kishan",
    "country": "India",
    "city": "Ahmedabad",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)

# 19	File with csv Extension

import csv

with open('csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

# 19	File with xlsx Extension

# import xlrd
# excel_book = xlrd.open_workbook('sample.xls)
# print(excel_book.nsheets)
# print(excel_book.sheet_names)


# 19	File with xml Extension

# 19	Exercises: Level 1

# Write a function which count number of lines and number of words in a text. All the files are in the data the
# folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file
# and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read
# melina_trump_speech.txt file and count number of lines and words

import os


def count_lines_and_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)

        return num_lines, num_words
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return 0, 0


data_folder = 'data'

files = [
    'obama_speech.txt',
    'michelle_obama_speech.txt',
    'donald_speech.txt',
    'melina_trump_speech.txt'
]
for file_name in files:
    full_path = os.path.join(data_folder, file_name)
    num_lines, num_words = count_lines_and_words(full_path)
    print(f"{file_name}: Lines = {num_lines}, Words = {num_words}")

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

import json


def find_most_spoken_languages(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        language_count = {}
        for country in data:
            languages = country.get('languages', [])
            population = country.get('population', 0)
            for language in languages:
                if language in language_count:
                    language_count[language] += population
                else:
                    language_count[language] = population

        sorted_languages = sorted(language_count.items(), key=lambda item: item[1], reverse=True)

        return sorted_languages[:10]

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []


data_file = 'countries_data.json'

top_languages = find_most_spoken_languages(data_file)
for language, speakers in top_languages:
    print(f"{language}: {speakers}")

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

import json


def most_populated_countries(filename, top_n):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)

        countries_population = [{'country': country['name'], 'population': country['population']} for country in data]

        sorted_countries = sorted(countries_population, key=lambda x: x['population'], reverse=True)

        return sorted_countries[:top_n]

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []


data_file = 'countries_data.json'

print(most_populated_countries(filename=data_file, top_n=10))
print(most_populated_countries(filename=data_file, top_n=3))

# 19	Exercises: Level 2

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

import re


def extract_emails(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        emails = re.findall(email_pattern, content)
        return emails

    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []


filename = 'email_exchanges_big.txt'
emails = extract_emails(filename)
print(emails)

# Find the most common words in the English language. Call the name of your function find_most_common_words,
# it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your
# function will return an array of tuples in descending order. Check the output

import re


def find_most_common_words(input_text, n):
    if isinstance(input_text, str) and (input_text.endswith('.txt') or input_text.endswith('.json')):
        try:
            with open(input_text, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"File {input_text} not found.")
            return []
    else:
        text = input_text
    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_word_counts[:n]


text = """I love teaching. If you do not love teaching what else can you love. I love Python if you do not love 
something which can give you all the capabilities to develop an application what else can you love."""
file_path = 'email_exchanges_big.txt'
print(find_most_common_words(text, 3))
print(find_most_common_words(file_path, 5))

# Find the most common words in the English language. Call the name of your function find_most_common_words,
# it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your
# function will return an array of tuples in descending order. Check the output

import re


def find_most_common_words(input_text, n):
    if isinstance(input_text, str) and (input_text.endswith('.txt') or input_text.endswith('.json')):
        try:
            with open(input_text, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"File {input_text} not found.")
            return []
    else:
        text = input_text

    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    return sorted_word_counts[:n]


text = """I love teaching. If you do not love teaching what else can you love. I love Python if you do not love 
something which can give you all the capabilities to develop an application what else can you love."""
file_path = 'email_exchanges_big.txt'
print(find_most_common_words(text, 3))
print(find_most_common_words(file_path, 5))

# 19	Exercises: Level 3

# Use the function, find_most_frequent_words to find:
# a) The ten most frequent words used in Obama's speech

import re


def find_most_common_words(input_text, n):
    text = re.sub(r'[^\w\s]', '', input_text)
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_word_counts[:n]


file_path = 'obama_speech.txt'
with open(file_path, 'r') as file:
    speech_text = file.read()
top_words = find_most_common_words(speech_text, 10)
print(top_words)

# b) The ten most frequent words used in Michelle's speech

import re
from collections import Counter


def find_most_common_words(file_path, n):
    with open(file_path, 'r') as file:
        text = file.read()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(n)
    return most_common_words


file_path = 'michelle_obama_speech.txt'

top_words = find_most_common_words(file_path, 10)

print("The ten most frequent words are:")
for word, count in top_words:
    print(f"{word}: {count}")

# c) The ten most frequent words used in Trump's speech

import re


def find_most_common_words(file_path, n):
    with open(file_path, 'r') as file:
        text = file.read()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_word_counts[:n]


file_path = 'donald_speech.txt'
top_words = find_most_common_words(file_path, 10)
print("The ten most frequent words are:")
for word, count in top_words:
    print(f"{word}: {count}")

# d) The ten most frequent words used in Melina's speech

import re


def find_most_common_words(file_path, n):
    with open(file_path, 'r') as file:
        text = file.read()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_word_counts[:n]


file_path = 'melina_trump_speech.txt'

top_words = find_most_common_words(file_path, 10)
print("The ten most frequent words are:")
for word, count in top_words:
    print(f"{word}: {count}")

# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and
# it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of
# Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text),
# function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity).
# List of stop words are in the data directory


import string
from typing import List


def load_stop_words(filepath: str) -> List[str]:
    with open(filepath, 'r') as file:
        stop_words = file.read().strip().split('\n')
    return stop_words


def read_text_from_file(filepath: str) -> str:
    with open(filepath, 'r') as file:
        return file.read()


def clean_text(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text


def remove_stop_words(text: str, stop_words: List[str]) -> str:
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)


def compute_similarity(text1: str, text2: str) -> float:
    set1 = set(text1.split())
    set2 = set(text2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if not union:
        return 0.0
    return len(intersection) / len(union)


def main():
    stop_words_file = 'stop_words.py'
    michelle_file = 'michelle_obama_speech.txt'
    melina_file = 'melina_trump_speech.txt'

    stop_words = load_stop_words(stop_words_file)

    michelle_text = read_text_from_file(michelle_file)
    melina_text = read_text_from_file(melina_file)

    michelle_cleaned = clean_text(michelle_text)
    melina_cleaned = clean_text(melina_text)

    michelle_filtered = remove_stop_words(michelle_cleaned, stop_words)
    melina_filtered = remove_stop_words(melina_cleaned, stop_words)
    similarity = compute_similarity(michelle_filtered, melina_filtered)
    print(f'The similarity between Michelle\'s and Melina\'s speeches is: {similarity:.2f}')


main()

# Find the 10 most repeated words in the romeo_and_juliet.txt


import string


def process_text(filepath: str, num_common: int) -> None:
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    word_counts = {}
    words = text.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    most_common_words = sorted_words[:num_common]

    print(f"The {num_common} most repeated words are:")
    for word, count in most_common_words:
        print(f'{word}: {count}')


def main():
    filepath = 'romeo_and_juliet.txt'
    process_text(filepath, 10)


main()

# Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the
# number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not
# JavaScript

import csv


def count_lines(filepath: str) -> None:
    python_count = 0
    js_count = 0
    java_not_js_count = 0

    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if len(row) == 0:
                continue
            text = ' '.join(row).lower()
            if 'python' in text or 'Python' in text:
                python_count += 1
            if 'JavaScript' in text or 'javascript' in text or 'Javascript' in text:
                js_count += 1
            if 'Java' in text and not ('JavaScript' in text):
                java_not_js_count += 1
    print(f"Number of lines containing 'python': {python_count}")
    print(f"Number of lines containing 'javascript': {js_count}")
    print(f"Number of lines containing 'java' and not 'javascript': {java_not_js_count}")

def main():
    filepath = 'hacker_news.csv'
    count_lines(filepath)
main()
