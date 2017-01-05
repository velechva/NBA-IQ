import Req
import URL
from Constants import *

def getTeamData(teamName):
    print("Getting data for: " + teamName)

    stats = []

    teamID = getTeamID(teamName)
    teamData(stats, teamID)

    return stats

def teamData(stats, teamID):
    for y in years:
        teamPlayerDashboard(stats, y, seasonType["Regular Season"], teamID)


def teamPlayerDashboard(stats, year, season, teamID):
    url = URL.teamPlayerDashboard(year, season, teamID)
    res = Req.get(url)

    # Overall stats for team
    overall = res['resultSets'][0]['rowSet'][0]
    for i in range(4, 55):
        stats.append(overall[i])

    playerStats = res['resultSets'][1]['rowSet']
    # For each player stat type
    for i in range(3, 58):
        # Calculate the average over the team and append it
        sum = 0

        for j in range(0, 13):
            sum += playerStats[j][i]

        append(stats, sum / 15)

def append(data, o):
    if type(o) is int or type(o) is float:
        data.append(o)