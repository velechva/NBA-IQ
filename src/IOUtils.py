import json

def extractTeamDataFromFile():
    with open('../Data/Teams.JSON') as infile:
        data = json.load(infile)

        return data

def saveTeamDataToFile(results):
    with open('../Data/Teams.JSON', 'w') as outfile:
        print("Writing team data to file")

        json.dump(results, outfile)

def appendTrainingData(xData, yData):
    print('Appending Training Data')

    with open('../Data/TrainX.JSON', 'r') as xFile:
        xJSON = json.load(xFile)
        xJSON.append(xData)

    with open('../Data/TrainX.JSON', 'w') as xFile:
        json.dump(xJSON, xFile)

    with open('../Data/TrainY.JSON', 'r') as yFile:
        yJSON = json.load(yFile)
        yJSON.append(yData)

    with open('../Data/TrainY.JSON', 'w') as yFile:
        json.dump(yJSON, yFile)

def resetDataFiles():
    with open('../Data/TrainX.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)

    with open('../Data/TrainY.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)