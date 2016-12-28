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

def appendTestingData(xData, yData):
    print('Appending Testing Data')

    with open('../Data/TestX.JSON', 'r') as xFile:
        xJSON = json.load(xFile)
        xJSON.append(xData)

    with open('../Data/TestX.JSON', 'w') as xFile:
        json.dump(xJSON, xFile)

    with open('../Data/TestY.JSON', 'r') as yFile:
        yJSON = json.load(yFile)
        yJSON.append(yData)

    with open('../Data/TestY.JSON', 'w') as yFile:
        json.dump(yJSON, yFile)

def resetDataFiles():
    with open('../Data/TrainX.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)

    with open('../Data/TrainY.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)

    with open('../Data/TestX.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)

    with open('../Data/TestY.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)

def loadData():
    print('Loading Training Data')

    with open('../Data/TrainX.JSON') as xFile:
        trainX = json.load(xFile)

    with open('../Data/TrainY.JSON') as yFile:
        trainY = json.load(yFile)

    with open('../Data/TestX.JSON') as xFile2:
        testX = json.load(xFile2)

    with open('../Data/TestY.JSON') as yFile2:
        testY = json.load(yFile2)

    return trainX, trainY, testX, testY