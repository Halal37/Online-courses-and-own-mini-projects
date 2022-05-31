import pandas as pd
import numpy as np
import unidecode

def fixed(merged):
    merged=merged.rename(columns={"version":"season"})
    merged=merged.replace({'season': {22: '2021/2022', 21: '2020/2021'}})
    merged["firstName"]=merged['firstName'].astype(str).str[0]+"."
    merged=merged.replace({'firstName': {'n.': np.nan}})
    merged["lastName"] = merged["lastName"].apply(unidecode.unidecode)
    return merged

csvplayers= pd.read_csv("playersfm2.csv")
csvgoalkeepers = pd.read_csv("goalkeepersfm2.csv")
page2_3 = pd.read_csv("page2-3_-_data_to_get.csv",delimiter=";")

playername=page2_3["Player Name"].str.split(" ",1, expand=True)
playername=playername.rename(columns={0:"lastName",1:"firstName"})
playername["lastName"] = playername["lastName"].apply(unidecode.unidecode)
merged = pd.concat([page2_3,playername],axis=1)

merged=merged.rename(columns={"Season":"season","Team Name":"club"})
players=fixed(csvplayers)
goalkeepers=fixed(csvgoalkeepers)
merged=merged.fillna(value=np.nan)
mergedplayers=merged.merge(players,on=['lastName','club','season','firstName'])
mergedgoalkeepers=merged.merge(goalkeepers,on=['lastName','club','season','firstName'])
mergedplayers.to_csv("mergeplayers2.csv")
mergedgoalkeepers.to_csv("mergegoalkeepers2.csv")