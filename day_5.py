# 5	How to Create a List

a = []

# 5	Accessing List Items Using Positive Indexing

fruits = ['banana', 'apple', 'pear', 'orange']
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
# print(fruits[4])

# 5	Accessing List Items Using Negative Indexing

fruits = ['banana', 'mango', 'apple', 'orange']
print(fruits)
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
# print(fruits[-5])

# 5	Unpacking List Items

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# 5	Slicing Items from a List

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
print(countries[2:5])
print(countries[-2:])
print(countries[:2])
print(countries[:])
print(countries[::-2])

# 5	Modifying Lists

num = [100,200,300,400,500,600,700,800]
num[1] = 150
print(num)

# 5	Checking Items in a List

fruits = ['banana', 'orange', 'mango', 'lemon']
x = 'banana' in fruits
print(x)

# 5	Adding Items to a List

fruits.append('watermelon')
print(fruits)

# 5	Inserting Items into a List

fruits.insert(2, 'lime')
print(fruits)

# 5	Removing Items from a List

fruits.remove('lime')
print(fruits)

# 5	Removing Items Using Pop

fruits.pop(0)
print(fruits)

# 5	Removing Items Using Del

del fruits[0]
print(fruits)

# 5	Clearing List Items

fruits.clear()
print(fruits)

# 5	Copying a List

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits2 = fruits.copy()
print(fruits2)

# 5	Joining Lists

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [-1,-3,-5,-6,-7,-8]
print(l1+l2)

# 5	Counting Items in a List

name = ['kishan', 'rushil','dharmik', 'vinesh', 'prem', 'kishan', 'kishan']
print(name.count('kishan'))


# 5	Finding Index of an Item

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))

# 5	Reversing a List

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

# 5	Sorting List Items
fruits.sort()
print(fruits)

# 5	Exercises: Level 1

# Declare an empty list

L = list()
l = []

# Declare a list with more than 5 items
l = [1,2,3,4,5,6,7]

# Find the length of your list
print(len(l))

# Get the first item, the middle item and the last item of the list
print(l[0])
print(l[3])
print(l[-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
lst = ['kishan', 21, 5.5, 'single', 'Rajkot']
print(lst)
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0])
print(it_companies[-1])
print(it_companies[3])
# Print the list after modifying one of the companies
print(it_companies)
# Add an IT company to it_companies
it_companies.append('DeftBox')
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies.insert(3, 'kishanpvt')
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = [company.upper() if company != 'IBM' else company for company in it_companies]
print(it_companies)
# Join the it_companies with a string '#;  '
joined_string = ' #;  '.join(it_companies)
print(joined_string)
# Check if a certain company exists in the it_companies list.
a = 'YouTube' in it_companies
print(a)
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# Slice out the first 3 companies from the list
print(it_companies[0:3])
# Slice out the last 3 companies from the list
print(it_companies[-4:-1])
# Slice out the middle IT company or companies from the list
print(it_companies)
print(it_companies[4:5])
# Remove the first IT company from the list
it_companies.remove('ORACLE')
print(it_companies)
# Remove the middle IT company or companies from the list
it_companies.remove('FACEBOOK')
print(it_companies)
# Remove the last IT company from the list
it_companies.remove('AMAZON')
# Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
del it_companies



# 5	Exercises: Level 2
# The following is a list of 10 students ages:
# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
minvalue = min(ages)
print(minvalue)
maxvalue = max(ages)
print(maxvalue)

# Add the min age and the max age again to the list
addition = minvalue + maxvalue
print(addition)

# Find the median age (one middle item or two middle items divided by two)
n = len(ages)
if n != 2 == 1:
    median = ages[n // 1]
else:
    mid1 = n // 2 - 1
    mid2 = n // 2
    median = (ages[mid1] + ages[mid2]) / 2
print(ages)
print(median)

# Find the average age (sum of all items divided by their number )

total_sum = sum(ages)
num_items = len(ages)
average_age = total_sum / num_items
print(average_age)

# Find the range of the ages (max minus min)
max_age = max(ages)
min_age = min(ages)
age_range = max_age - min_age
print(age_range)

# Compare the value of (min - average) and (max - average), use abs() method

min_age = min(ages)
max_age = max(ages)

average_age = sum(ages) / len(ages)

min_diff = min_age - average_age
max_diff = max_age - average_age

abs_min_diff = abs(min_diff)
abs_max_diff = abs(max_diff)

if abs_min_diff > abs_max_diff:
    print('average is greater')
    print(max_age)
elif abs_min_diff < abs_max_diff:
    print('average is greater')
    print(min_age)
else:
    print('average is equal')


# Find the middle country(ies) in the countries list

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

count = 0
for _ in countries:
    count +=1
mid_index = count // 2
middle_element = countries[mid_index]
print(middle_element)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

count = len(countries)
midde = (count+1) // 2
first_half = countries[:midde]
second_half = countries[midde:]
print(first_half)
print(second_half)

  # ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

first_three = ['China', 'Russia', 'USA']
scandic_countries = ['Finland', 'Sweden', 'Norway', 'Danmark']

unpacked_first_three = [country for country in countries if country in first_three]
unpacked_scandic = [country for country in countries if country in scandic_countries]

print('first three is : ', unpacked_first_three)
print('scandic is : ', unpacked_scandic)