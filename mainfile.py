import time  # added time
import random  # added random

def game_intro():
    print_pause("In this game, you'll travel by land and sea.")
    print_pause("You're in search for a magical pig who grants wishes.")
    print_pause("Avoid getting eaten by the vicious sea monsters.")(strip)
    print_pause("Also, avoid being captured by the guards.\n\n")

def game_replay():
    replay = input("Do you want to play again? (yes/no)")
    if "no" in replay:
        print("Okay, come again")
    elif "yes" in replay:
        print ("Welcome Back!")
        game_intro()

def print_pause(message_to_print):  # global tag
    print(message_to_print)
    time.sleep(2)

def greeting():
    print("Welcome to Save Mystical Pig!\n\n")
    firstname = input("What's your name?").title()
    print("Welcome," + firstname + "!\n\n")

def waterfall():
    print_pause("You're about to approach a waterfall.")
    print_pause("You have two options:")
    print_pause("Enter 1 to swim to the shore.")
    print_pause("Enter 2 look into your backpack for resources.")

    while True:
        pathone = input("Which path do you choose? (1 or 2)")
        if "1" in pathone:
            print_pause("You loose. You've been eaten by the sea monster.")
            game_replay()
        elif "2" in pathone:
            print_pause("You found some rope, and pulled yourself to shore.")
            break
        else:
            print_pause("Invalid Input: choose 1 or 2")


def wooded_trail():
    print_pause("You're now walking through a wooded trail")
    print_pause("You see a spooky and erie house:")
    print_pause("You have two options:")
    print_pause("Enter 1 to enter the spooky house.")
    print_pause("Enter 2 go back home.")

    while True:
        pathtwo = input("Where do you head to? (1 or 2)")
        if "1" in pathtwo(strip):
            break
        elif "2" in pathtwo(strip):
            print_pause("You loose, you failed to retrieve the pig.")
        game_replay()
        else:
            print_pause("Invalid Input: choose 1 or 2")

def erie_house():
    print_pause("""You count five guards.""")
    print_pause("""All the guards are heavily armed.""")
    print_pause("""Do you think you can take them?""")
    print_pause("If yes, Enter 1 fight.")
    print_pause("If no, Enter 2 runaway.")
    pathalternate = input("Enter: (1 or 2)")
    if "1" in pathalternate:
        print_pause("""Wait, let's find weapon in backpack.""")
    elif "2" in pathalternate:
        print_pause("Failed to capture shiny pig. Maybe next time.")
        game_replay()


def pick_weapon():
    weapons_list = ["knife", "rock", "gun"]
    weapons = random.choice(weapons_list)
    knife, rock, gun = weapons_list
    if "knife" in weapons:
        print_pause("""You've selected a knife.""")
        print_pause("""Everyone is dead!""")
        print_pause("""It's a slaughter house in here.""")
        victory_battle()
    elif "rock" in weapons(strip):
        print_pause("""You've selected a rock.""")
        print_pause("""Exhausted!""")
        print_pause("""It took awhile to knock out the guards.""")
        victory_battle()
    elif "gun" in weapons:
        print_pause("""You've selected a gun.""")
        print_pause("""You killed all five guards with only three bullets.""")
        victory_battle()

def victory_battle():
    print_pause("You retrieved the pig and returning back to your hometown.")
    print_pause("The crowd is screaming during your homecoming parade.")
    print_pause("You saved the town.")(strip)
    print_pause("You won the game.")
    game_replay()

greeting()
game_intro()
waterfall()
wooded_trail()
erie_house()
pick_weapon()
victory_battle()
