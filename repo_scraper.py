import requests
from bs4 import BeautifulSoup

repos = []
base_url = "https://gitstar-ranking.com/repositories"
for page in range(1,11):
    url = f"{base_url}?page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a",class_= "paginated_item"):
        #print(link.get("href"))
        href = link.get("href")
        repos.append(href)
#print(repos)
api_repos = []
for repo in repos:
    api_url = f"https://api.github.com/repos" + repo
    #print(api_url)
    api_repos.append(api_url)
#print(api_repos)

    #if href and "github.com" in href:
    #    repos.append(href)
print(len(repos))