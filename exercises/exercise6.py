import json

path = '/Users/charbeltabet/Library/CloudStorage/OneDrive-EPITA/S3-Specialization/DST/data-structuration-and-transportation/resources/json/users.json'

class User:
    def __init__(self, id, name, city, school, age, is_teacher):
        self.id = id
        self.name = name
        self.city = city
        self.school = school
        self.age = age
        self.is_teacher = is_teacher

with open(path, 'r') as f:
    data = json.load(f)

users = []
for user_dict in data:
    user = User(user_dict['id'], user_dict['name'], user_dict['city'], user_dict['school'], user_dict['age'], user_dict['is_teacher'])
    users.append(user)

