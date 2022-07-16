# Card Buster assignment
# Geetha Karthikesan

def haveSameNumberOfCards(list1, list2):
    list1Size = len(list1)
    list2Size = len(list2)
    return list1Size == list2Size

def printFinalOutcome(numberOfWinsForPlayer1, numberOfWinsForPlayer2, numberOfTies):
    winningMessageFinal = "Player {} wins the game, by {} wins to {}"
    drawMessageFinal = "The game ended in a draw of {} rounds"
    
    if (numberOfWinsForPlayer1 > numberOfWinsForPlayer2):
        print(winningMessageFinal.format(1, numberOfWinsForPlayer1, numberOfWinsForPlayer2))
    elif (numberOfWinsForPlayer2 > numberOfWinsForPlayer1):
        print(winningMessageFinal.format(2, numberOfWinsForPlayer2, numberOfWinsForPlayer1))
    else:
        print(drawMessageFinal.format(numberOfTies))

# Card Buster starts

player1Cards = [10,6,8,9,7,12,7]
player2Cards = [7,6,9,5,2,8,11]


# check both have the same number of cards
if (haveSameNumberOfCards(player1Cards, player2Cards)):
    print("Game on...")
    
    player1WinCount = 0
    player2WinCount = 0
    numberOfTies = 0
    
    # print message
    winningMessageForRound = "Round number {}: Player {} wins the round, with {} beating {}"
    drawMessageForRound = "Round number {}: This round has ended in a draw"
    
    for i in range(len(player1Cards)):
         # check if player 1 the winner?
        if (player1Cards[i] > player2Cards[i]):
            player1WinCount += 1
            roundNumber = i + 1 # because i starts from zero
            print(winningMessageForRound.format(roundNumber, 1, player1Cards[i], player2Cards[i]))
             # check if player 2 the winner?
        elif (player2Cards[i] > player1Cards[i]):
            player2WinCount += 1
            roundNumber = i + 1
            print(winningMessageForRound.format(roundNumber, 2, player2Cards[i], player1Cards[i]))
        else: 
            # check is it a draw
            numberOfTies += 1
            roundNumber = i + 1
            print(drawMessageForRound.format(roundNumber))
    
    printFinalOutcome(player1WinCount, player2WinCount, numberOfTies)
            
else:
    print("ERROR: Players don't have the same number of cards!")
