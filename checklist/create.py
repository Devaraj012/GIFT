import requests
import json
import os 
from dotenv import load_dotenv
load_dotenv()
AUTH=os.getenv('AUTH')

url = "https://greenestep.giftai.co.in/api/v1/csv"

headers = {
  'Cookie': 'ticket=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRldmFyYWpAaWJhY3VzdGVjaGxhYnMuaW4iLCJpZCI6NCwidHlwZSI6IkFETUlOIiwiaWF0IjoxNzQzNTk2MzY5LCJleHAiOjE3NDM2Mzk1Njl9.Arz_SkFA8oNFmc7OwOLDCDTf63c5sAJgBTAuT3fhKf0',
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {AUTH}'
}

Collections=[
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of Tasks worked on",
  "collection_permission": "READ",
  "collection_type": "PUBLIC"
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of interview scheduled",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of students passed the level",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of candidates selected",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of candidates Rejected",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of registration in careersheets",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of students applied on careersheets",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
    {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No of careersheets invite sent to interview candidates",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },
  {
  "collection_description": "Checklist_Gienie",
  "collection_name": "No cleared Technical screening",
  "collection_permission": "READ",
  "collection_type": "PUBLIC" 
  },      
]

for collection in Collections:
  payload = json.dumps(collection)
  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)