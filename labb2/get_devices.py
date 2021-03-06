import requests
import json
import urllib3
dnac = {
             "host": "sandboxdnac2.cisco.com",
             "username": "devnetuser",
             "password": "Cisco123!",
             "port": 443
         }

# Silence the insecure warning due to SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {
              'content-type': "application/json",
              'x-auth-token': ""
          }


def dnac_login(dnac, port, username, password):
    """
    Use the REST API to Log into an DNA Center and retrieve ticket
    """
    url = "https://{}:{}/dna/system/api/v1/auth/token".format(dnac, port)

    # Make Login request and return the response body
    response = requests.request("POST", url,
                                auth=(username, password),
                                headers=headers, verify=False)
    return response.json()["Token"]


def network_device_list(host, token):
    """
    Use the REST API to retrieve the list of network devices
    """
    url = "https://{}/dna/intent/api/v1/network-device".format(host)
    headers["x-auth-token"] = token

    # Make API request and return the response body
    response = requests.request("GET", url, headers=headers, verify=False)
    return response.json()["response"]


# Entry point for program
if __name__ == '__main__':
    # Log into the DNA Center Controller to get Ticket
    token = dnac_login(dnac["host"], dnac["port"], dnac["username"], dnac["password"])

    # Get the list of devices
    devices = network_device_list(dnac["host"], token)

    # Loop through the devices and print details
    for device in devices:
        print("{} in family {}".format(device["hostname"], device["family"]))
        print("  Management IP: {}".format(device["managementIpAddress"]))
        print("  Platform Type: {}".format(device["platformId"]))
        print("  Software Version: {}".format(device["softwareVersion"]))
        print("")
