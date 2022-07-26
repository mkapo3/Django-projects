import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/products/"
#endpoint = "http://localhost:8000/api/products/create/"

data = {
    "title" : "This field is done"
}
response = requests.post(endpoint, json=data)  # API -> Method
# print(response.text)
# print(response.status_code)

print(response.json())
#
