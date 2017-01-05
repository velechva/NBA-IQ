import json

def extractTeamDataFromFile():
    with open('../data/Teams.JSON') as infile:
        data = json.load(infile)

        return data

def saveTeamDataToFile(results):
    with open('../data/Teams.JSON', 'w') as outfile:
        print("Writing team data to file")

        json.dump(results, outfile)

def appendTrainingData(xdata, ydata):
    print('Appending Training data')

    with open('../data/TrainX.JSON', 'r') as xFile:
        xJSON = json.load(xFile)
        xJSON.append(xdata)

    with open('../data/TrainX.JSON', 'w') as xFile:
        json.dump(xJSON, xFile)

    with open('../data/TrainY.JSON', 'r') as yFile:
        yJSON = json.load(yFile)
        yJSON.append(ydata)

    with open('../data/TrainY.JSON', 'w') as yFile:
        json.dump(yJSON, yFile)

def appendTestingData(xdata, ydata):
    print('Appending Testing data')

    with open('../data/TestX.JSON', 'r') as xFile:
        xJSON = json.load(xFile)
        xJSON.append(xdata)

    with open('../data/TestX.JSON', 'w') as xFile:
        json.dump(xJSON, xFile)

    with open('../data/TestY.JSON', 'r') as yFile:
        yJSON = json.load(yFile)
        yJSON.append(ydata)

    with open('../data/TestY.JSON', 'w') as yFile:
        json.dump(yJSON, yFile)

def resetDataFiles():
    with open('../data/TrainX.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)

    with open('../data/TrainY.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)

    with open('../data/TestX.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)

    with open('../data/TestY.JSON', 'w') as file:
        obj = []
        json.dump(obj, file)

    print("IOUtils: Data Files reset")

def loadData():
    print('Loading Training data')

    with open('../data/TrainX.JSON') as xFile:
        trainX = json.load(xFile)

    with open('../data/TrainY.JSON') as yFile:
        trainY = json.load(yFile)

    with open('../data/TestX.JSON') as xFile2:
        testX = json.load(xFile2)

    with open('../data/TestY.JSON') as yFile2:
        testY = json.load(yFile2)

    return trainX, trainY, testX, testY