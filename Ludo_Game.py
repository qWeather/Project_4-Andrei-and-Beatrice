from random import randint

class player:
    def __init__(self, playerID):
        if playerID == 1:
            #blue - player 1
            self.startCol = "\033[1;94m" # prefix for colour
            self.endCol = "\033[0m"  # postfix for colour
            self.playerID = playerID  # player ID
            self.startingPos = [2, 0]  # starting position for player
            self.coin1Pos = [2, 0]  # first coin position
            self.coin2Pos = [2, 0]  # second coin position
            self.coin3Pos = [2, 0]  # third coin position
            self.coin4Pos = [2, 0]  # fourth coin position
            self.limit = [1, 0]  # limit before entering inner square
            self.innerLimit = [2, 1]  # limit before winning inside inner square
            self.hasWon = False
            self.coinDirections = {1: "d", 2: "d", 3: "d", 4: "d"}  # dictionary for coin direction of movement
        if playerID == 2:
            #green - player 2
            self.startCol = "\033[1;92m" # prefix for colour
            self.endCol = "\033[0m"  # postfix for colour
            self.playerID = playerID  # player ID
            self.startingPos = [4, 2]  # starting position for player
            self.coin1Pos = [4, 2]  # first coin position
            self.coin2Pos = [4, 2]  # second coin position
            self.coin3Pos = [4, 2]  # third coin position
            self.coin4Pos = [4, 2]  # fourth coin position
            self.limit = [4, 1]  # limit before entering inner square
            self.innerLimit = [3, 2]  # limit before winning inside inner square
            self.hasWon = False
            self.coinDirections = {1: "r", 2: "r", 3: "r", 4: "r"}  # dictionary for coin direction of movement
        if playerID == 3:            
            #yellow - player 3
            self.startCol = "\033[1;93m" # prefix for colour
            self.endCol = "\033[0m"  # postfix for colour
            self.playerID = playerID  # player ID
            self.startingPos = [2, 4]  # starting position for player
            self.coin1Pos = [2, 4]  # first coin position
            self.coin2Pos = [2, 4]  # second coin position
            self.coin3Pos = [2, 4]  # third coin position
            self.coin4Pos = [2, 4]  # fourth coin position
            self.limit = [3, 4]  # limit before entering inner square
            self.innerLimit = [2, 3]  # limit before winning inside inner square
            self.hasWon = False
            self.coinDirections = {1: "u", 2: "u", 3: "u", 4: "u"}  # dictionary for coin direction of movement

        if playerID == 4:
            #pink - player 4
            self.startCol = "\033[1;95m" # prefix for colour
            self.endCol = "\033[0m"  # postfix for colour
            self.playerID = playerID  # player ID
            self.startingPos = [0, 2]  # starting position for player
            self.coin1Pos = [0, 2]  # first coin position
            self.coin2Pos = [0, 2]  # second coin position
            self.coin3Pos = [0, 2]  # third coin position
            self.coin4Pos = [0, 2]  # fourth coin position
            self.limit = [0, 3]  # limit before entering inner square
            self.innerLimit = [1, 2]  # limit before winning inside inner square
            self.hasWon = False
            self.coinDirections = {1: "l", 2: "l", 3: "l", 4: "l"}  # dictionary for coin direction of movement

        self.killCount = 0  # counter for kills
        self.coins = [self.coin1Pos, self.coin2Pos, self.coin3Pos, self.coin4Pos]  # list of coins positions

#  function to display and update board
def displayBoard(currentPlayer, board, firstIter = False):
    for x in range(5):
        for y in range(5):

            for player in players:
                counter = 0
                for coin in player.coins:
                    if coin == [x, y]:
                        colourPrefix = player.startCol
                        colourPostfix = player.endCol
                        playerID = player.playerID
                        counter += 1
                if firstIter:
                    if counter != 0:
                        if board[x][y] == "-":
                            board[x][y] = [playerID, counter]
                        else:
                            board[x][y] += [playerID, counter]

            if board[x][y] != "-" and board[x][y] != "X":
                toPrint = []
                for j in range(0, len(board[x][y]), 2):
                    playerID = board[x][y][j]
                    counter = board[x][y][j+1]
                    printedPlayer = eval(f"player{playerID}")
                    colourPrefix = printedPlayer.startCol
                    colourPostfix = printedPlayer.endCol
                    if not firstIter:
                        toPrint.append((colourPrefix + str(counter) + colourPostfix))
                for item in toPrint:
                    print(item, end='')
                print("\t", end='')
            elif x == 2 and y == 2:
                board[x][y] = "X"
                if not firstIter:
                    print("\033[1;91mX\033[0m", end="\t")
            else:
                board[x][y] = "-"
                if not firstIter:
                    print("-", end="\t")

        print("\n")

