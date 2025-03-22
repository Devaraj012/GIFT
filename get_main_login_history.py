import csv
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# TO GET DATA
# The API endpoint
url = "https://gac.giftai.co.in/api/v1/activity/loginhistory"
# A GET request to the API
response = requests.post(url)


# To MAP THE DATA
# Your Bearer token
bearer_token=os.getenv('TOKEN')

# Headers with Authorization
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

data = {
    "domain_name": "gmail"
}

# TO SEND THE DATA TO CENTRAL GAC_SERVER
# url="http://localhost:5003/api/v1/activity/loginhistory"
# response = requests.get(url)
response = requests.get(url, headers=headers,data=data)

resp_data = response.json()

data =resp_data['data'] 

with open('giftHistories_02-01-2025.csv', 'w', newline='') as csvfile:
    fieldnames = ['id' ,
    'created_at' ,
    'email',
    'hostname',
    'user_agent',
    'url',
    'login_type',
    'domain',
    'app_name',
    'product_name',
    'update_id'
]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
# Print the response
# print(response.json())