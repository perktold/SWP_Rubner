#! /usr/bin/env /usr/bin/python3

from simple_term_menu import TerminalMenu
import random 

signs = ["rock", "paper", "scissors", "spock", "lizard"]

class PlayerStats:
    def __init__(self):
        self.playerWins = [0, 0, 0, 0, 0] # wins with rock paper, scissors etc
        self.playerLosses = [0, 0, 0, 0, 0] # losses with rock, paper, scissors, etc
        self.playerDraws = 0

    def __str__():
        return f"{self.playerWins}({self.playerDraws})"
            

def playerWins(player, sheldon):
    #true if player wins, false if sheldon wins
    if(player==sheldon):
        return None
    if(player == signs[signs.index(sheldon)-2] or
       sheldon == signs[signs.index(player)-1]):
        return True
    return False

def play():
    print("choose:")
    playerChoice = signs[TerminalMenu(signs).show()]
    sheldonChoice = random.choice(signs)
    print("you chose " + playerChoice)
    print("sheldon chose " + sheldonChoice)

    pWins = playerWins(playerChoice, sheldonChoice)
    if pWins == None:
        print("draw!")
    elif pWins:
        print("you win!")
    else:
        print("sheldon wins!")

def menu(stats):
    while True:
        initChoice = TerminalMenu(["play", "endless", "view statistics", "save", "quit"]).show()
        if initChoice == 0:
            play(stats)
        elif initChoice == 1:
            while True:
                try:
                    play(stats)
                except:
                    break
        elif initChoice == 2:
            print(stats)
        elif initChoice == 3:
            print("WIP")
        else:
            break
    print("goodbye!")

if __name__ == "__main__":
    stats = PlayerStats() # TODO read from disk
    menu(stats)
