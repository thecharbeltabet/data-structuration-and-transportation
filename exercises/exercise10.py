import requests

data = {'param1': 'value1', 'param2': 'value2'}
response = requests.post('https://httpbin.org/post', data=data)

print(response.status_code)
print(response.json())

response2 = requests.post('https://httpbin.org/post', json=data)

print(response2.status_code)
print(response2.json())

# The main difference between these two is the way data is passed in the request body and the content type headers that are set automatically based on the data passed.
#If we use the data parameter, the data is sent in the body of the request encoded as application/x-www-form-urlencoded, and if we use the json parameter, the data is sent in the body of the request encoded as application/json.
