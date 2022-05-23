from datetime import date
import requests
import json
import csv
from bs4 import BeautifulSoup;
import re

csvFile = "fmscraped.csv"
headersCSV = ["id","firstName", "lastName", "version", "club at date", "market value at date","wages","contractexpires","dateofbirth","EU National"]   

headers = {'User-Agent': 
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
           'Accept' : 
           'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
urls = [
    'https://www.fmscout.com/player/67085965/suso.html',
    'https://www.fmscout.com/player/43008779/mattia-destro.html',
    'https://www.fmscout.com/player/43315178/junior-messias.html',
    'https://www.fmscout.com/player/67030699/kamil-glik.html',
    'https://www.fmscout.com/player/19190099/jemerson.html',
    'https://www.fmscout.com/player/13158205/victor-osimhen.html',
    'https://www.fmscout.com/player/55083779/diogo-jota.html',
    'https://www.fmscout.com/player/27000596/christian-gytkjaer.html',
    'https://www.fmscout.com/player/28108490/jadon-sancho.html',
    'https://www.fmscout.com/player/67293495/pedri.html',
    'https://www.fmscout.com/player/67142868/samu-castillejo.html',
    'https://www.fmscout.com/player/67080313/samu-sáiz.html',
    'https://www.fmscout.com/player/67269484/samuel-chukwueze.html',
    'https://www.fmscout.com/player/43317933/hamed-junior-traoré.html',
    'https://www.fmscout.com/player/19302146/vinícius-júnior.html',
    'https://www.fmscout.com/player/43318305/flavio-junior-bianchi.html',
    'https://www.fmscout.com/player/28000482/junior-hoilett.html',

]

def getPlayerInfo(playerPageUrl):
    data=[]
    for a in range(22,12,-1):
      if a==22:
          pageTree = requests.get(playerPageUrl)
      else:
       pageTree = requests.get(playerPageUrl+f'?rev={(a)}.0')#, headers = headers)
      soup = BeautifulSoup(pageTree.content, 'html.parser')	
      test=soup.find_all("div", {"class": "large-4 medium-6 columns"})

      if len(test)!=0:
          data.append(test)

    clubs = []
    version = []
    marketValues = []
    contractExpires= []
    wages= []
    eu=[]
    dateofBirth=[]
    for i in data:
      table=i[0].get_text(" ")
      list_of_words = table.split()
      table2=i[1].find("table").get_text(" ")
      list_of_words2 = table2.split()
      club_list=list_of_words2[list_of_words2.index('Club')+1:list_of_words2.index('Expires')]
      club=' '.join(str(e) for e in club_list)
      clubs.append( club )
      contractExpires.append(list_of_words2[list_of_words2.index("Expires") + 1] )
      marketValues.append(list_of_words2[list_of_words2.index("Value") + 1] )
      wages.append(list_of_words2[list_of_words2.index("Wage") + 1] )
      version.append(list_of_words[list_of_words.index("Details") + 1])
      dateofBirth.append(list_of_words[list_of_words.index("D.O.B.") + 1])
      eu.append(list_of_words[list_of_words.index("National") + 1])

    link = playerPageUrl.split("https://www.fmscout.com/player/")[1].split(".html")[0]
    player=link.rsplit('/',1)[1]
    id=link.rsplit('/',1)[0]
    if "-" in player:
     player = player.rsplit("-",1)
     firstName = (player[0].replace('-'," ")).title()
     lastName = (player[1]).capitalize()
    else:
     firstName = player.capitalize()
     lastName = ""
    return {
         "id": id,
         "firstName": firstName,
         "lastName": lastName,
         "clubs": clubs,
         "version": version,
         "marketValues": marketValues,
         "wages": wages,
         "contractexpires":contractExpires,
         "dateofbirth":dateofBirth,
         "EU National": eu,
     }

def main(outputToCsv = True):
    allPlayerData = []    
    for url in urls:
        allPlayerData.append(getPlayerInfo(url))

    if outputToCsv:
        with open(csvFile, 'a', encoding='UTF-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headersCSV)
            for playerData in allPlayerData:
                id = playerData["id"]
                firstName = playerData["firstName"]
                lastName = playerData["lastName"]
                clubs = playerData["clubs"]
                version = playerData["version"]
                marketValues = playerData["marketValues"]
                wages = playerData["wages"]
                contractExpires = playerData["contractexpires"]
                dateofBirth = playerData["dateofbirth"]
                eu = playerData["EU National"]
                for i in range(len(clubs)):
                    writer.writerow([id,firstName, lastName, clubs[i], version[i], marketValues[i],wages[i],contractExpires[i],dateofBirth[i],eu[i]])
            f.close()

main()