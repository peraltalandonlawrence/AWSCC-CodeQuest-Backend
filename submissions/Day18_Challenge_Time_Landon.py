import requests

endpoint_url = "https://jsonplaceholder.typicode.com/posts"

header = {
    "User-Agent" : "MyApp/1.0"
}

response = requests.get(endpoint_url, headers=header)

print("Status code: ", response.status_code)
print("Response header: ",response.headers)

print("Response content: ", response.json)
for key, value in response.headers.items():
    print(f"{key}: {value}")
data  = {
    "title": "I am Landon Lawrence Peralta",
    "body": "I am 20 years old and I have been studying at the Polytechnic University of the Philippines for 6 years."
}

post_response = requests.post(endpoint_url, headers=header, json=data)

print("\nPost Response Section")
print("Status Code: ", post_response.status_code)
print("Response Content: ",post_response.json())
