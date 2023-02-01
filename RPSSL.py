#! /usr/bin/env /usr/bin/python3

from simple_term_menu import TerminalMenu
import random, json

signs = ["rock", "paper", "scissors", "spock", "lizard"]

class PlayerStats:
    def __init__(self, name):
        try:
            with open(name+".json", "r") as f:
                dct = f.read()
                print(dct)
        except:
 
        if name == "":
            self.playerWins = [0, 0, 0, 0, 0] # wins with rock paper, scissors etc
            self.playerLosses = [0, 0, 0, 0, 0] # losses with rock, paper, scissors, etc
            self.playerDraws = 0
            self.name = name


    def __str__(self):
        out = f"draws: {self.playerDraws}\n"
        out += "\nwins:\n"
        for i in range(0, len(self.playerWins)):
            out += f"{signs[i]}: {self.playerWins[i]}\n"
        out += "\nlosses:\n"
        for i in range(0, len(self.playerLosses)):
            out += f"{signs[i]}: {self.playerLosses[i]}\n"
        return out

    def asDict(self):
        return {
            "name": self.name,
            "draws" : self.playerDraws,
            "losses" : self.playerLosses,
            "wins" : self.playerWins
        }

def playerWins(player, sheldon):
    #true if player wins, false if sheldon wins
    if(player==sheldon):
        return None
    if(player == signs[signs.index(sheldon)-2] or
       sheldon == signs[signs.index(player)-1]):
        return True
    return False

def play(stats):
    print("choose:")
    playerChoice = signs[TerminalMenu(signs).show()]
    sheldonChoice = random.choice(signs)
    print("you chose " + playerChoice)
    print("sheldon chose " + sheldonChoice)

    pWins = playerWins(playerChoice, sheldonChoice)
    if pWins == None:
        print("draw!")
        stats.playerDraws += 1
    elif pWins:
        print("you win!")
        stats.playerWins[signs.index(playerChoice)] += 1
    else:
        print("sheldon wins!")
        stats.playerLosses[signs.index(playerChoice)] += 1

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
            with open(stats.name+".json", "w") as f:
                print("writing as " + stats.name + ".json")
                f.write(json.dumps(stats.asDict()))
        else:
            break
    print("goodbye!")

if __name__ == "__main__":
    name = input("username: ")
    stats = PlayerStats(name) # TODO read from disk
    menu(stats)
