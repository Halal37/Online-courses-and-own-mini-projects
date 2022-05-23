from datetime import date
import requests
import json
import csv
from bs4 import BeautifulSoup;

csvFile = "scraped.csv"
headersCSV = ["firstName", "lastName", "date", "club at date", "market value at date"]   

headers = {'User-Agent': 
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
           'Accept' : 
           'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

urls = [
    "https://www.transfermarkt.com/jadon-sancho/profil/spieler/401173",
    "https://www.transfermarkt.com/mohamed-salah/profil/spieler/148455",
    "https://www.transfermarkt.com/erling-haaland/profil/spieler/418560",
    "https://www.transfermarkt.com/vinicius-junior/profil/spieler/371998",
    "https://www.transfermarkt.com/mohamed-salah/profil/spieler/148455",
    "https://www.transfermarkt.com/harry-kane/profil/spieler/132098",
    "https://www.transfermarkt.com/raheem-sterling/profil/spieler/134425",
    "https://www.transfermarkt.com/pedri/profil/spieler/683840",
    "https://www.transfermarkt.com/lautaro-martinez/profil/spieler/406625",
    "https://www.transfermarkt.com/jules-kounde/profil/spieler/411975",
    "https://www.transfermarkt.com/victor-osimhen/profil/spieler/401923",
    "https://www.transfermarkt.com/eder-militao/profil/spieler/401530",
    "https://www.transfermarkt.com/gabriel-jesus/profil/spieler/363205",
    "https://www.transfermarkt.com/diogo-jota/profil/spieler/340950",
    "https://www.transfermarkt.com/alessandro-bastoni/profil/spieler/315853",
    "https://www.transfermarkt.com/marcos-llorente/profil/spieler/282411",
    "https://www.transfermarkt.com/wilfred-ndidi/profil/spieler/274839",
    "https://www.transfermarkt.com/fabinho/profil/spieler/225693",
    "https://www.transfermarkt.com/joao-cancelo/profil/spieler/182712",
]

def getPlayerInfo(playerPageUrl):
    pageTree = requests.get(playerPageUrl, headers = headers)
    soup = BeautifulSoup(pageTree.content, 'html.parser')
    script = soup.find_all('script')
    print(script)
    script = ' '.join([str(elem) for elem in script])
    chartCode = script.split("var chart = new Highcharts.Chart")[1]
    dataWithPadding = chartCode.split("'data':")[1]
    data = dataWithPadding.split("}],'legend'")[0]
    data = data.encode().decode('unicode-escape')
    data = data.replace("\'", "\"")
    data = json.loads(data)

    clubs = [""] * len(data)
    dates = [""] * len(data)
    marketValues = [""] * len(data)

    for i in range(len(data)):
        clubs[i] = data[i]["verein"]
        dates[i] = data[i]["datum_mw"]
        marketValues[i] = data[i]["mw"]
        marketValues[i] = marketValues[i].replace("€", "")

    player = playerPageUrl.split("transfermarkt.com/")[1]
    player = player.split("/profil")[0]
    if "-" in player:
        player = player.split("-")
        firstName = (player[0]).capitalize()
        lastName = (player[1]).capitalize()
    else:
        firstName = player
        lastName = ""
        
    return {
        "firstName": firstName,
        "lastName": lastName,
        "clubs": clubs,
        "dates": dates,
        "marketValues": marketValues
    }

def main(outputToCsv = True):
    allPlayerData = []    
    for url in urls:
        allPlayerData.append(getPlayerInfo(url))

    if outputToCsv:
        with open(csvFile, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headersCSV)
            for playerData in allPlayerData:
                firstName = playerData["firstName"]
                lastName = playerData["lastName"]
                clubs = playerData["clubs"]
                dates = playerData["dates"]
                marketValues = playerData["marketValues"]
                for i in range(len(clubs)):
                    writer.writerow([firstName, lastName, clubs[i], dates[i], marketValues[i]])
            f.close()

main()