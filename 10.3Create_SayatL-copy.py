# Blackjack!
"""
The user will play against the house, and after they are given a card, 
they can ask the house for another card (for a maximum of 5 cards) 
until they reach a maximum point value of 21 (bust). The program will
default to ending the round when the user busts. When the user decides to
play instead of taking another card, the program will print the hand (and its
corresponding value) for the house and the player, automatically deciding the
winner by comparing the values. 
"""

import random

# Converts random generated values to face cards
facesDict = {
    1 : "A",
    11 : "J",
    12 : "Q",
    13 : "K"
}

# Saves hands and scores
playerHand = []
houseHand = []
playerScore = 0
houseScore = 0

# finds the current cards in play to pass to the random card get program
def find_in_play():
    # Adds hands to a comprehensive list for convenient comparison/tally
    cards_in_play = []
    cards_in_play.extend(playerHand)
    cards_in_play.extend(houseHand)

    in_playList = []

    # Checks for the amount of each card and saves number of each of the the current cards in play in a list
    for i in range(1,14):
        temp = 0
        for card in cards_in_play:
            if i == card:
                temp += 1
        in_playList.append(temp)
    return in_playList
    
# Gets a card from the deck to add into a hand
def get_card(in_play):
    card = random.randrange(1,14,1)

    # Make sure theres aren't more than 4 of the same cards in play
    while in_play[card-1] == 4:
        card = random.randrange(1,14,1)
    return card

# formats the hand to include face/ace cards (from numbers)
def format_hand(hand):
    formatted_hand = []
    for card in hand:
        if card >= 11:
            formatted_hand.append(facesDict[card])
        elif card == 1:
            formatted_hand.append(facesDict[card])
        else: 
            formatted_hand.append(card)
    return formatted_hand

# Get an action from the player (draw or play)
def get_input():
    action = input("Action: ")
    while action != "draw" and action != "play":
        print("Please input a valid action.")
        action = input("Action: ")
    return action

# Verify if the player wants to play another round
def verify_again():
    again = input("Do you want to play another round? y/n ")
    while again != "n" and again != "y":
        print(again)
        print("Please input y or n.")
        again = input("Do you want to play another round? y/n ")
    if "y" == again:
        return True
    elif "n" == again:
        return False

# score the current hands of both players
def score_hands():
    phand = []
    hhand = []
    
    # for each card in the player's hand, add its value to the list (face = 10), sum list
    for card in playerHand:
        if card >= 11:
            phand.append(10)
        else:
            phand.append(card)
    
    # for each card in the house's hand, add its value to the list (face = 10), sum list
    for card in houseHand:
        if card >= 11:
            hhand.append(10)
        else:
            hhand.append(card)
    
    return (sum(phand), sum(hhand))

# Run the entire game (cycle of drawing until a play, display scores, etc)
def run_game():

    # Deal initial hands
    playerHand.append(get_card(find_in_play()))
    houseHand.append(get_card(find_in_play()))
    houseHand.append(get_card(find_in_play()))

    playerScore = score_hands()[0]
    print(f"Your hand: \n{format_hand(playerHand)}\nScore: {playerScore}")

    while True:
        # Enforces a maximum hand of 5 cards
        if len(playerHand) >= 5:
            print("You can't draw any more cards!")

            break
        # Enforces a maximum score of 21
        elif sum(playerHand) > 22:
            print("You bust!")
            
            break
        else:
            #Ask the user what they want to do next
            act = get_input()
            if act == "draw":
                playerHand.append(get_card(find_in_play()))
                playerScore = score_hands()[0]

                print(f"Your hand: \n{format_hand(playerHand)}\nScore:{playerScore}")
            elif act == "play":
                break

    # Score the current hands before printing both
    playerScore = score_hands()[0]
    houseScore = score_hands()[1]

    # Print both hands and their scores
    print(f"The House: \n{format_hand(houseHand)}\nScore: {houseScore}")
    print(f"Your Hand: \n{format_hand(playerHand)}\nScore: {playerScore}")

    # Determine the winner by comparing scores, Note: impossible for house to bust
    if playerScore > 21:
        print("You lose!")
    elif playerScore < houseScore:
        print("You lose!")
    else:
        print("You win!")


# Print instructions
print("Welcome to BLACKJACK! \n\
The user will play against the house, and after they are given a card, \
they can ask the house for another card (for a maximum of 5 cards) \
until they reach a maximum point value of 21 (bust). The program will \
default to ending the round when the user busts. When the user decides to \
play instead of taking another card, the program will print the hand (and its \
corresponding value) for the house and the player, automatically deciding the \
winner by comparing the values. ")

# Main game will run until the user decides to quit
while True:
    run_game()
    if not verify_again():
        break
    playerHand = []
    houseHand = []
    playerScore = 0
    houseScore = 0