import requests
from requests.auth import HTTPBasicAuth
import json
import os

# API adress
url = "https://uat-cps-api.eminxing.com/open-api/v2/order/create"

# JSON pass
json_file_path = r'C:\Users\salom\Documents\ExcelFile\orders.json'

# user name et pwd
username = "YT_temu"
password = "YT_temu@123"

# header
headers = {
    "Content-Type": "application/json"
}

# check json
if os.path.exists(json_file_path):
    # readjson
    with open(json_file_path, 'r') as json_file:
        payloads = json.load(json_file)  # load data

    # for JSON
    for payload in payloads:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            auth=HTTPBasicAuth(username, password)
        )

        # print
        print(f"Order No: {payload['cOrderNo']}")
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)
        print("-" * 40)

else:
    print(f" {json_file_path} not exsit！pleqse check the pathjs")
