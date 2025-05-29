from pybtex.database.input import bibtex
import requests, json
import csv
import notion_api as na
from jsonmerge import merge

with open("../notion_ids.csv", 'r') as f:
    f_csv = f.read().splitlines()
database_id = f_csv[1]
secret = f_csv[2]

print("Database ID:", database_id)
print("Notion Token:", secret[:8] + "...")

headers_read = {
    "Authorization": "Bearer " + secret,
    "Notion-Version": "2022-02-22"
}
headers_query = {
    "Authorization": "Bearer " + secret,
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json"
}
headers_create = {
    "Authorization": "Bearer " + secret,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22",
}

b = 0
PageData = {}
numPages = {}
PageData[b] = na.queryDatabase(database_id, headers_query)

while PageData[b]['has_more']:
    next_cursor = PageData[b]['next_cursor']
    PageData[b+1] = na.queryDatabase_again(database_id, headers_query, next_cursor)
    b += 1

existing_titles = set()
for page_num in range(b + 1):
    for entry in PageData[page_num]['results']:
        title_prop = entry['properties']['Title']
        rich_text = title_prop.get('rich_text', [])
        if rich_text:
            title_text = rich_text[0]['text']['content'].strip().lower()
            existing_titles.add(title_text)

print('There are ' + str(len(existing_titles)) + ' existing entries on Notion.\n')

parser = bibtex.Parser()
bibdata = parser.parse_file("references.bib")

count = 0
for bib_id in bibdata.entries:

    b = bibdata.entries[bib_id]

    paper_title = bibdata.entries[bib_id].fields['title']
    first_author = bib_id[:-3]
    author_list = bibdata.entries[bib_id].persons['author']
    
    if 'journal' in bibdata.entries[bib_id].fields:
        journal_name = bibdata.entries[bib_id].fields['journal']
    elif 'publisher' in bibdata.entries[bib_id].fields:
        journal_name = bibdata.entries[bib_id].fields['publisher']
    elif 'URLs' in bibdata.entries[bib_id].fields:
        journal_name = bibdata.entries[bib_id].fields['URLs']
    elif 'archivePrefix' in bibdata.entries[bib_id].fields:
        journal_name = bibdata.entries[bib_id].fields['archivePrefix']

    year_pub = bibdata.entries[bib_id].fields['year']

    if len(author_list) > 2:
        auth_year = first_author[:-4] + ' et. al.,' + year_pub
    elif len(author_list) == 1:
        auth_year = first_author[:-4] + ', ' + year_pub
    if len(author_list) == 2:
        prim_auth = str(author_list[0]).split(", ")[0]
        sec_auth = str(author_list[1]).split(", ")[0]
        auth_year = prim_auth + " & " + sec_auth + ", " + year_pub


    if paper_title.strip().lower() not in existing_titles:
        count += 1
        na.createPage(database_id, headers_create, auth_year, str(journal_name), paper_title)

print('Success: ' + str(count) + ' new entries were added to Notion!')
