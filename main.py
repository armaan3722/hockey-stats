#import libraries
import random
import math

#set starting variables

#[shots per game, goals against per game, shots against per game, team]
teams = [
    [28.2, 2.32, 27.2, "WPG"],
    [26.7, 2.82, 27.3, "STL"],
    [28.4, 2.71, 29.0, "DAL"],
    [29.9, 2.82, 25.9, "COL"],
    [30.3, 2.61, 26.1, "VGK"],
    [27.6, 2.88, 29.6, "MIN"],
    [28.1, 2.48, 25.5, "LAK"],
    [32.0, 2.87, 27.0, "EDM"],
    [28.0, 2.79, 29.3, "TOR"],
    [29.3, 2.83, 28.6, "OTT"],
    [28.5, 2.63, 28.2, "TBL"],
    [31.6, 2.72, 26.2, "FLA"],
    [27.6, 2.79, 27.2, "WSH"],
    [25.6, 3.18, 29.0, "MTL"],
    [31.7, 2.80, 24.9, "CAR"],
    [28.1, 2.68, 26.4, "NJD"]
]

#[shots per game, save percentage, team name]
secondRound = [
    [0, 0, ""],
    [0, 0, ""],
    [0, 0, ""],
    [0, 0, ""],
    [0, 0, ""],
    [0, 0, ""],
    [0, 0, ""],
    [0, 0, ""]
]

#[shots per game, save percentage, team name]
thirdRound = [
    [0, 0, ""],
    [0, 0, ""],
    [0, 0, ""],
    [0, 0, ""]
]

#[shots per game, save percentage, team name]
fourthRound = [
    [0, 0, ""],
    [0, 0, ""]
]

#[first team, simulations won, second team, simulations won]
games = [
    ["", 0, "", 0, 0],
    ["", 0, "", 0, 0],
    ["", 0, "", 0, 0],
    ["", 0, "", 0, 0],
    ["", 0, "", 0, 0],
    ["", 0, "", 0, 0],
    ["", 0, "", 0, 0],
    ["", 0, "", 0, 0],
    ["", 0, "", 0],
    ["", 0, "", 0],
    ["", 0, "", 0],
    ["", 0, "", 0],
    ["", 0, "", 0],
    ["", 0, "", 0],
    ["", 0, "", 0]
]

goalsA = 0
goalsB = 0
gamesA = 0
gamesB = 0
winsA = 0
winsB = 0
totalGames = 0
totalGoals = 0

teamOneShots = 0
teamOneSavePercent = 0
teamOneName = ""

teamTwoShots = 0
teamTwoSavePercent = 0
teamTwoName = ""

i = 0
j = 0
k = 0

totalSimulations = 100000
simulationsRun = 0

round = 1
teamsInRound = 16

