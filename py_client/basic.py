import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, params={"abc": 123}, json={"query":"Nesto"})  # API -> Method
# print(response.text)
# print(response.status_code)

print(response.json())
#
