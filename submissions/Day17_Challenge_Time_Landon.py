import requests

endpoint_url = "https://jsonplaceholder.typicode.com/"

response = requests.get(endpoint_url)

if response.status_code == 200:
    print("Request Successful")
else:
    print("Request Failed")

