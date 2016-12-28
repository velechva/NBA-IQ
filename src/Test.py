import Req
from Constants import *

import json

with open('../Data/Teams.JSON') as infile:
    data = json.load(infile)

    print(data["Toronto Raptors"])