# Import packages
import requests
import pandas as pd

# Season end dates
seasonEndDates = [
    '2026-04-17',
    '2025-04-17',
    '2024-04-18',
    '2023-04-14',
    '2022-05-01',
    '2019-04-06',
    '2018-04-08',
    '2017-04-09',
    '2016-04-10',
    '2015-04-11'
]

for j in seasonEndDates:
    # Set up url
    url = f"https://api-web.nhle.com/v1/standings/{j}"

    # Read API
    response = requests.get(url)
    data = response.json()

    # Convert to csv
    dataRows = []

    for i in data["standings"]:
        dataRows.append([
            i['teamAbbrev']['default'],
            i['conferenceHomeSequence'],
            i['conferenceL10Sequence'],
            i['conferenceRoadSequence'],
            i['conferenceSequence'],
            i['divisionHomeSequence'],
            i['divisionL10Sequence'],
            i['divisionRoadSequence'],
            i['divisionSequence'],
            i['gameTypeId'],
            i['goalDifferential'],
            i['goalFor'],
            i['goalAgainst'],
            i['homeGoalDifferential'],
            i['homeGoalsFor'],
            i['homeGoalsAgainst'],
            i['homeLosses'],
            i['homeOtLosses'],
            i['homePoints'],
            i['homeRegulationWins'],
            i['homeWins'],
            i['l10GamesPlayed'],
            i['l10GoalDifferential'],
            i['l10GoalsAgainst'],
            i['l10GoalsFor'],
            i['l10Losses'],
            i['l10OtLosses'],
            i['l10Points'],
            i['l10RegulationWins'],
            i['l10Wins'],
            i['leagueHomeSequence'],
            i['leagueL10Sequence'],
            i['leagueRoadSequence'],
            i['leagueSequence'],
            i['losses'],
            i['otLosses'],
            i['points'],
            i['regulationPlusOtWins'],
            i['regulationWins'],
            i['roadGoalDifferential'],
            i['roadGoalsFor'],
            i['roadGoalsAgainst'],
            i['roadLosses'],
            i['roadOtLosses'],
            i['roadPoints'],
            i['roadRegulationWins'],
            i['roadWins']
        ])

    df = pd.DataFrame(dataRows, columns=[
        'teamAbbrev',
        'conferenceHomeSequence',
        'conferenceL10Sequence',
        'conferenceRoadSequence',
        'conferenceSequence',
        'divisionHomeSequence',
        'divisionL10Sequence',
        'divisionRoadSequence',
        'divisionSequence',
        'gameTypeId',
        'goalDifferential',
        'goalFor',
        'goalAgainst',
        'homeGoalDifferential',
        'homeGoalsFor',
        'homeGoalsAgainst',
        'homeLosses',
        'homeOtLosses',
        'homePoints',
        'homeRegulationWins',
        'homeWins',
        'l10GamesPlayed',
        'l10GoalDifferential',
        'l10GoalsAgainst',
        'l10GoalsFor',
        'l10Losses',
        'l10OtLosses',
        'l10Points',
        'l10RegulationWins',
        'l10Wins',
        'leagueHomeSequence',
        'leagueL10Sequence',
        'leagueRoadSequence',
        'leagueSequence',
        'losses',
        'otLosses',
        'points',
        'regulationPlusOtWins',
        'regulationWins',
        'roadGoalDifferential',
        'roadGoalsFor',
        'roadGoalsAgainst',
        'roadLosses',
        'roadOtLosses',
        'roadPoints',
        'roadRegulationWins',
        'roadWins'
    ])

    df.to_csv(f'data{j[0]}{j[1]}{j[2]}{j[3]}.csv', index=False)