# Black Jack
# Card is tuple (Suit, Value)
# (0, 0) is null card
import random

# Returns card to be added to stack
def generateCard(cardsInPlay):
    # Possible suits of cards
    # Clubs is C, Diamonds is D, Heart is H, and Clover is R
    Suits = ['C', 'D', 'H', 'R']
    # Possible values for cards
    Value = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    # Suit of generated card
    suit = 0
    # Value of generated card
    value = 0
    # While card isn't a possible card option
    notValid = True

    # Generated card until a valid one comes up
    while notValid:
        suit = random.randrange(0, 4)
        value = random.randrange(0, 13)

        # Gets Suit Char for card
        if suit == 0:
            suit = 'C'
        elif suit == 1:
            suit = 'D'
        elif suit == 2:
            suit = 'H'
        else:
            suit = 'R'

        # Gets Value for card
        if value == 0:
            value = 'A'
        elif value == 10:
            value = 'J'
        elif value == 11:
            value = 'Q'
        elif value == 12:
            value = 'K'
        else:
            value += 1

        # Checks if card is already in play
        if (suit, value) in cardsInPlay:
            pass
        else:
            notValid = False

    return (suit, value)

# Returns value of stack for player
def calculateValue(playersCards):
    # Value of stack
    value = 0
    # Number of aces
    aceCount = 0

    # Gets value of cards in stack without Aces
    for card in playersCards:
        if card[1] == 'A':
            aceCount += 1
        elif card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
            value += 10
        else:
            value += card[1]

    # Add value of aces to value of card stack
    value += aceCount
    for i in range(aceCount):
        if value <= 11:
            value += 10

    return value

# Decides which move for dealer
def dealerDecision(playerCards, dealerCards):
    # If 17, stand
    if calculateValue(dealerCards) == 17:
        return (0, 0)
    # If less than 17, hit
    elif calculateValue(dealerCards) < 17:
        return generateCard(playerCards + dealerCards)
    # If less than player, hit
    elif calculateValue(dealerCards) < calculateValue(playerCards):
        return generateCard(playerCards + dealerCards)
    # Else, stand
    else:
        return (0, 0)

# Gets user's action
def readUserInput(cardsInPlay):
    # Asks until valid input is given
    while True:
        move = input('Will you HIT(1) or STAND(2)?')
        # If hit, add card to stack
        if move == 'HIT' or move == '1':
            return generateCard(cardsInPlay)
        # If stand, return null card
        elif move == 'STAND' or move == '2':
            return (0, 0)
        else:
            pass

# Runs game
def runGame():
    # Stacks for player and dealer cards
    playerCards = []
    dealerCards = []

    # Adds 2 cards to player stack and 1 card to dealer stack
    playerCards.append(generateCard(playerCards + dealerCards))
    dealerCards.append(generateCard(playerCards + dealerCards))
    playerCards.append(generateCard(playerCards + dealerCards))

    if calculateValue(playerCards) == 21:
        print('Blackjack! You win!')

    # Player's turn
    while True:
        displayCards(playerCards, dealerCards)
        # Checks if bust
        if calculateValue(playerCards) > 21:
            print('You have busted! You lose!')
            return None
        # Player moves
        card = readUserInput(playerCards + dealerCards)
        if card == (0, 0):
            break
        else:
            playerCards.append(card)

    # Dealer starts his turn
    dealerCards.append(generateCard(playerCards + dealerCards))

    # Dealer's turn
    while True:
        displayCards(playerCards, dealerCards)
        # Checks if bust
        if calculateValue(dealerCards) > 21:
            print('Dealer has busted! You win!')
            return None
        # Dealer moves
        newCard = dealerDecision(playerCards, dealerCards)
        if newCard == (0, 0):
            break
        else:
            dealerCards.append(newCard)

    # Checks who wins or if tie
    if calculateValue(playerCards) > calculateValue(dealerCards):
        print('You win!')
    elif calculateValue(dealerCards) > calculateValue(playerCards):
        print('You lose!')
    else:
        print('It\'s a tie!')

# Displays cards and their values
def displayCards(playerCards, dealerCards):
    print(dealerCards, end = ' ')
    print('=', end = ' ')
    print(calculateValue(dealerCards))
    print(playerCards, end = ' ')
    print('=', end = ' ')
    print(calculateValue(playerCards))
    print('--------------------------------------------------------------')

def main():
    for i in range(5):
        runGame()

if __name__ == '__main__':
    main()
