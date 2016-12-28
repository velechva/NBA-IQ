import json

from GetTeamData import getTeamData
from Constants import *

results = {}
for team in teamIdentifiers:
	print("Fetching data for: " + team)

	resultData = getTeamData(team)
	results[team] = resultData

with open('../Data/Teams.JSON', 'w') as outfile:
	print("Writing team data to file")
	
	json.dump(results, outfile)