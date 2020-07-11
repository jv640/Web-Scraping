import requests 
from bs4 import BeautifulSoup
import html5lib as h5l
import json
import pandas as pd
import os
import time

r = requests.get("https://en.wikipedia.org/wiki/List_of_Indian_Premier_League_venues")
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')

stadium_det = [['Stadium', 'Home Teams']]

table = soup.find("tbody").find_all("tr")
table = table[1:]       # Removing table Heading 

for rows in table:
    row = rows.find_all("td")
    stadium_name = row[0].getText().strip('\n')
    home_team = []
    home_teams = row[5].find_all("a")
    for team in home_teams:
        home_team.append(team.getText())
    
    temp = [stadium_name, home_team]
    stadium_det.append(temp)

df = pd.DataFrame(stadium_det)
df.to_csv('Stadium_and_Home_Teams.csv')
print("Done")

