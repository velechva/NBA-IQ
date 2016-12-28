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
        teamInfoCommon(stats, teamID, y, seasonType["Pre Season"])
        teamDashBoardByGeneralSplits(stats, 100, "", y, seasonType["Pre Season"], teamID)
        commonTeamRoster(stats, teamID)

def teamData(stats, teamID):
    for y in years:
        teamInfoCommon(stats, teamID, y, seasonType["Pre Season"])

def teamInfoCommon(stats, teamID, year, season):
    url = URL.teamInfoCommon(teamID, year, season)
    res = Req.get(url)

    team_info_common = res['resultSets'][0]['rowSet'][0]
    for t in team_info_common[8:12]:
        append(stats, t)

    team_season_ranks = res['resultSets'][1]['rowSet'][0]
    for t in team_season_ranks[3:10]:
        append(stats, t)

def teamDashBoardByGeneralSplits(stats, lastNGames, month, year, season, teamID):
    url = URL.teamDashBoardByGeneralSplits(lastNGames, month, year, season, teamID)

    res = Req.get(url)

    for i in range(0, 6):
        result_set = res['resultSets'][i]['rowSet']
        for t in result_set[2:56]:
            append(stats, t)

def commonTeamRoster(stats, teamID):
    url = URL.commonTeamRoster(teamID)

    res = Req.get(url)

    commonTeamRoster = res['resultSets'][0]['rowSet']
    for p in commonTeamRoster:
        playerID = p[12]

        playerData(stats, playerID, "2016-17", "Pre+Season")

    coaches = res['resultSets'][1]['rowSet']
    for c in coaches:
        stats.append(stats, c[2])

def playerData(stats, playerID, year, season):
    url = URL.playerData(playerID, year, season)

    res = Req.get(url)

    overallPlayerDashBoard = res['resultSets'][1]['rowSet'][0]
    for t in overallPlayerDashBoard[2:62]:
        append(stats, t)
        
def append(data, o):
    if type(o) is int or type(o) is float:
        data.append(o)