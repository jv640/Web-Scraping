import requests 
from bs4 import BeautifulSoup
import html5lib as h5l
import json
import pandas as pd
import os
import time

X = [['ID', 'Season', 'Home', 'Away', 'TossWin', 'TossDec', 'Venue', 'Winner']]

webpages = ["https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2007/08;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2009;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2010;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2011;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2012;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2013;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2014;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2015;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2016;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2017;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2018;trophy=117;type=season",
            "https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=2019;trophy=117;type=season"
        ]

# For Match ID
match_id = 1

# Iterating over Given webpages of Seasonal Match
for page in webpages:
    r = requests.get(page)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    # print(soup)
    # print(soup.prettify)
    
    # Finding link for all Matches Summary in given Season
    links = soup.find_all("a", class_ = "data-link", text = "T20")

    # Iterating over Matches
    for link in links:
        # print(link['href'])
        print("https://stats.espncricinfo.com" + link['href'])
        r = requests.get("https://stats.espncricinfo.com:443" + link['href'])
        # r = requests.get("https://stats.espncricinfo.com/ci/engine/match/733991.html")
        htmlContent = r.content
        soup = BeautifulSoup(htmlContent, 'html.parser')

        #finding Season
        Season_var = soup.find("a", class_ = "d-block").getText()
        season = Season_var[-4:]
        # print(season)

        #finding Short Names of Teams
        teams = []
        T = soup.find_all("a", class_ = "team-name")
        for tt in T:
            teams.append(tt.getText())

        # Finding Full Names of Teams
        full_team_names = []
        TN = soup.find_all("a", class_ = "team-name")
        for ttt in TN:
            span = ttt.find("span")
            full_team_names.append(span['title'])
        # print(full_team_names)

        # Toss Details
        toss_det = soup.find("td", text = "Toss").findNext("td").getText()
        toss_det = toss_det.split(',')
        if len(toss_det) == 2:
            toss_det[0] = toss_det[0][:-1]
            
            # Toss Winner
            toss_win = ""
            # print(toss_det[0],len(toss_det[0]), full_team_names[0], len(full_team_names[0]))
            if toss_det[0] == full_team_names[0]:
                toss_win = toss_win + "Team 1"
                # print(toss_det[0], full_team_names[0])
            else:
                toss_win = toss_win + "Team 2"
                # print(toss_det[0], full_team_names[1])
            # print(toss_win)
            
            # Toss Decision
            toss_array = toss_det[1].split()
            toss_dec = toss_array[2]
            # print(toss_dec)
        else:
            toss_win = "none"
            toss_dec = "none"

        # Finding Ground
        full_place = soup.find("td", class_ = "match-venue").getText()
        places = full_place.split(',')
        stadium = places[0]
        
        # Finding Winner of match
        win = ""
        winner_tag = soup.find("td", text = "Points")
        
        if winner_tag != None:
            winner_tagg = winner_tag.findNext("td").getText()
            winner_arr = winner_tagg.split(',')
            # print(winner_arr[0])
            # print(winner_arr[0][-1])
            # print(winner_arr[0][:-2])
            if winner_arr[0][-1] == 1:
                win = win + "Tie"
                # print(winner_arr, win)
            elif winner_arr[0][:-2] == full_team_names[0]:
                win = win + "Team 1"
                # print(winner_arr[0][:-2], full_team_names[0], win)
            else:
                win = win + "Team 2"
                # print(winner_arr[0][:-2], full_team_names[1], win)
            # print(win)
        else:
            lose = soup.find("span", class_ = "score-run-gray")['title']
            if lose != full_team_names:
                win = win + "Team 1"
            else:
                win = win + "Team 2"

            # print(lose)


        
        temp = [match_id, season, teams[0], teams[1], toss_win, toss_dec, stadium, win]
        del season, teams, toss_win, toss_dec, stadium, win
        match_id = match_id + 1
        X.append(temp)
        del temp
        print("Running", match_id-1)
        del soup
        # time.sleep(2)
    # del soup

df = pd.DataFrame(X)
df.to_csv('Matches.csv')
print("Completed")


