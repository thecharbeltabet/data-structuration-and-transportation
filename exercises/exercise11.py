import requests
from collections import defaultdict


# Convert the date and time to UNIX timestamp
departure_time = int("1609459200")

# Set the API endpoint and parameters
endpoint = "https://opensky-network.org/api/flights/departure"
params = {
    "airport": "LFPG",
    "begin": departure_time,
    "end": departure_time + 86400
}

# Make the API request
response = requests.get(endpoint, params=params)

# Print the response content
# print(response.content)

data = response.json()

flight_count = defaultdict(int)

# Iterate over the flight data
for flight in data:
     if flight['estArrivalAirport'] is not None:
        flight_count[flight['estArrivalAirport']] += 1

# Find the airport with the most flights
most_flights_destination = max(flight_count, key=flight_count.get)

print("The airport with the most flights out of CDG is: " + most_flights_destination)
