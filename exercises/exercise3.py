import csv

path = '/Users/charbeltabet/Library/CloudStorage/OneDrive-EPITA/S3-Specialization/DST/data-structuration-and-transportation/resources/csv/users.csv'
# Define the User class
class User:
    def __init__(self, id, name, city, school):
        self.id = id
        self.name = name
        self.city = city
        self.school = school

# Initialize an empty list to store the User instances
users = []

# Open the file in read mode
with open(path, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Iterate over the rows of the file
    for row in reader:
        # Create a User instance for each row
        user = User(row[0], row[1], row[2], row[3])

        # Add the User instance to the list
        users.append(user)

# Print the list of User instances
print("done")