while round < 5:
    #simulate round
    while (k * 2) < teamsInRound:
        #set team one and two stats
        if round == 1:
            teamOneShots = math.floor(teams[k * 2][0])
            teamOneSavePercent = 1000 * (1 - (teams[(k * 2)][1] / teams[(k * 2)][2]))
            teamOneName = teams[k * 2][3]

            teamTwoShots = math.floor(teams[k*2 + 1][0])
            teamTwoSavePercent = 1000 * (1 - (teams[(k*2 + 1)][1] / teams[(k*2 + 1)][2]))
            teamTwoName = teams[k*2 + 1][3]

        elif round == 2:
            teamOneShots = secondRound[k*2][0]
            teamOneSavePercent = secondRound[k*2][1]
            teamOneName = secondRound[k*2][2]

            teamTwoShots = secondRound[k*2 + 1][0]
            teamTwoSavePercent = secondRound[k*2 + 1][1]
            teamTwoName = secondRound[k*2 + 1][2]

        elif round == 3:
            teamOneShots = thirdRound[k*2][0]
            teamOneSavePercent = thirdRound[k*2][1]
            teamOneName = thirdRound[k*2][2]

            teamTwoShots = thirdRound[k*2 + 1][0]
            teamTwoSavePercent = thirdRound[k*2 + 1][1]
            teamTwoName = thirdRound[k*2 + 1][2]

        elif round == 4:
            teamOneShots = fourthRound[k*2][0]
            teamOneSavePercent = fourthRound[k*2][1]
            teamOneName = fourthRound[k*2][2]

            teamTwoShots = fourthRound[k*2 + 1][0]
            teamTwoSavePercent = fourthRound[k*2 + 1][1]
            teamTwoName = fourthRound[k*2 + 1][2]

        #repeat series simulation
        while j < totalSimulations:
            #simulate series
            while gamesA < 4 and gamesB < 4:
                #simulate game

                #check team a goals
                while i < teamOneShots:
                    if random.randint(1, 1000) > teamTwoSavePercent:
                        goalsA += 1
                    i += 1
                
                #reset i
                i = 0

                #check team b goals
                while i < teamTwoShots:
                    if random.randint(1, 1000) > teamOneSavePercent:
                        goalsB += 1
                    i += 1

                #reset i
                i = 0

                #check winner
                if goalsA >= goalsB:
                    gamesA += 1
                else:
                    gamesB += 1

                #count goals
                if round == 4:
                    totalGoals += goalsA
                    totalGoals += goalsB

                #reset variables
                goalsA = 0
                goalsB = 0

            #check series winner
            if gamesA > gamesB:
                winsA += 1
            elif gamesB > gamesA:
                winsB += 1
            
            #add games total
            if round == 1:
                totalGames += gamesA
                totalGames += gamesB

            #set and reset variables
            gamesA = 0
            gamesB = 0
            j += 1
            simulationsRun += 1

            #print current progress
            print(simulationsRun)
        
        #reset j
        j = 0

        #save simulation record
        if round == 1:
            games[k][0] = teamOneName
            games[k][1] = winsA
            games[k][2] = teamTwoName
            games[k][3] = winsB
            games[k][4] = (totalGames / totalSimulations)

        elif round == 2:
            games[k + 8][0] = teamOneName
            games[k + 8][1] = winsA
            games[k + 8][2] = teamTwoName
            games[k + 8][3] = winsB

        elif round == 3:
            games[k + 12][0] = teamOneName
            games[k + 12][1] = winsA
            games[k + 12][2] = teamTwoName
            games[k + 12][3] = winsB

        elif round == 4:
            games[k + 14][0] = teamOneName
            games[k + 14][1] = winsA
            games[k + 14][2] = teamTwoName
            games[k + 14][3] = winsB
        
        #track winner
        if winsA > winsB:
            if round == 1:
                secondRound[k][0] = teamOneShots
                secondRound[k][1] = teamOneSavePercent
                secondRound[k][2] = teamOneName
            elif round == 2:
                thirdRound[k][0] = teamOneShots
                thirdRound[k][1] = teamOneSavePercent
                thirdRound[k][2] = teamOneName
            elif round == 3:
                fourthRound[k][0] = teamOneShots
                fourthRound[k][1] = teamOneSavePercent
                fourthRound[k][2] = teamOneName
        else:
            if round == 1:
                secondRound[k][0] = teamTwoShots
                secondRound[k][1] = teamTwoSavePercent
                secondRound[k][2] = teamTwoName
            elif round == 2:
                thirdRound[k][0] = teamTwoShots
                thirdRound[k][1] = teamTwoSavePercent
                thirdRound[k][2] = teamTwoName
            elif round == 3:
                fourthRound[k][0] = teamTwoShots
                fourthRound[k][1] = teamTwoSavePercent
                fourthRound[k][2] = teamTwoName

        #set and reset variables
        winsA = 0
        winsB = 0
        totalGames = 0
        k += 1

    #set and reset variables
    k = 0
    round += 1

    #set games in round
    if round == 2:
        teamsInRound = 8
    elif round == 3:
        teamsInRound = 4
    elif round == 4:
        teamsInRound = 2

#print results
print("")
print("")
print("")

print("First round")
print("")

print("Series 1")
print(games[0][0])
print(games[0][1])
print(games[0][2])
print(games[0][3])
print(games[0][4])
print("")

print("Series 2")
print(games[1][0])
print(games[1][1])
print(games[1][2])
print(games[1][3])
print(games[1][4])
print("")

print("Series 3")
print(games[2][0])
print(games[2][1])
print(games[2][2])
print(games[2][3])
print(games[2][4])
print("")

print("Series 4")
print(games[3][0])
print(games[3][1])
print(games[3][2])
print(games[3][3])
print(games[3][4])
print("")

print("Series 5")
print(games[4][0])
print(games[4][1])
print(games[4][2])
print(games[4][3])
print(games[4][4])
print("")

print("Series 6")
print(games[5][0])
print(games[5][1])
print(games[5][2])
print(games[5][3])
print(games[5][4])
print("")

print("Series 7")
print(games[6][0])
print(games[6][1])
print(games[6][2])
print(games[6][3])
print(games[6][4])
print("")

print("Series 8")
print(games[7][0])
print(games[7][1])
print(games[7][2])
print(games[7][3])
print(games[7][4])
print("")
print("")

print("Second round")
print("")

print("Series 1")
print(games[8][0])
print(games[8][1])
print(games[8][2])
print(games[8][3])
print("")

print("Series 2")
print(games[9][0])
print(games[9][1])
print(games[9][2])
print(games[9][3])
print("")

print("Series 3")
print(games[10][0])
print(games[10][1])
print(games[10][2])
print(games[10][3])
print("")

print("Series 4")
print(games[11][0])
print(games[11][1])
print(games[11][2])
print(games[11][3])
print("")
print("")

print("Semi final")
print("")

print("Series 1")
print(games[12][0])
print(games[12][1])
print(games[12][2])
print(games[12][3])
print("")

print("Series 2")
print(games[13][0])
print(games[13][1])
print(games[13][2])
print(games[13][3])
print("")
print("")

print("Final")
print(games[14][0])
print(games[14][1])
print(games[14][2])
print(games[14][3])
print(totalGoals / totalSimulations)