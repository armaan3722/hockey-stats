import pandas as pd
from sklearn.model_selection import train_test_split

data2025 = pd.read_csv('data2025.csv')
dataWithoutNames = data2025.drop('teamAbbrev', axis=1)

print(data2025)
print(dataWithoutNames)

# Set up x and y for training
x = dataWithoutNames