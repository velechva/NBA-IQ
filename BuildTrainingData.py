import pickle

import Req

# Season: NNNN-NN (eg. 1995-96)

teams = {
    "Atlanta Hawks": 1610612737,
    "Boston Celtics": 1610612738,
    "Brooklyn Nets": 1610612751,
    "Charlotte Hornets": 1610612766,
    "Chicago Bulls": 1610612741,
    "Cleveland Cavaliers": 1610612739,
    "Dallas Mavericks": 1610612742,
    "Denver Nuggets": 1610612743,
    "Detroit Pistons": 1610612765,
    "Golden State Warriors": 1610612744,
    "Houston Rockets": 1610612745,
    "Indiana Pacers": 1610612754,
    "Los Angeles Clippers": 1610612746,
    "Los Angeles Lakers": 1610612747,
    "Memphis Grizzlies": 1610612763,
    "Miami Heat": 1610612748,
    "Milwaukee Bucks": 1610612749,
    "Minnesota Timberwolves": 1610612750,
    "New Orleans Pelicans": 1610612740,
    "New York Knicks": 1610612752,
    "Oklahoma City Thunder": 1610612760,
    "Orlando Magic": 1610612753,
    "Philadelphia 76ers": 1610612755,
    "Phoenix Suns": 1610612756,
    "Portland Trail Blazers": 1610612757,
    "Sacramento Kings": 1610612758,
    "San Antonio Spurs": 1610612759,
    "Toronto Raptors": 1610612761,
    "Utah Jazz": 1610612762,
    "Washington Wizards": 1610612764
}

seasonType = {
    "Regular Season": "Regular+Season",
    "Pre Season": "Pre+Season",
    "Playoffs": "Playoffs",
    "All-Star": "All-Star",
    "All Star": "All+Star",
    "Preseason": "Preseason"
}

leagueID = 00

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

def test():
    shots_url = "http://states.nba.com/stats/..."

    response = Req.get(shots_url)
    response.raise_for_status()
    shots = response.json()['resultsSet'][0]['rowSet']

def getMatchData(home, away):
    homeID = getTeamID(home)
    awayID = getTeamID(away)

def getTeamID(name):
    return teams[name]

def teamData(teamID):
    result = ""

def teamInfoCommon(teamID, year, season):
    result = ""

    url = "http://stats.nba.com/stats/teaminfocommon?LeagueID=00&Season={}&SeasonType={}&TeamID={}".format(year, season, teamID)
    res = Req.get(url)

    parameters = res['parameters']
    for p in parameters:
        result += parameters[p]

    team_info_common = res['resultSets'][0]['rowSet'][0]
    for t in team_info_common:
        result += t

    team_season_ranks = res['resultSets'][1]['rowSet'][0]
    for t in team_season_ranks:
        result += t

def teamDashBoardByGeneralSplits(lastNGames, month, year, season, teamID):
    result = ""

    url = "http://stats.nba.com/stats/teamdashboardbygeneralsplits?DateFrom=&DateTo=&GameSegment=&LastNGames={}".format(lastNGames) \
        + "&LeagueID=00&Location=&MeasureType=Base&Month={}&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0".format(month) \
        + "&PlusMinus=N&Rank=N&Season={}&SeasonSegment=&SeasonType={}&ShotClockRange=&Split=general&TeamID={}&VsConference=&VsDivision=".format(year, season, teamID)

    res = Req.get(url)

    params = res['parameters']

    for p in params:
        result += params[p]