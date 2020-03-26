import json

with open('interfaces.json', 'r') as f:
    interface_dict = json.load(f)

for i in interface_dict:
    print(i["ip-adress"])