#  function for movement, killing and game rules
def movePiece(player, coinPos, coinIx, moves):
    killed = False
    coinIx = int(coinIx) + 1
    originalPos = coinPos.copy()
    for x in range(0, len(board[coinPos[0]][coinPos[1]]), 2):
        # if old space had multiple players
        if board[coinPos[0]][coinPos[1]][x] == player.playerID and len(board[coinPos[0]][coinPos[1]]) > 2:
            if board[coinPos[0]][coinPos[1]][x+1] > 1:
                board[coinPos[0]][coinPos[1]][x+1] -= 1
            else:
                del board[coinPos[0]][coinPos[1]][x]
                del board[coinPos[0]][coinPos[1]][x]
        elif board[coinPos[0]][coinPos[1]][x] == player.playerID:
            if board[coinPos[0]][coinPos[1]][x+1] > 1:
                board[coinPos[0]][coinPos[1]][x+1] -= 1
            else:
                if coinPos != player.startingPos:
                    board[coinPos[0]][coinPos[1]] = "-"
                else:
                    board[coinPos[0]][coinPos[1]][x+1] = "-"
        elif len(board[coinPos[0]][coinPos[1]]) == 2:
            if coinPos != player.startingPos:
                board[coinPos[0]][coinPos[1]] = "-"

        if len(board[coinPos[0]][coinPos[1]]) >= 2 and board[coinPos[0]][coinPos[1]] not in safeSpots:
            if coinPos != player.startingPos and board[coinPos[0]][coinPos[1]][x+1] == 0:
                board[coinPos[0]][coinPos[1]] = "-"

    for x in range(moves):
        if coinPos == player.limit and player.killCount < 1:
            coinPos = originalPos
            print("\033[1;97m\nPlayer doesn't have enough kills!\033[0m\n")
            break
        
        elif coinPos == player.limit:
            player.coinDirections[coinIx] = rotate[player.coinDirections[coinIx]]
            
        elif coinPos == player.innerLimit:
            player.coinDirections[coinIx] = rotate[player.coinDirections[coinIx]]
            player.hasWon = True
            ranking.append(player.playerID)
            # coinPos = [2, 2]
            if len(ranking) == 3 and player.playerID not in ranking:
                ranking.append(player.playerID)
            print(f"\033[1;97m\nPlayer {player.playerID} has won!\033[0m\n")
            
        exec(directions[player.coinDirections[coinIx]])
        for direction, pos in outerCorners.items():
            if coinPos == pos:
                player.coinDirections[coinIx] = direction
        if player.killCount >= 1:
            
            for direction, pos in innerCorners.items():
                if coinPos == pos:
                    player.coinDirections[coinIx] = direction

    if coinPos in safeSpots:
        found = False
        for x in range(0, len(board[coinPos[0]][coinPos[1]]), 2):
            if board[coinPos[0]][coinPos[1]][x] == player.playerID:
                found = True
                ix = x

        if found:
            if board[coinPos[0]][coinPos[1]][ix+1] > 0:
                board[coinPos[0]][coinPos[1]][ix+1] += 1
        else:
            board[coinPos[0]][coinPos[1]] += [player.playerID, 1]
        
    else:
        enemyPlayer = board[coinPos[0]][coinPos[1]][0]
        if str(enemyPlayer) not in "-X" and player.playerID != enemyPlayer:
            enemyPlayer = eval(f"player{enemyPlayer}")
            for x in range(len(enemyPlayer.coins)):
                if coinPos == enemyPlayer.coins[x]:
                    enemyPlayer.coins[x] = enemyPlayer.startingPos
                    board[coinPos[0]][coinPos[1]] = [player.playerID, 1]
                    board[enemyPlayer.startingPos[0]][enemyPlayer.startingPos[1]][1] += 1
                    player.killCount += 1
                    killed = True
                    print(f"{player.startCol}Kill count: {player.killCount}{player.endCol}")
        elif enemyPlayer == "-":
            for x in range(0, len(board[coinPos[0]][coinPos[1]]), 2):
                if board[coinPos[0]][coinPos[1]][x] == player.playerID:
                    if board[coinPos[0]][coinPos[1]][x+1] > 1:
                        board[coinPos[0]][coinPos[1]][x+1] += 1
                else:
                    board[coinPos[0]][coinPos[1]] = [player.playerID, 1]
        elif player.playerID == enemyPlayer:
            board[coinPos[0]][coinPos[1]][x+1] += 1

    return killed
    

