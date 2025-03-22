import os
import requests
import mariadb,pandas as pd
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\devar\Documents\Code\GIFT\.env")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")) if os.getenv("DB_PORT") else None,  # Prevent NoneType error
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

cookie_ticket = os.getenv("COOKIE_TICKET")

conn = mariadb.connect(**DB_CONFIG)
cursor = conn.cursor(dictionary=True)

queries = {
    1: """
        SELECT 
            u.name AS employee_name,
            cir.input AS interview_count,
            cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
            (ci.checklist_name = 'No of Interview conducted' OR ci.checklist_name = 'No of technical Interview conducted')
            AND cir.input <> 0
        ORDER BY 
            cir.created_at DESC;
    """,
    2: """
        SELECT 
            u.name AS employee_name,
            cir.input AS meeting_count,
            cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
             ci.checklist_name = 'No of In-Person Meeting' OR ci.checklist_name='No of Inperson meeting' 
        ORDER BY 
            cir.created_at DESC;
    """,
    3:"""
        SELECT 
            u.name AS employee_name,
            cir.input AS deploy_count,
            cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
             ci.checklist_name = 'Deployed Build' and cir.input<>0
        ORDER BY 
            cir.created_at DESC;
    """,
    4:"""
        SELECT 
            u.name AS employee_name,
            cir.input AS completed_count,
            cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
             (ci.checklist_name = 'No of Tasks Completed' or ci.checklist_name='No of Task Completed') and cir.input<>0
        ORDER BY 
            cir.created_at DESC;
    """,
    5:"""
        SELECT 
            u.name AS employee_name,
            cir.input AS prospects_count,
            cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
             ci.checklist_name = 'No of Prospects Identified' and cir.input<>0 and u.id in (8,10,27)
        ORDER BY 
            cir.created_at DESC;
    """,
    6:"""
        SELECT 
            u.name AS employee_name,
            cir.input AS powercut_count,
            cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
             ci.checklist_name = 'No of Power Cuts' and cir.input<>0
        ORDER BY 
            cir.created_at DESC;
    """,
    7:"""
        SELECT 
        u.name AS employee_name,
        cir.input AS prospects_called,
        cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
            ci.checklist_name = 'No of prospects called' and cir.input<>0 and u.id in (8,10,27)

        ORDER BY
        cir.created_at desc""",
    8:"""
        SELECT 
        u.name AS employee_name,
        cir.input AS prospects_qualified,
        cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
            ci.checklist_name = 'No of prospects qualified' and cir.input<>0 and u.id in (8,10,27)

        ORDER BY
            cir.created_at desc """,
    9:"""
        SELECT 
        u.name AS employee_name,
        cir.input AS meetings_scheduled,
        cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
            ci.checklist_name = 'No of meetings scheduled' and cir.input<>0 and u.id in (8,10,27)

        ORDER BY
        cir.created_at desc      
    """,
    10:"""
        SELECT 
        u.name AS employee_name,
        cir.input AS meetings_attended,
        cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
            ci.checklist_name = 'No of meetings attended' and cir.input<>0 and u.id in (8,10,27)

        ORDER BY
        cir.created_at desc
    """,
    11:"""
        SELECT 
        u.name AS employee_name,
        cir.input AS follow_up_calls,
        cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
            ci.checklist_name = 'No of follow up calls made' and cir.input<>0 and u.id in (8,10,27)

        ORDER BY
        cir.created_at desc
    """,
    12:"""
        SELECT 
        u.name AS employee_name,
        cir.input AS closure_made,
        cir.created_at AS date
        FROM 
            checklist_item_response cir
        JOIN 
            checklist_template_linked_items ctli ON cir.checklist_template_linked_items_id = ctli.id
        JOIN 
            checklist_items ci ON ctli.checklist_item_id = ci.id
        JOIN 
            Organisation_Users ou ON cir.organisation_user_id = ou.id
        JOIN 
            User u ON ou.user_id = u.id
        WHERE 
            ci.checklist_name = 'No of closure made' and cir.input<>0 and u.id in (8,10,27)

        ORDER BY
        cir.created_at desc
    """
        
}

def fetch_and_upload_data(query_number):
    if query_number in queries:
        query = queries[query_number]
        cursor.execute(query)
        results = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(results, columns=column_names)
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%m-%d-%Y')
        
        output_file = f"Query_{query_number}_Data.csv"
        df.to_csv(output_file, index=False)
        print(f"Query {query_number} executed successfully. Data saved to {output_file}")
        
        upload_data(output_file, query_number)
    else:
        print("Invalid query number. Please provide a valid query number.")

def upload_data(file_path, query_number):
    url = "https://greenestep.giftai.co.in/api/v1/csv/upload?d_type=none&"
    
    payloads = {
        1: {
            'collection_id': '87',
            'type': 'Replace',
            'fieldMapped': 'Object'
        },
        2: {
            'collection_id': '92',
            'type': 'Replace',
            'fieldMapped': 'Object'
        },
        3: {
            'collection_id': '90',
            'type': 'Replace',
            'fieldMapped': 'Object'
        },
        4: {
            'collection_id': '99',
            'type': 'Replace',
            'fieldMapped': 'Object'
        },
        5: {
            'collection_id': '98',
            'type': 'Replace',
            'fieldMapped': 'Object'
        },
        6:{
            'collection_id': '100',
            'type': 'Replace',
            'fieldMapped': 'Object'
        },
        7:{
            'collection_id': '108',
            'type': 'Replace',
            'fieldMapped': 'Object'            
        },
        8:{
            'collection_id': '109',
            'type': 'Replace',
            'fieldMapped': 'Object'             
        },
        9:{
            'collection_id': '110',
            'type': 'Replace',
            'fieldMapped': 'Object'             
        },
        10:{
            'collection_id': '111',
            'type': 'Replace',
            'fieldMapped': 'Object'             
        },
        11:{
            'collection_id': '112',
            'type': 'Replace',
            'fieldMapped': 'Object'             
        },
        12:{
            'collection_id': '113',
            'type': 'Replace',
            'fieldMapped': 'Object'             
        }        
    }
    
    headers = {
        'Cookie': 'ticket=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRldmFyYWpAaWJhY3VzdGVjaGxhYnMuaW4iLCJpZCI6NCwidHlwZSI6IkFETUlOIiwiaWF0IjoxNzQyNTM4Mzg0LCJleHAiOjE3NDI1ODE1ODR9.M2FXM5VskT1T7VHDouULwiVfOTnlsj5cpcyu0odrvKc'
    }
    
    payload = payloads.get(query_number, {})
    
    with open(file_path, 'rb') as f:
        files = {'csvFile': (file_path, f, 'text/csv')}
        response = requests.post(url, headers=headers, data=payload, files=files)
    
    print(response.text)

for query_num in queries.keys():
    fetch_and_upload_data(query_num)

cursor.close()
conn.close()