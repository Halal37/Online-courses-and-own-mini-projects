import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
page2_3 = pd.read_csv("csv_fminside.csv",delimiter=",")
page2_3=page2_3[page2_3["Fminside Link"].str.contains('https://fminside.net/players/')]
page2_3=page2_3[['Player Name','Season','Team Name','Fminside Link']]
sections=[]
for i in range(0, len(page2_3)):   
    sections.append(page2_3['Fminside Link'].iloc[i].split("players/", 2))
    if sections[i][1].find("2-fm-22/")==-1:
        if sections[i][1].find("1-fm-21/")==0:
         print(sections[i][0]," ",sections[i][1])
         sections[i][1]=sections[i][1].split("1-fm-21/", 2)[1]
         print(sections[i][1])
        page2_3['Fminside Link'].iloc[i]=sections[i][0] + "players/2-fm-22/" + sections[i][1]
page2_3[['Player Name','Season','Team Name','Fminside Link']].to_csv("csv_without.csv")