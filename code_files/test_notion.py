import requests
import json

database_id = "202152b71a3b8097966aebf32d66611f"
headers = {
    "Authorization": "Bearer ntn_c5682698811a4oBW4gs2vZ5Svc4t8KZ96G54BBhRT0Q6jm",
    "Notion-Version": "2022-06-28"
}

url = f"https://api.notion.com/v1/databases/{database_id}"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    db_data = response.json()
    print(json.dumps(db_data['properties'], indent=2))
else:
    print("Failed to fetch database:", response.status_code)
    print(response.text)


