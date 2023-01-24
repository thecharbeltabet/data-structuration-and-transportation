import json

path = '/Users/charbeltabet/Library/CloudStorage/OneDrive-EPITA/S3-Specialization/DST/data-structuration-and-transportation/resources/json/french-cities.json'

class City:
    city: str
    lat: float
    lng:float
    country: str
    iso2: str
    admin_name: str
    capital: str
    population: int
    population_proper: int

    def __init__(self, data):
        self.city = data['city']
        self.lat = data['lat']
        self.lng = data['lng']
        self.country = data['country']
        self.iso2 = data['iso2']
        self.admin_name = data['admin_name']
        self.capital = data['capital']
        self.population = int(data['population'])
        self.population_proper = data['population_proper']

       
        

# Initialize an empty list
cities = []

# Open the file
with open(path) as f:
    # Load the data from the file
    data = json.load(f)

# Iterate through the data and create City instances
for city_data in data:
    city = City(city_data)
    cities.append(city)

# The list `cities` now contains City instances
# You can access the attributes of a city by using the dot notation, e.g. city.city



# Compute the total population
total_population = 0
print(total_population)


for city in cities:
    print(city.population)

    total_population = city.population + total_population



#Compute the average population per city
average_population = total_population / len(cities)

# Find the biggest city
biggest_city = {'name': '', 'population': 0}
for city in cities:
    if city.population > biggest_city['population']:
        biggest_city['name'] = city.cityclear
        biggest_city['population'] = city.population

# Print the results
print(f'Total population: {total_population}')
print(f'Average population per city: {average_population}')
print(f'Biggest city: {biggest_city["name"]} ({biggest_city["population"]})')

