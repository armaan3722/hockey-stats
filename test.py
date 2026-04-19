import pandas as pd
from sklearn.model_selection import train_test_split

stats2025 = pd.read_csv('./data/stats/stats2025.csv')
playoffs2025 = pd.read_csv('./data/playoffs/playoffs2025.csv')

# Set up x and y for training
df = playoffs2025.merge(
    stats2025.add_prefix('H_'), 
    left_on='homeTeam', 
    right_on='H_teamAbbrev', 
    how='left'
)

df = df.merge(
    stats2025.add_prefix('A_'), 
    left_on='awayTeam', 
    right_on='A_teamAbbrev', 
    how='left'
)

df = df.drop(['homeTeam', 'awayTeam', 'H_teamAbbrev', 'A_teamAbbrev'], axis=1)

x = df.drop(['winner', 'games'], axis=1)
yWinner = df['winner']
yGames = df['games']