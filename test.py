import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, accuracy_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import RandomForestClassifier
import joblib

traingingYears = [
    '2025',
    '2024',
    '2023',
    '2022',
    '2019',
    '2018',
    '2017',
    '2016',
    '2015'
]

df = pd.DataFrame()

for i in traingingYears:
    stats = pd.read_csv(f'./data/stats/stats{i}.csv')
    playoffs = pd.read_csv(f'./data/playoffs/playoffs{i}.csv')

    # Set up x and y for training
    tempDF = playoffs.merge(
        stats.add_prefix('H_'), 
        left_on='homeTeam', 
        right_on='H_teamAbbrev', 
        how='left'
    )

    tempDF = tempDF.merge(
        stats.add_prefix('A_'), 
        left_on='awayTeam', 
        right_on='A_teamAbbrev', 
        how='left'
    )

    tempDF = tempDF.drop(['homeTeam', 'awayTeam', 'H_teamAbbrev', 'A_teamAbbrev'], axis=1)
    df = pd.concat([df, tempDF], ignore_index=True)

x = df.drop(['winner', 'games'], axis=1)
yWinner = df['winner']
yGames = df['games']

poly = PolynomialFeatures()
polyX = poly.fit_transform(x)

def winnerModelTrain():
    # Prepare to start training
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        yWinner,
        test_size=0.2,
        random_state=42
    )

    # Train
    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=5,
        min_samples_split=2,
        min_samples_leaf=3,
        max_leaf_nodes=5,
        random_state=42,
        n_jobs=-1
    )
    model.fit(x_train, y_train)

    yPred = model.predict(x_test)
    accuracy = accuracy_score(y_test, yPred)
    print(accuracy)

def winnerModelFinal():
    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=5,
        min_samples_split=2,
        min_samples_leaf=3,
        max_leaf_nodes=5,
        random_state=42,
        n_jobs=-1
    )

    model.fit(x, yWinner)
    joblib.dump(model, './models/winner_model_1.joblib')

def gamesModelTrain():
    # Prepare to start training
    x_train, x_test, y_train, y_test = train_test_split(
        polyX,
        yGames,
        test_size=0.2,
        random_state=42
    )

    # Train
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=6,
        min_samples_split=2,
        min_samples_leaf=1,
        max_leaf_nodes=None,
        random_state=42,
        n_jobs=-1
    )
    model.fit(x_train, y_train)

    yPred = model.predict(x_test)
    accuracy = accuracy_score(y_test, yPred)
    print(accuracy)

def gamesModelFinal():
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=6,
        min_samples_split=2,
        min_samples_leaf=1,
        max_leaf_nodes=None,
        random_state=42,
        n_jobs=-1
    )

    model.fit(x, yGames)
    joblib.dump(model, './models/games_model_1.joblib')

def makePrediction():
    # Load models
    winnerModel = joblib.load('./models/winner_model_1.joblib')
    gamesModel = joblib.load('./models/games_model_1.joblib')

    print('Enter home team')
    homeTeam = input()
    print('Enter away team')
    awayTeam = input()

    # Get data
    stats = pd.read_csv('./data/stats/stats2026.csv')

    x = pd.concat(
        [
            stats[stats['teamAbbrev'] == homeTeam].add_prefix('H_').reset_index(drop=True), 
            stats[stats['teamAbbrev'] == awayTeam].add_prefix('A_').reset_index(drop=True)
        ], 
        axis=1
    )

    x = x.drop(['H_teamAbbrev', 'A_teamAbbrev'], axis=1)

    # Make prediction
    winnerPred = winnerModel.predict(x)
    gamesPred = gamesModel.predict(x)

    print(winnerPred)
    print(gamesPred)

winnerModelTrain()
gamesModelTrain()
winnerModelFinal()
gamesModelFinal()

i = 0
while i < 15:
    makePrediction()
    i += 1