from email import header
import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username:\n")
password = getpass()

auth_response = requests.post(endpoint, json={"username":"cfe", "password": password}) 
print(auth_response.json())

if auth_response.status_code == 200: 
    token = auth_response.json()['token']
    headers = {
        'Authorization' : f"Token {token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    response = requests.get(endpoint, headers=headers) 
    print(response.json())
    # data = response.json()
    # next_url = data["next"]
    # if next_url is not None:
    #     response = requests.get(next_url, headers=headers)

#
