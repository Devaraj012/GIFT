import requests
import json
import os 
from dotenv import load_dotenv
load_dotenv()
AUTH=os.getenv('AUTH')

url = "https://greenestep.giftai.co.in/api/v1/csv"

headers = {
  'Cookie': 'ticket=eyJhb5GciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRldmFyYWpAaWJhY3VzdGVjaGxhYnMuaW4iLCJpZCI6NCwidHlwZSI6IkFETUlOIiwiaWF0IjoxNzQyMjc5MjQ1LCJleHAiOjE3NDIzMjI0NDV9.QdR1vwu5mmtWslJRS3gnD-Wxtvshc93aGlx5QHhglyY',
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {AUTH}'
}

Collections=[
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of prospects called",
  "collection_permission": "READ",
  "collection_type": "PUBLIC"
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of prospects qualified",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of meetings scheduled",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of meetings attended",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of follow up calls made",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of closure made",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },      
]

for collection in Collections:
  payload = json.dumps(collection)
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)