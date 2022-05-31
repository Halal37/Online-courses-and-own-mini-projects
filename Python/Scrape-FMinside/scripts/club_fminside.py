from bs4 import BeautifulSoup
import requests
import re

def getClubInfo(playerPageUrl):
    pageTree = requests.get(playerPageUrl)
    soup = BeautifulSoup(pageTree.content, 'html.parser')	
    column=soup.find("div", {"id": "player_info"})
    project_href = [i['href'] for i in column.find_all('a', href=True)]
    pageTree = requests.get('https://fminside.net'+project_href[0])
    soup = BeautifulSoup(pageTree.content, 'html.parser')	
    column=soup.find("div", {"class": "column"})
    clubtext=column.get_text(" ")
    clubName=re.search(f'Name(.*)',clubtext).group(1).strip()
    return clubName
