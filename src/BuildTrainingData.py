import Req
from Constants import *

import json

def boxscoreBreakdown(date):
    url = "http://stats.nba.com/js/data/widgets/boxscore_breakdown_{}.json".format(date)

    res = Req.get(url)

    for game in res['results']:
        gameID = game['GameID']

        homeTeam = game['HomeTeam']['teamName']
        awayTeam = game['AwayTeam']['teamName']

        homeID = getTeamID(homeTeam)
        awayID = getTeamID(awayTeam)

        homeData = extractTeamDataFromFile(homeTeam)
        awayData = extractTeamDataFromFile(awayTeam)

def extractTeamDataFromFile(teamName):
    with open('../Data/Teams.JSON') as infile:
        data = json.load(infile)

        return data[teamName]
