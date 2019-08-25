import csv

def load_city_data(city):
    with open('cities.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city.create_city(**row)