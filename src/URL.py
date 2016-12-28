import json

with open('../data/endpoints.JSON') as infile: 
    URLs = json.load(infile)

def teamInfoCommon(teamID, year, season):
	return URLs['teamInfoCommon'].format(year, season, teamID)

def teamDashBoardByGeneralSplits(lastNGames, month, year, season, teamID):
	return URLs['teamDashBoardByGeneralSplits'].format(lastNGames, month, year, season, teamID)

def commonTeamRoster(teamID):
	return URLs['commonTeamRoster'].format(teamID)

def playerData(playerID, year, season):
	return URLs['playerData'].format(playerID, year, season)

def boxScoreBreakdown(date):
    return URLs['boxScoreBreakdown'].format(date)

def boxScoreSummary(gameID):
    return URLs['boxScoreSummary'].format(gameID)