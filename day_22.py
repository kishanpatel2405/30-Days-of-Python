# 22	What is Web Scrapping


import requests

url = 'https://www.kaggle.com/datasets/waqi786/brain-tumor-dataset?select=brain_tumor_dataset.csv'

response = requests.get(url)
status = response.status_code
print(status)

import requests
from bs4 import BeautifulSoup

url = 'https://www.kaggle.com/datasets/waqi786/brain-tumor-dataset?select=brain_tumor_dataset.csv'

response = requests.get(url)

if response.status_code == 200:
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    print(soup.title.get_text())

    tables = soup.find_all('table')

    print(f"Number of tables found: {len(tables)}")

    if tables:
        table = tables[0]
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            row = [td.get_text(strip=True) for td in tds]
            print(row)
    else:
        print("No tables found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# 22	Exercises: Day 22


# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').


import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    data = {}
    section = soup.find('section', {'class': 'factoids'})
    if section:
        facts = section.find_all('div', {'class': 'fact'})
        for fact in facts:
            title = fact.find('h3').get_text(strip=True) if fact.find('h3') else 'No Title'
            content = fact.find('p').get_text(strip=True) if fact.find('p') else 'No Content'
            data[title] = content
    print(json.dumps(data, indent=4))

    with open('bu_facts_and_stats.json', 'w') as f:
        json.dump(data, f, indent=4)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

print()

# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file


import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = "https://github.com/ahmadmughees/SH17dataset"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table')

if not tables:
    raise ValueError("No tables found on the page.")

table = tables[0]

header_row = table.find('tr')
headers = [header.get_text(strip=True) for header in header_row.find_all('th')]

rows = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) > 0:
        row_data = [col.get_text(strip=True) for col in cols]
        rows.append(row_data)

df = pd.DataFrame(rows, columns=headers)

data_dict = df.to_dict(orient='records')

with open('datasets.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Data has been successfully scraped and saved to datasets.json.")

print()


# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States).
# The table is not very structured and the scrapping may take very long time.


import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})

presidents = []

for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    if len(columns) >= 4:
        number = columns[0].get_text(strip=True)
        name = columns[1].get_text(strip=True)
        term = columns[2].get_text(strip=True)
        party = columns[3].get_text(strip=True)

        presidents.append({
            'number': number,
            'name': name,
            'term': term,
            'party': party
        })

presidents_json = json.dumps(presidents, indent=4)

with open('presidents.json', 'w') as file:
    file.write(presidents_json)

print("Data has been successfully scraped and saved to 'presidents.json'.")













