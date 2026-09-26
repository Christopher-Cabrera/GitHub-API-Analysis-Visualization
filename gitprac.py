import requests
import json
import os   
import sqlite3
from outcome import capture
import http.client
from bs4 import BeautifulSoup
import json

#connect to db
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
db_path = os.path.join(BASE_DIR, "db", "git_repo.db")
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
created_on DATETIME);""")
from repo_scraper import api_repos
#repo list
repos = ["https://api.github.com/repos/msitarzewski/agency-agents",
"https://api.github.com/repos/addyosmani/agent-skills",
"https://api.github.com/repos/ZhuLinsen/daily_stock_analysis",
"https://api.github.com/repos/vitali87/code-graph-rag",
"https://api.github.com/repos/paperclipai/paperclip",
"https://api.github.com/repos/google/skills",
"https://api.github.com/repos/Comfy-Org/ComfyUI",
"https://api.github.com/repos/HKUDS/DeepTutor",
"https://api.github.com/repos/github/copilot-sdk",
"https://api.github.com/repos/microsoft/AI-For-Beginners",
"https://api.github.com/repos/chatwoot/chatwoot",
"https://api.github.com/repos/usekaneo/kaneo",
"https://api.github.com/repos/1jehuang/jcode",
"https://api.github.com/repos/PrimeIntellect-ai/prime-agent",
"https://api.github.com/repos/google-deepmind/weathernext",
"https://api.github.com/repos/goauthentik/authentik",
"https://api.github.com/repos/anthropics/skills",
"https://api.github.com/repos/different-ai/openwork",
"https://api.github.com/repos/paperswithbacktest/awesome-systematic-trading",
"https://api.github.com/repos/harry0703/MoneyPrinterTurbo",
"https://api.github.com/repos/n8n-io/n8n",
"https://api.github.com/repos/langflow-ai/langflow",
"https://api.github.com/repos/ollama/ollama",
"https://api.github.com/repos/open-webui/open-webui",
"https://api.github.com/repos/immich-app/immich",
"https://api.github.com/repos/semantica-agi/semantica",
"https://api.github.com/repos/volcengine/OpenViking",
"https://api.github.com/repos/OpenCut-app/OpenCut",
"https://api.github.com/repos/microsoft/agent-lightning",
"https://api.github.com/repos/microsoft/TRELLIS.2",
"https://api.github.com/repos/TencentCloud/TencentDB-Agent-Memory",
"https://api.github.com/repos/iv-org/invidious",
"https://api.github.com/repos/ansible/ansible",
"https://api.github.com/repos/andrewyng/aisuite",
"https://api.github.com/repos/moeru-ai/airi",
"https://api.github.com/repos/pranshuparmar/witr",
"https://api.github.com/repos/3b1b/manim",
"https://api.github.com/repos/huggingface/transformers",
"https://api.github.com/repos/nautechsystems/nautilus_trader",
"https://api.github.com/repos/usestrix/strix",
"https://api.github.com/repos/akitaonrails/ai-memory",
"https://api.github.com/repos/santifer/career-ops",
"https://api.github.com/repos/jundot/omlx",
"https://api.github.com/repos/cathrynlavery/diagram-design",
"https://api.github.com/repos/nvm-sh/nvm"]

token = os.getenv("GITHUB_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

#get request for api

def get_repo(url):
    response = requests.get(url, headers=headers)
    
    data1 = response.json()
    #find json structure in order to parse data
    #print (data1)

    #page specific data withinjson rersponse
    repo1_data = data1

    name = repo1_data["name"]
    link = repo1_data["html_url"]
    language = repo1_data["language"]
    stargazers = repo1_data["stargazers_count"]
    forks = repo1_data["forks_count"]
    open_issues  = repo1_data["open_issues"]
    created_on = repo1_data["created_at"]

            #insert into sql tables
    cursor.execute("""INSERT INTO repos(name, link, language, stargazers, forks, open_issues, created_on)
    VALUES(?,?,?,?,?,?,?)""", (name, link, language, stargazers, forks, open_issues, created_on))
   # print(name, link, language, stargazers, forks, open_issues, created_on )

for url in api_repos:
    get_repo(url)

connection.commit()