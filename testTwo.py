import pandas as pd

rows = []

i = 0
while i < 10:
    tempList = []

    j = 0
    while j < 16:
        tempInput = input()
        tempList.append(tempInput)
        j += 1
    rows.append(tempList)
    i += 1

df = pd.DataFrame(rows, columns=[
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16'
])

df.to_csv('RoundOneResults.csv', index=False)