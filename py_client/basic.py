import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api"

response = requests.get(endpoint, json={"query":"Hello world!"}) #API -> Method
print(response.text)
print(response.status_code)

print(response.json())
#