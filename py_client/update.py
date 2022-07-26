import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title" : "Hello world friend",
    "price" : 129.0
}

response = requests.put(endpoint, json=data)

print(response.json())