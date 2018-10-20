import random 

def playersInformation(): 
    newNames = {}
    playerNames = 0
    numberOfPlayers = int(input("Enter number of players: "))
    for i in range(numberOfPlayers): 
        player = input("Enter player's name: ")
        newNames[player] = {"Score" : 0, "Won": 0}
    playerNames = randomNames(newNames, numberOfPlayers)
    print("Playing in this order" + str(list(playerNames)))
    return playerNames
def randomNames(newNames, numberOfPlayers):
    playerNames = {}
    nameTrack = []
    counter = 0
    while counter < numberOfPlayers:
        new = random.choice(list(newNames))
        if new not in nameTrack:
            nameTrack.append(new)
            playerNames[new] = {"Score": 0, "Won":0}
        else: 
            if len(nameTrack) == 3: 
                break
            counter -= 1
    return playerNames
def colorGenerator(): 
    colors = "RGBYOP"
    randomColors = random.sample(colors, 4)
    randomColors = "".join(randomColors)
    return randomColors
 
def playAGame(playerNames, randomColors): 
    currentScore = 0
    afterScore = 0
    whiteScore = 1 
    blackScore = 5
    counter = 0
    scoreTracker = 0
    userTracker = 0
    firstRound = 0
    round = 0
    score = []
    overallWin = 0
    overallWinnerName = 0
    dictKeys = list(playerNames)
    while True:
        if score == ["B", "B", "B", "B"]:
            if firstRound == 0:
                userTracker["Won"] += 1
            elif counter != 0: 
                userTracker["Won"] += 1
            print("Correct Guess!")
            print(playerNames)
            print("Winner: " +winnerName + str(userTracker))
            if keepOnPlaying() == False:
                for i in range(len(playerNames)):
                    playerNames[list(playerNames)[i]]["Score"] = 0
                counter = 0
                randomColors = colorGenerator()
            else:
                for i in range(len(playerNames)):
                    if overallWin < playerNames[list(playerNames)[i]]["Won"]:
                        overallWin = playerNames[list(playerNames)[i]]["Won"]
                        overallWinnerName = list(playerNames)[i]
                print("Overall winner: "+ str(overallWinnerName))
                print("Program end")
                break
        score = []
        if (counter < len(playerNames)):
            userGuess = input(list(playerNames)[counter] + ", make a guess of 4 colors from RGBYOP: ").upper()
            currentPlayer = list(playerNames)[counter]
            currentScore = playerNames[currentPlayer]["Score"]
            
   
        for i in range(len(randomColors)): 
            if userGuess[i] == randomColors[i]: 
                playerNames[list(playerNames)[counter]]["Score"] += blackScore
                score.append("B")
            elif userGuess[i] in randomColors: 
                playerNames[list(playerNames)[counter]]["Score"] += whiteScore
                score.append("W")
        if scoreTracker < playerNames[currentPlayer]["Score"]:
            scoreTracker = playerNames[currentPlayer]["Score"]
            userTracker = playerNames[currentPlayer]
            winnerName = currentPlayer
        afterScore = playerNames[list(playerNames)[counter]]["Score"]
        counter += 1
        if counter == len(playerNames): 
                userTracker["Won"] += 1
                round += 1
                firstRound += 1 
                counter = 0
        print("".join(score))   
        print("Current player:    " + currentPlayer + " current score:  " + str(currentScore))
        print("Current player:    " + currentPlayer + " updated score:  " + str(afterScore))
        
  
def keepOnPlaying():
    keepPlaying = input("\n" + "<Enter> to play and any letter to stop: ")
    if keepPlaying == "":
        return False
    else: 
        return True
def main(): 
    playerNames = playersInformation()
    randomColors = colorGenerator()
    playAGame(playerNames, randomColors)
main()
