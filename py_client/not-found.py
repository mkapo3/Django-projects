import requests

endpoint = "http://localhost:8000/api/products/3122314"


response = requests.get(endpoint) 
print(response.json())

