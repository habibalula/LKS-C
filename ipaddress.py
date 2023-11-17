import requests
from requests.auth import HTTPBasicAuth

# Router Information
router_ip = "10.10.10.10"
username = "admin"
password = "cisco"

# RESTCONF Endpoint
restconf_url = f"https://10.10.10.10/restconf/data/native/interface/Loopback=8888"

# Data to Configure IP Address
config_data = {
    "Cisco-IOS-XE-native:Loopback": {
        "name": 8888,
        "ip": {
            "address": {
                "primary": {
                    "address": "8.8.8.8",
                    "mask": "255.255.255.255"
                }
            }
        }
    }
}

# Headers for RESTCONF Request
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

# Disable SSL Warnings (Only for testing purposes)
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# RESTCONF Authentication
auth = HTTPBasicAuth(username, password)

# Send RESTCONF Patch Request to Configure IP Address
response = requests.patch(restconf_url, json=config_data, headers=headers, auth=auth, verify=False)

# Print Response
print(f"Response Status Code: {response.status_code}")
print(response.text)



