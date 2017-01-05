# NBA-IQ

## What It Does

This application uses NBA statistics from the stats.nba.com website, along with a tensorflow neural network, to try and
predict the outcome of games.

Software is in early development. Much more data needs to be analyzed and formatted in order to increase accuracy of the
network. Current accuracy is around 60-80%, depending on the training/testing data that is used.

## Usage

First, the basic data about each team needs to be fetched and stored:

```python
import BuildTeamDatabase

BuildTeamDatabase.buildTeamDatabase()
```

Second, the training and testing data needs to be fetched and stored:

```python
import BuildTrainingData

BuildTrainingData.buildTrainingData()
```

Then, the neural network can be run with:
```python
import NBAIQ

trainNet(x)
```