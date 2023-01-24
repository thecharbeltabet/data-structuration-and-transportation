import requests

response = requests.post('https://httpbin.org/get')

print(response.status_code)

# The reason for this is that we're sending a POST request to an endpoint that's only set up to handle GET requests. The endpoint https://httpbin.org/post is used to post the request and get a response back which can be used to test post request and get the status code and other data related to post request but we're trying to send your request to https://httpbin.org/get which is a endpoint to test get request so the server will not be able to handle it and thus it will return the status code '405 Method Not Allowed'.