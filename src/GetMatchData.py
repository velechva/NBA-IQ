import pickle

import Req
import Constants

result = []

def test():
    shots_url = "http://states.nba.com/stats/..."

    response = Req.get(shots_url)
    response.raise_for_status()
    shots = response.json()['resultsSet'][0]['rowSet']


def matchData(home, away):
    homeID = getTeamID(home)
    awayID = getTeamID(away)

    teamData(homeID)
    teamData(awayID)

def getTeamID(name):
    return teams[name]

def teamData(teamID):
    for y in years:
        teamInfoCommon(teamID, y, seaonType["Pre Season"])
        teamInfoCommon(teamID, y, seasonType["Playoffs"])

        teamDashBoardByGeneralSplits(100, "", y)

def teamInfoCommon(teamID, year, season):
    url = "http://stats.nba.com/stats/teaminfocommon?LeagueID=00&Season={}&SeasonType={}&TeamID={}".format(year, season, teamID)
    res = Req.get(url)

    team_info_common = res['resultSets'][0]['rowSet'][0]
    for t in team_info_common[8:12]:
        result += t

    team_season_ranks = res['resultSets'][1]['rowSet'][0]
    for t in team_season_ranks[3:10]:
        result += t

def teamDashBoardByGeneralSplits(lastNGames, month, year, season, teamID):
    url = "http://stats.nba.com/stats/teamdashboardbygeneralsplits?DateFrom=&DateTo=&GameSegment=&LastNGames={}".format(lastNGames) \
        + "&LeagueID=00&Location=&MeasureType=Base&Month={}&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0".format(month) \
        + "&PlusMinus=N&Rank=N&Season={}&SeasonSegment=&SeasonType={}&ShotClockRange=&Split=general&TeamID={}&VsConference=&VsDivision=".format(year, season, teamID)

    res = Req.get(url)

    for i in range(0, 6):
        result_set = res['resultSets'][i]['rowSet']
        for t in result_set[2:56]:
            result += t

    overall

def commonTeamRoster(teamID):
    url = "http://stats.nba.com/stats/commonteamroster?LeagueID=00&Season=2016-17&TeamID={}".format(teamID)

    res = Req.get(url)

    commonTeamRoster = res['resultSets'][0]['rowSet']
    for p in commonTeamRoster:
        playerID = p[12]

        playerData(playerID)

    coaches = res['resultSets'][1]['rowSet']
    for c in coaches:
        result += c[2]

def playerData(playerID):
    