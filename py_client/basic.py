import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint, json={"query":"Hello world!"}) #API -> Method
#print(response.text)

print(response.json())