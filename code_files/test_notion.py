import requests

database_id = "1f2152b71a3b8077b3c0fab8a364ab95"
secret = "ntn_c5682698811a4oBW4gs2vZ5Svc4t8KZ96G54BBhRT0Q6jm"

url = f"https://api.notion.com/v1/databases/{database_id}/query"
headers = {
    "Authorization": f"Bearer {secret}",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)

print("Status code:", response.status_code)
print("Response text:", response.text)

