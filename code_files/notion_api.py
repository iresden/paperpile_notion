import requests, json
import csv

def queryDatabase(database_id, headers):
    query_url = "https://api.notion.com/v1/databases/"+database_id+"/query"
    blurb = '{"start_cursor": null}'
    blurb = json.loads(blurb)

    res = requests.request("POST", query_url, headers=headers, data = blurb)
    data = res.json()
    print('Querying database: ' + str(res.status_code))
    return data

def queryDatabase_again(database_id, headers, next_cursor):
    query_url = "https://api.notion.com/v1/databases/"+database_id+"/query"
    
    cursor_val ={
        "start_cursor": next_cursor
    }
    cursor_val = json.dumps(cursor_val)

    res = requests.request("POST", query_url, headers=headers, data = cursor_val)
    data = res.json()
    print('Querying database: ' + str(res.status_code))
    return data

def createPage(database_id, headers, auth_year, journal, title):
    create_url = "https://api.notion.com/v1/pages"
    fname = 'newpage.json'
    with open(fname, 'r') as f:
        newPageData = json.load(f)
    newPageData['parent']['database_id'] = database_id
    newPageData['properties']['Journal']["rich_text"][0]['text']['content'] = journal
    newPageData['properties']['Journal']["rich_text"][0]['plain_text'] = journal
    newPageData['properties']['Title']["rich_text"][0]['text']['content'] = title
    newPageData['properties']['Title']["rich_text"][0]['plain_text'] = title
    newPageData['properties']['Author, Year']['title'][0]['text']['content'] = auth_year
    newPageData['properties']['Author, Year']['title'][0]['plain_text'] = auth_year
    
    print("Payload being sent:")
    print(json.dumps(newPageData, indent=2))

    res = requests.post(create_url, headers=headers, json=newPageData)
    print('Creating page: ' + str(res.status_code))

    if res.status_code != 200:
        print('Error response from Notion API:')
        print(res.text)

if __name__ == "__main__":
    # Temporary test values (replace with real ones)
	print("We made it to here")
	database_id = "1f2152b71a3b80a49083fbff5e87b744"
	headers = {
	"Authorization": "Bearer ntn_c5682698811a4oBW4gs2vZ5Svc4t8KZ96G54BBhRT0Q6jm",
	"Content-Type": "application/json",
	"Notion-Version": "2022-06-28"
    	}

    # Example input values
	auth_year = "Smith et al., 2023"
	journal = "Nature"
	title = "A Groundbreaking Paper"

	createPage(database_id, headers, auth_year, journal, title)