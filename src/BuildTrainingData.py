import Req
import URL
import IOUtils
from Constants import *

import json

def boxScoreBreakdown(date, teamData):
    print("Analyzing Data for: " + date)

    boxScore = Req.get(URL.boxScoreBreakdown(date))

    for game in boxScore['results']:
        gameID = game['GameID']

        boxScoreSummary = Req.get(URL.boxScoreSummary(gameID))

        homeTeam = game['HomeTeam']['teamName']
        awayTeam = game['VisitorTeam']['teamName']

        homeID = getTeamID(homeTeam)
        awayID = getTeamID(awayTeam)

        homeData = teamData[homeTeam]
        awayData = teamData[awayTeam]

        homeScore = boxScoreSummary['resultSets'][5]['rowSet'][0][22]
        awayScore = boxScoreSummary['resultSets'][5]['rowSet'][1][22]

        print('{} @ {} : {} v. {} Final'.format(awayTeam, homeTeam, homeScore, awayScore))

        xData = homeData + awayData

        if (homeScore > awayScore):
            yData = [1, 0]
        else:
            yData = [0, 1]

        IOUtils.appendTrainingData(xData, yData)

teamData = IOUtils.extractTeamDataFromFile()

boxScoreBreakdown("20161227", teamData)