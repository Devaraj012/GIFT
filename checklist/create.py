import requests
import json
import os 
from dotenv import load_dotenv
load_dotenv()
load_dotenv(dotenv_path=r"C:\Users\devar\OneDrive\Documents\Code\GIFT\.env")

AUTH=os.getenv('AUTH')

cookie = os.getenv('IBT_COOKIE')

url = "https://greenestep.giftai.co.in/api/v1/csv"

headers = {
  'Cookie': f'ticket={cookie}',
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {AUTH}'
}

Collections=[
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "In person meeting with Prospects",
  "collection_permission": "READ",
  "collection_type": "PUBLIC"
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "In person meeting with Customers",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  }    
]

for collection in Collections:
  payload = json.dumps(collection)
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)