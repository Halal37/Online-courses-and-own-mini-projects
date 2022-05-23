import requests
from bs4 import BeautifulSoup;
import re
import pandas as pd
from club_fminside import getClubInfo

headers = {'User-Agent': 
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
           'Accept' : 
           'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
# urls = [
# 'https://fminside.net/players/2-fm-22/29161106-ronaldo-vieira',
# 'https://fminside.net/players/2-fm-22/43317933-hamed-junior-traore',
# 'https://fminside.net/players/2-fm-22/35017428-marc-andre-ter-stegen',
# 'https://fminside.net/players/2-fm-22/18004418-eden-hazard',
# 'https://fminside.net/players/2-fm-22/721326-kamil-grosicki',
# 'https://fminside.net/players/2-fm-22/91003497-lasse-sobiech',
# 'https://fminside.net/players/2-fm-22/54006889-artur-sobiech',
# 'https://fminside.net/players/2-fm-22/14110660-lautaro-martinez',
# 'https://fminside.net/players/2-fm-22/96145145-kacper-kozlowski',
# 'https://fminside.net/players/2-fm-22/17011618-mikhail-kozlov',
# 'https://fminside.net/players/2-fm-22/2000046143-gabriel-misehouy',
# 'https://fminside.net/players/2-fm-22/37088406-julian-rijkhoff',
# 'https://fminside.net/players/2-fm-22/52014865-stuart-dallas',
# 'https://fminside.net/players/2-fm-22/18097159-alexis-saelemaekers',
# 'https://fminside.net/players/2-fm-22/38037430-szilveszter-hangya',
# 'https://fminside.net/players/2-fm-22/38041412-daniel-salloi',
# 'https://fminside.net/players/2-fm-22/12029963-yassine-bounou',
# 'https://fminside.net/players/2-fm-22/92017506-odysseas-vlachodimos',
# 'https://fminside.net/players/2-fm-22/14166615-cesar-ibanez',
# 'https://fminside.net/players/2-fm-22/29222614-soufiane-rahimi',
# 'https://fminside.net/players/2-fm-22/14135256-norberto-briasco',
# 'https://fminside.net/players/2-fm-22/42061427-gabi-kanichowsky',
# 'https://fminside.net/players/2-fm-22/48036350-aissa-laidouni',
# 'https://fminside.net/players/2-fm-22/63023419-miroslav-kacer',
# 'https://fminside.net/players/2-fm-22/79024208-luis-amarilla',
# 'https://fminside.net/players/2-fm-22/59006259-grigor-meliksetyan',
# 'https://fminside.net/players/2-fm-22/58085193-arshak-koryan',
# 'https://fminside.net/players/2-fm-22/53088903-martin-ellingsen',
# 'https://fminside.net/players/2-fm-22/19226437-otavio',
# 'https://fminside.net/players/2-fm-22/43093936-danilo-cataldi',
# 'https://fminside.net/players/2-fm-22/2000142821-felipe-sanchez',
# 'https://fminside.net/players/2-fm-22/2000100625-mateja-bubanj',
# 'https://fminside.net/players/2-fm-22/37084998-iggy-houben',
# 'https://fminside.net/players/2-fm-22/2000077702-luis-valdez',
# 'https://fminside.net/players/2-fm-22/67085965-suso',
# 'https://fminside.net/players/2-fm-22/54004036-lukasz-burliga',
# 'https://fminside.net/players/2-fm-22/96075388-mateusz-lis',
# 'https://fminside.net/players/2-fm-22/96027391-filip-starzynski',
# 'https://fminside.net/players/2-fm-22/54000966-artur-jedrzejczyk',
# 'https://fminside.net/players/2-fm-22/713854-artur-boruc',
# 'https://fminside.net/players/2-fm-22/96061971-taras-romanczuk',
# 'https://fminside.net/players/2-fm-22/96011096-rafal-wolski',
# 'https://fminside.net/players/2-fm-22/96010344-kamil-drygas',
# 'https://fminside.net/players/2-fm-22/96003382-michal-kucharczyk',
# 'https://fminside.net/players/2-fm-22/96111188-bartosz-slisz',
# 'https://fminside.net/players/2-fm-22/96002753-maciej-gajos',
# 'https://fminside.net/players/2-fm-22/19359019-conrado',
# 'https://fminside.net/players/2-fm-22/8404400-pavels-teinbors',
# 'https://fminside.net/players/2-fm-22/67039209-flavio-paixao',
# 'https://fminside.net/players/2-fm-22/55022487-luis-rocha',
# 'https://fminside.net/players/2-fm-22/55038682-tomas-podstawski',
# 'https://fminside.net/players/2-fm-22/55070306-luis-mata',
# 'https://fminside.net/players/2-fm-22/84109364-luquinhas',
# 'https://fminside.net/players/2-fm-22/19148891-rivaldinho',
# 'https://fminside.net/players/2-fm-22/67227812-chuca',
# 'https://fminside.net/players/2-fm-22/67102055-jesus-imaz',
# 'https://fminside.net/players/2-fm-22/67209472-jesus-jimenez',
# 'https://fminside.net/players/2-fm-22/67179962-fernan-ferreiroa',
# 'https://fminside.net/players/2-fm-22/14000745-mateo-musacchio',
# 'https://fminside.net/players/2-fm-22/98004008-loris-benito',
# 'https://fminside.net/players/2-fm-22/43001238-mario-balotelli',
# 'https://fminside.net/players/2-fm-22/5127717-daniel-sturridge',
# 'https://fminside.net/players/2-fm-22/29024338-jack-wilshere',
# 'https://fminside.net/players/2-fm-22/62070825-matej-pucko',
# 'https://fminside.net/players/2-fm-22/62094092-luka-zahovic',
# 'https://fminside.net/players/2-fm-22/96088106-przemyslaw-placheta',
# 'https://fminside.net/players/2-fm-22/96115556-maciej-zurawski',
# 'https://fminside.net/players/2-fm-22/96021109-andreja-prokic',
# 'https://fminside.net/players/2-fm-22/96011267-maciej-domanski',

# ]
# def details(soup,column,index):
#               meta=soup.find_all("div", {"class": "meta"})

#               temporary_data = [[cell.text for cell in row("td")]
#                          for row in column[index[0]].findAll("tr")]
#               temporary_data1 = [[cell.text for cell in row("td")]
#                          for row in column[index[1]].findAll("tr")]
#               temporary_data2 = [[cell.text for cell in row("td")]
#                          for row in column[index[2]].findAll("tr")]
#               span=soup.find("span", {"title": "This players maximum potential, stats generated are speculative"}).get("class")
#               return span[1],temporary_data,temporary_data1,temporary_data2,meta

def getPlayerInfo(playerPageUrl):
  #empty lists
    data=[];playerClubData=[];technicalscrape=[];mentalscrape=[];physicalscrape=[]
    potencial=[];linkversion=[];versiondate=[];iscontractexpires=[False,False]
    for i in range(2):
     if i==0:
      linkversion.append(playerPageUrl)
      pageTree = requests.get(playerPageUrl)
     else:
      linkversion.append(playerPageUrl.replace('-22','-21').replace('s/2','s/1'))
      pageTree = requests.get(playerPageUrl.replace('-22','-21').replace('s/2','s/1'))
     soup = BeautifulSoup(pageTree.content, 'html.parser')	
     column=soup.find_all("div", {"class": "column"})
     
     if len(column)==2:
        print(" Tyle bylo", len(column))
        if i==0:
         continue
        if i==1:
          break
     if len(column)==7:
              print(" Tyle bylo", len(column))
              iscontractexpires[i]=True
              meta=soup.find_all("div", {"class": "meta"})

              temporary_data = [[cell.text for cell in row("td")]
                         for row in column[2].findAll("tr")]
              temporary_data1 = [[cell.text for cell in row("td")]
                         for row in column[3].findAll("tr")]
              temporary_data2 = [[cell.text for cell in row("td")]
                         for row in column[4].findAll("tr")]
              span=soup.find("span", {"title": "This players maximum potential, stats generated are speculative"}).get("class")
              potencial.append(span[1])
              technicalscrape.append(temporary_data)
              mentalscrape.append(temporary_data1)
              physicalscrape.append(temporary_data2)
              playerClubData.append(meta)
              data.append(column)
     else:
      print(" Tyle bylo", len(column))
      meta=soup.find_all("div", {"class": "meta"})

      temporary_data = [[cell.text for cell in row("td")]
                         for row in column[3].findAll("tr")]
      temporary_data1 = [[cell.text for cell in row("td")]
                         for row in column[4].findAll("tr")]
      temporary_data2 = [[cell.text for cell in row("td")]
                         for row in column[5].findAll("tr")]
      span=soup.find("span", {"title": "This players maximum potential, stats generated are speculative"}).get("class")
      potencial.append(span[1])
      technicalscrape.append(temporary_data)
      mentalscrape.append(temporary_data1)
      physicalscrape.append(temporary_data2)
      playerClubData.append(meta)
      data.append(column)
#empty lists
    clubs = []; version = []; contractExpires= [];wages= [];nationality=[];weight=[];length=[]
    foot=[];age=[];ca=[];pa=[];position=[];firstname=[];lastname=[]
    technicalgoalkeeper= [ [] for _ in range(3) ];physical = [ [] for _ in range(8) ]
    goalkeeping = [ [] for _ in range(13) ]; technical = [ [] for _ in range(14) ]
    mental=[ [] for _ in range(14) ];values=[]
   
    for i in range(len(data)):
      table=data[i][0].get_text(" ")
      list_of_words = table.split()
      table2=data[i][1].get_text(" ")
      list_of_words2 = table2.split()
      age.append(list_of_words[list_of_words.index("Age") + 1])
      lastname.append(list_of_words[list_of_words.index("Age") - 1])
      firstname.append(re.search(f'Name(.*){list_of_words[list_of_words.index("Age") - 1]}',table).group(1).strip())

      foot.append(list_of_words[list_of_words.index("Foot") + 1])
      position.append(list_of_words[list_of_words.index("Position") + 1])
      length.append(list_of_words[list_of_words.index("Length") + 1])
      weight.append(list_of_words[list_of_words.index("Weight") + 1])
      if iscontractexpires[i]==True:
        values.append("0")
        wages.append("0")
        contractExpires.append("")
      else:
       values.append("€ "+ list_of_words2[list_of_words2.index("Wages") - 1].replace(',',".") )
       wages.append("€ "+ list_of_words2[list_of_words2.index("Wages") + 2].replace(',',".") )
       contractExpires.append(list_of_words2[list_of_words2.index("end") + 1] )

    for i in range(len(playerClubData)):
      list_of_words=playerClubData[i][0].get_text(" ").splitlines()
      if iscontractexpires[i]==True:
        nationality.append(list_of_words[4].strip())
        clubs.append('')
      elif '..' in list_of_words[4].strip():
        clubs.append(getClubInfo(linkversion[i]))
        nationality.append(list_of_words[5].strip())
      else:
       clubs.append(list_of_words[4].strip())
       nationality.append(list_of_words[5].strip())
      ca.append(list_of_words[2].split()[0])
      if len(list_of_words[2].split())==2:
       pa.append(list_of_words[2].split()[1])
      else:
       pa.append(potencial[i].replace('superstar','80-100').replace('excellent','70-90').replace('good','60-80').replace('decent','50-70').replace('decent','50-70').replace('poor','40-60'))

    for i in range(len(technicalscrape)):
      if position[i]=="GK":
        for j in range(len(goalkeeping)):
          goalkeeping[j].append(technicalscrape[i][j][1])

      else:
        for j in range(len(technical)):
          technical[j].append(technicalscrape[i][j][1])


    for i in range(len(mentalscrape)):
      for j in range(len(mental)):
       mental[j].append(mentalscrape[i][j][1])
    for i in range(len(physicalscrape)):
      for j in range(len(physical)):
       physical[j].append(physicalscrape[i][j][1])

      if position[i]=="GK":
        for j in range(len(technicalgoalkeeper)):
          technicalgoalkeeper[j].append(physicalscrape[i][j+8][1])

    link = playerPageUrl.split("https://fminside.net/players/2-fm-22/")[1].split(".html")[0]
    id=link.split('-',1)[0]
    for i in linkversion:
     link=i.split("https://fminside.net/players/")[1].split(".html")[0]
     version.append("2"+link.split('-',1)[0])
    for i in range(len(version)):
     if version[i]=='21':
      versiondate.append("2020-11-23")
     else:
      versiondate.append("2021-11-8")
    if position[0]=="GK":
      return {
         "id": id,
         "firstName": firstname,
         "lastName": lastname,
         "club": clubs,
         "values": values,
         "wages": wages,
         "contractexpires":contractExpires,
         "nation": nationality,
         "currentAbility":ca,
         "potentialAbility":pa,
         "position":position,
         "version":version,
         "date":versiondate,
                         
         "aerialReach":goalkeeping[0],
         "commandofArea":goalkeeping[1],
         "communication":goalkeeping[2],
         "eccentricity":goalkeeping[3],
         "firstTouch":goalkeeping[4],
         "handling":goalkeeping[5],
         "kicking":goalkeeping[6],
         "oneonOnes":goalkeeping[7],
         "passing":goalkeeping[8],
         "punchingTendency":goalkeeping[9],
         "reflexes":goalkeeping[10],
         "rushingoutTendency":goalkeeping[11],
         "throwing":goalkeeping[12],

         "aggression":mental[0],
         "anticipation":mental[1],
         "bravery":mental[2],
         "composure":mental[3],
         "concentration":mental[4],
         "decisions":mental[5],
         "determination":mental[6],
         "flair":mental[7],
         "leadership":mental[8],
         "offtheBall":mental[9],
         "positioning":mental[10],
         "teamwork":mental[11],
         "vision":mental[12],
         "workRate":mental[13],

         "acceleration":physical[0],
         "agility":physical[1],
         "balance":physical[2],
         "jumpingReach":physical[3],
         "naturalFitness":physical[4],
         "pace":physical[5],
         "stamina":physical[6],
         "strength":physical[7],

         "freeKickTaking":technicalgoalkeeper[0],
         "penaltyTaking":technicalgoalkeeper[1],
         "technique":technicalgoalkeeper[2],
     }
    else:
      return{
         "id": id,
         "firstName": firstname,
         "lastName": lastname,
         "club": clubs,
         "values": values,
         "wages": wages,
         "contractexpires":contractExpires,
         "nation": nationality,
         "currentAbility":ca,
         "potentialAbility":pa,
         "position":position,
         "version":version,
         "date":versiondate,

         "corners":technical[0],
         "crossing":technical[1],
         "dribbling":technical[2],
         "finishing":technical[3],
         "firstTouch":technical[4],
         "freeKickTaking":technical[5],
         "heading":technical[6],
         "longShots":technical[7],
         "longThrows":technical[8],
         "marking":technical[9],
         "passing":technical[10],
         "penaltyTaking":technical[11],
         "tackling":technical[12],
         "technique":technical[13],

         "aggression":mental[0],
         "anticipation":mental[1],
         "bravery":mental[2],
         "composure":mental[3],
         "concentration":mental[4],
         "decisions":mental[5],
         "determination":mental[6],
         "flair":mental[7],
         "leadership":mental[8],
         "offtheBall":mental[9],
         "positioning":mental[10],
         "teamwork":mental[11],
         "vision":mental[12],
         "workRate":mental[13],

         "acceleration":physical[0],
         "agility":physical[1],
         "balance":physical[2],
         "jumpingReach":physical[3],
         "naturalFitness":physical[4],
         "pace":physical[5],
         "stamina":physical[6],
         "strength":physical[7],
     }

def main():
    urls2 = pd.read_csv("csv_without.csv",delimiter=",")
    allPlayerData = []  
    allGoalkeepersData=[]  
 #   for url in urls:
    for iteration,url in enumerate(urls2["Fminside Link"]):
        print(iteration)
        playerData=getPlayerInfo(url)
        if playerData["position"][0]=='GK':
          allGoalkeepersData.append(playerData)
        else:
          allPlayerData.append(playerData)

    players=pd.DataFrame.from_dict(allPlayerData)
    goalkeepers=pd.DataFrame.from_dict(allGoalkeepersData)
       
    players=(players.set_index('id')
   .apply(lambda x: x.apply(pd.Series).stack())
   .reset_index()
   .drop('level_1', 1).dropna())

    goalkeepers=(goalkeepers.set_index('id')
   .apply(lambda x: x.apply(pd.Series).stack())
   .reset_index()
   .drop('level_1', 1).dropna())  

    players.to_csv("playersfm2.csv")
    goalkeepers.to_csv("goalkeepersfm2.csv")
main()