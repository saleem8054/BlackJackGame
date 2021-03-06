import random
from os import system
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computerCards = []
userCards = []

def putRandomValues():
    for _ in range(2):
        userCards.append(random.choice(cards))
        computerCards.append(random.choice(cards))

def userInput():
    userCards.append(random.choice(cards))
    if 11 in userCards and calcSum(userCards) > 21:
        userCards.remove(11)
        userCards.append(1)

def computerInput():
    computerCards.append(random.choice(cards))
            
def isGreaterThan21():
    if calcSum(userCards) > 21:
        return True
    else:
        return False
    
def adjustComputerCardSum():
    while calcSum(computerCards) < 17 :
        computerInput()
        
def calcSum(card):
    return sum(card)

def checkBlackJack(card):
    if calcSum(card) == 21 and len(card) == 2:
        return True
    return False 
    
def decision():
    print(f"your final hand: {userCards}, final score: "+str(calcSum(userCards)))
    adjustComputerCardSum()
    print(f"Computer final hand: {computerCards}, final score: "+str(calcSum(computerCards)))
    message = ""
    if calcSum(userCards) > 21:
        message = "You went over. You lose"
    elif calcSum(computerCards) > 21:
        message = "Opponent went over. You win" 
    elif calcSum(computerCards) > calcSum(userCards):
        message = "Opponent has higher score than you. Opponent wins"
    elif calcSum(computerCards) < calcSum(userCards):
        message = "You have higher score than opponent. You win"
    else:
        message = "Match is draw."
    
    print(message)

def play(permissionToPlay):
    while permissionToPlay:    
        print(f"Your cards: {userCards}, current score: "+str(calcSum(userCards)))    
        print(f"Computer's first card: {computerCards[0]}")
            
        if isGreaterThan21():
            decision()
            permissionToPlay = False
            
        else:
            isContinue = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if isContinue.lower() == "n":
                decision()
                permissionToPlay = False
            else:
                userInput()

permissionToPlay = True
while permissionToPlay:
    permission = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") 
    if permission.lower() == 'y':
        system('clear')
        print(logo)
        putRandomValues()
        if checkBlackJack(userCards):
            print("User got the BlackJack. User wins.")
        elif checkBlackJack(computerCards):
            print("Computer got the BlackJack. Computer wins.")
        else:    
            play(permissionToPlay)
        userCards = []
        computerCards = []
            
    else:
        permissionToPlay = False
