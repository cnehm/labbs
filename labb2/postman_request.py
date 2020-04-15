import requests

url = "https://sandboxapicem.cisco.com/api/v1/ticket"

payload = "{\r\n  \"username\": \"devnetuser\",\r\n  \"password\": \"Cisco123!\"\r\n}\r\n"
headers = {
  'Content-Type':'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
