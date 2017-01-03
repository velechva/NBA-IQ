import json

from GetTeamData import getTeamData
from Constants import *
import IOUtils

results = {}
for team in teamIdentifiers:
    print("Fetching data for: " + team)

    resultData = getTeamData(team)
    results[team] = resultData

IOUtils.saveTeamDataToFile(results)