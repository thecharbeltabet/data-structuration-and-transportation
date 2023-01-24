import csv

path = '/Users/charbeltabet/Library/CloudStorage/OneDrive-EPITA/S3-Specialization/DST/data-structuration-and-transportation/resources/csv/ratp.csv'


class Station:
    rank: int
    network: str
    name: str
    number_of_users: int
    connections: list[str]
    city: str
    district: int | None

    def __init__(self, rank, network, name, number_of_users, connections, city, district):
        self.rank = rank
        self.network = network
        self.name = name
        self.number_of_users = number_of_users
        self.connections = connections
        self.city = city
        self.district = district

stations = []

# Open the CSV file and read the data
with open(path, 'r') as file:
    reader = csv.reader(file,delimiter=";")
    for row in reader:
        # Create a new Station instance for each row and append it to the stations list
        rank = row[0]
        network = row[1]
        name = row[2]
        number_of_users = row[3]
        connections = row[4:]
        city = row[-2]
        district = row[-1]
        stations.append(Station(rank, network, name, number_of_users, connections, city, district))

# Now you can access the data for each station like this:
stations.sort(key=lambda x: x.name)

for station in stations:
    print(f"{station.name}: {station.number_of_users} users per day")
