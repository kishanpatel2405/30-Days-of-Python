# Python PIP - Python Package Manager


# Exercises: Day 20

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats

import requests
import numpy as np
from collections import Counter


def fetch_data(url: str) -> list:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def process_data(data: list) -> (list, list, list, list):
    weights = []
    lifespans = []
    countries = []
    breeds = []

    for cat in data:
        weight_str = cat.get('weight', {}).get('metric', '')
        lifespan_str = cat.get('life_span', '')
        country = cat.get('origin', '')
        breed = cat.get('name', '')

        if weight_str:
            try:
                weight = float(weight_str.split()[0])
                weights.append(weight)
            except ValueError:
                continue

        if lifespan_str:
            try:
                lifespan = int(lifespan_str.split()[0])
                lifespans.append(lifespan)
            except ValueError:
                continue
        if country:
            countries.append(country)
        if breed:
            breeds.append(breed)
    return weights, lifespans, countries, breeds


def calculate_and_print_stats(values: list, label: str):
    if values:
        np_values = np.array(values)
        print(
            f"{label} - Min: {np.min(np_values)}, Max: {np.max(np_values)}, Mean: {np.mean(np_values)}, Median: {np.median(np_values)}, Std Dev: {np.std(np_values)}")
    else:
        print(f"{label} - No data available")


def main():
    url = 'https://api.thecatapi.com/v1/breeds'
    data = fetch_data(url)
    weights, lifespans, countries, breeds = process_data(data)
    calculate_and_print_stats(weights, "Weight")
    calculate_and_print_stats(lifespans, "Lifespan")
    country_freq = Counter(countries)
    breed_freq = Counter(breeds)

    print("\nCountry Frequency Table:")
    for country, freq in country_freq.items():
        print(f'{country}: {freq}')

    print("\nBreed Frequency Table:")
    for breed, freq in breed_freq.items():
        print(f'{breed}: {freq}')


main()