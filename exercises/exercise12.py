import requests

# Set the API endpoint
endpoint = "https://api.github.com/users/thecharbeltabet/repos"

# Set the headers for the request
headers = {
    "Authorization": "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"
}

# Make the API request
response = requests.get(endpoint, headers=headers)

data = response.json()

for repo in data:
    print(f'{repo["name"]}')
