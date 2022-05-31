import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
def getPage(url, headers):
    try:
        req = requests.get(url, headers=headers)
        print(url)
    except requests.exceptions.RequestException:
        print("An error occured!")
        return None
    return BeautifulSoup(req.text, 'html.parser')

id = []
link=[]
page2_3 = pd.read_csv("page2-3_-_data_to_get.csv",delimiter=";")
page2_3 = page2_3[page2_3['Season']=='2020/2021']
page2_3 = page2_3.drop_duplicates(subset=['Player Name'])
page2_3 =page2_3[['Player Name','Season','Team Name']]
for i in range(0, len(page2_3)):   
    page2_3['Player Name'].iloc[i]=' '.join(page2_3['Player Name'].iloc[i].split())
page2_3 = page2_3.drop_duplicates(subset=['Player Name'])
page2_3['Player Name'].to_csv("player_names.csv")  
for i in range(0, len(page2_3)):
 id.append(i)
 link.append('')
page2_3['ID']=id
page2_3['Fminside Link']=link
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Language':'pl'}
links=[] 
names=[]         
for i in range(0, len(page2_3)):    

 url='https://www.bing.com/search?q={}+transfermarkt'.format(page2_3['Player Name'].iloc[i].replace(' ','+'))
 response = requests.get(
    url,
    headers=headers).text

 soup = BeautifulSoup(response, 'lxml')

 cos=soup.select('.b_algo h2 a')[0].get_text().split('-')[0]
 names.append(cos)

 url='https://www.bing.com/search?q={}+fminside'.format(cos.replace(' ','+'))
 
 response = requests.get(
    url,
    headers=headers).text

 soup = BeautifulSoup(response, 'lxml')
 link=soup.select('.b_algo h2 a')[0]['href']
 links.append(soup.select('.b_algo h2 a')[0]['href'])
 print(link)

page2_3['Fminside Link']=links
page2_3['Player Name']=names

page2_3.to_csv("csv_fminside.csv")  

