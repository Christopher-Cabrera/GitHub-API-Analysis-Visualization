import requests
import json
import os   
import sqlite3
from outcome import capture
import http.client
from bs4 import BeautifulSoup
import json
import pandas as pd

#connect to db
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
db_path = os.path.join(BASE_DIR, "git_repo.db")
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

#create sql tables
cursor.execute("""DROP TABLE IF EXISTS repos""")
cursor.execute("""CREATE TABLE IF NOT EXISTS repos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
link TEXT NOT NULL,
language TEXT,
stargazers INT,
forks INT,
open_issues INT,
created_on DATETIME,
Project_type TEXT,
description TEXT,
topics TEXT);""")
from repo_scraper import api_repos
#repo list

token = os.getenv("GITHUB_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

#get request for api

def get_repo(url):
    response = requests.get(url, headers=headers)
#debugging
    if response.status_code != 200:
        return
    data1 = response.json()
    #find json structure in order to parse data
    print (data1)

    #page specific data withinjson rersponse
    repo_data = data1

    
    name = repo_data["name"]
    link = repo_data["html_url"]
    language = repo_data["language"]
    stargazers = repo_data["stargazers_count"]
    forks = repo_data["forks_count"]
    open_issues  = repo_data["open_issues"]
    created_on = repo_data["created_at"]
    project_type = repo_data["owner"]["type"]
    description = repo_data["description"]
    topics = repo_data["topics"]
    #convert json list into json string
    topics_json = json.dumps(topics)

            #insert into sql tables
    cursor.execute("""INSERT INTO repos(name, link, language, stargazers, forks, open_issues, created_on,project_type, description, topics)
    VALUES(?,?,?,?,?,?,?,?,?,?)""", (name, link, language, stargazers, forks, open_issues, created_on,project_type, description,topics_json))
   # print(name, link, language, stargazers, forks, open_issues, created_on, project_type,description)

for url in api_repos:
    get_repo(url)

connection.commit()
