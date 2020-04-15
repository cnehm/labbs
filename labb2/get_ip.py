import requests
import json

url = "http://127.0.0.1:5000/interfaces"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

interface_dict = json.loads(response.text)

for i in interface_dict:
    print(i["ip-adress"])
