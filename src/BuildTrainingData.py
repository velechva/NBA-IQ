import Req
import URL
import IOUtils
from Constants import *

import json

def boxScoreBreakdown(date, teamData, option):
    print("Analyzing Data for: " + date)

    boxScore = Req.get(URL.boxScoreBreakdown(str(date)))

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

        if (option == 'training'):
            IOUtils.appendTrainingData(xData, yData)
        if (option == 'testing'):
            IOUtils.appendTestingData(xData, yData)

def loadScoreDataByMonth(year, month, option):
    dates = []

    for i in range(1, 28):
        if i < 10:
            date = "0" + str(i)
        else:
            date = str(i)

        dates.append(str(year + month + date))

    for date in dates:
        boxScoreBreakdown(date, teamData, option)

teamData = IOUtils.extractTeamDataFromFile()

loadScoreDataByMonth('2016', '11', 'training')
loadScoreDataByMonth('2016', '12', 'testing')