#  initializing objects of each player
player1 = player(1)
player2 = player(2)
player3 = player(3)
player4 = player(4)
players = [player1, player2, player3, player4]  # list of players

board = [["-" for x in range(5)] for y in range(5)]  # initializing empty board
directions = {"d": "coinPos[0] += 1", "r": "coinPos[1] += 1", "u": "coinPos[0] -= 1", "l": "coinPos[1] -= 1"}  # dictionary of coin directions
outerCorners = {"u": [4, 4], "l": [0, 4], "d": [0, 0], "r": [4, 0]}  # dictionary of outer corners coordinates
innerCorners = {"u": [3, 1], "l": [3, 3], "d": [1, 3], "r": [1, 1]}  # dictionary of inner corners coordinates
rotate = {"u": "l", "l": "d", "d": "r", "r": "u"}
safeSpots = [[2, 0], [0, 2], [2, 4], [4, 2]]  # list of safe spots coordinates
ranking = []  # list for ranking the players

playerIx = 0  # variable for keeping track of the current player
currentPlayer = players[playerIx]  # current player
displayBoard(currentPlayer, board, True)  # display board
while True:
    currentPlayer = players[playerIx]  # update player's turn
    displayBoard(currentPlayer, board)  # display and update board each time
    print(f"\n{currentPlayer.startCol}It is Player {currentPlayer.playerID}'s turn!{currentPlayer.endCol}\n")
    input("\033[1;96mPress Enter to roll dice...\033[0m")
    moves = int(input("How many places to move?"))
    # moves = randint(1, 4)  # random dice value
    print(f"\033[1;97m\nMoving {moves} spaces!\033[0m\n")

    for x in range(len(currentPlayer.coins)):  # choosing available coins to move
        print(f"\033[1;97m\n{x+1}. Move the coin found currently at {currentPlayer.coins[x]}\033[0m\n")
    coinChoice = int(input(f"\n{currentPlayer.startCol}Which coin would you like to move: {currentPlayer.endCol}"))  # user coin choice
    coinChoice -= 1  # 
    killed = movePiece(currentPlayer, currentPlayer.coins[coinChoice], coinChoice, moves)  # check if coin was killed

    if not killed and not (moves == 4):  #  coin wasn't killed or didn't roll 4
        playerIx += 1
    elif killed:  # coin is killed --> deadly (roll again)
        print("\033[1;91m\nDeadly!\033[0m\n")
    elif moves == 4:  # rolled aa 4 --> supershot (roll again)
        print("\033[1;97m\nSuper Shot!\033[0m\n")
    
    if playerIx == 4 and len(ranking) < 1 and not currentPlayer.hasWon:  # reset player turn after an entire round
        playerIx = 0
    elif playerIx == 4 and len(ranking) >=1 and currentPlayer.hasWon:
        print(f"Player {currentPlayer} has already won!")
    elif playerIx == 4 and len(ranking) >=2 and currentPlayer.hasWon:
        print(f"Player {currentPlayer} has already won!")
    elif len(ranking) == 3:  # check 3 players have won and display ranking
    
        rank_place = 0  # variable to track ranking
        for p in ranking:  # print ranking
            if len(ranking):  # display players in order of winning
                print("\033[1;92m\nRANKING\033[0m\n")
                print(f"\033[1;92m\n{rank_place + 1}. Player {p}\033[0m\n")
                rank_place += 1
            else:
                print("\033[1;97m\nGame's still on!\033[0m\n")
        break
        
