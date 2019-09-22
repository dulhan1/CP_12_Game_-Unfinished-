# user_movement_5x5
# Dulhan


import random
import time
file = open("map.txt", "r")
m = file.readlines()

lr = 0
ud = 0
text = ""
programLoop = True
total = 0
pick = ""


def Menu_Start():
    print("\033[1;32m1. Play\033[1;m")
    print("\033[1;32m2. Exit\033[1;m")
    choice = input("Please choose an option: ")
    return choice

def Menu_Game():
    print("w. Move Up")
    print("s. Move Down")
    print("a. Move Left")
    print("d. Move Right")
    print("q. Stop Current Game")
    choice2 = input("Please choose an option: ")
    return choice2

def Menu_Salesman():
    print("1. Health Reset to 25 - 5 coins")
    print("2. Weapons (Purchase/Level Up) - 10 coins")
    print("3. Armor (Increase Hitpoints) - 15 coins")
    print("4. Buy nothing")
    choice3 = input("Please choose an option: ")
    return choice3

def Menu_Monster():
    print("1. Fight (If you fight and win, you get 50 coins. If you die, you lose the game...)")
    print("2. Run (If you run, your armor, health, and weapons will all reset to 0, and you go back to point 0,0)")
    choice4 = input("Please choose an option: ")
    return choice4

def timer():
    counter = 5
    while counter > 0:
        counter = counter - 1
        time.sleep(1)
    return

def level():
    global total
    global move_count
    global x
    if move_count >= (((x+1)**2) + 11) and total >= (20*(x-1))*(x-1):
        print("LEVEL",x,"REACHED! TO REACH NEXT LEVEL, COLLECT A TOTAL OF",(20*(x-1))*(x-1),"COINS AND MOVE",(((x+1)**2) + 11)-(((x)**2) + 11),
        "MORE SPACES...")
        x = x + 1

    return

def find_something():
    global total
    global lr
    global ud
    global health
    global weapons
    global armor
    salesman = random.randint(1, 10)
    monster = random.randint(1, 20)
    if salesman == 10:
        print("You have found a traveling salesman!")
        print("Your currently have", total, "coins")
        pick = input("Do you want to purchase something? (y/n): ")
        if pick.lower() == "y":
            buyLoop = True
            while buyLoop:
                pick = Menu_Salesman()
                if pick == "1" and (total - 5) >= 0:
                    health = 25
                    total = total - 5
                    print("You have successfully purchased 25 health points!")
                    print("Your total number of coins is now", total)
                    buyLoop = False

                elif pick == "2" and (total - 10) >= 0:
                    weapons = weapons + 1
                    total = total - 10
                    print("You have successfully purchased level", weapons,"hand weapons!")
                    print("Your total number of coins is now", total)
                    buyLoop = False

                elif pick == "3" and (total - 15) >= 0:
                    armor = armor + 100
                    total = total - 15
                    print("You have successfully purchased chest armor! It has", armor, "hitpoints!")
                    print("Your total number of coins is now", total)
                    buyLoop = False

                elif pick == "4":
                    buyLoop = False

                else:
                    print("You do not have enough coins to purchase this item!")



    elif monster == 20:
        global move_count
        global gameLoop
        print("Oh No! You have found a monster!")
        pick = Menu_Monster()
        if pick == "1":
            print("You are fighting the monster")
            timer()
            if health == 25:
                if armor > 300 and weapons > 5:
                    outcome = random.randint(1, 5)
                    if outcome == 2 or outcome == 3 or outcome == 4 or outcome == 5:
                        total = total + 50
                        health = 20
                        armor = armor - 150
                        weapons = weapons - 2
                        print("You have beat the monster... good job!")
                        print("Your weapons have downgraded to level", weapons)
                        print("Your number of coins is now", total)
                        print("Your health is", health)
                        print("Your armor is at", weapons, "hitpoints")
                    else:
                        print("You lost the fight, and you have lost the game...")
                        gameLoop = False
                elif armor >=100 and weapons > 1:
                    outcome = random.randint(1, 5)
                    if outcome == 3 or outcome == 4 or outcome == 5:
                        total = total + 50
                        health = 15
                        armor = armor - 75
                        weapons = weapons - 1
                        print("You have beat the monster... good job!")
                        print("Your weapons have downgraded to level", weapons)
                        print("Your number of coins is now", total)
                        print("Your health is", health)
                        print("Your armor is at", weapons, "hitpoints")
                    else:
                        print("You lost the fight, and you have lost the game...")
                        gameLoop = False
                elif armor > 0 or weapons > 0:
                    outcome = random.randint(1,5)
                    if outcome == 4 or outcome == 5:
                        total = total + 50
                        health = 10
                        armor = armor - 150
                        weapons = weapons - 1
                        print("You have beat the monster... good job!")
                        print("Your weapons have downgraded to level", weapons)
                        print("Your number of coins is now", total)
                        print("Your health is", health)
                        print("Your armor is at", armor, "hitpoints")
                    else:
                        print("You lost the fight, and you have lost the game...")
                        gameLoop = False
                else:
                    outcome = random.randint(1,5)
                    if outcome == 4 or outcome == 5:
                        total = total + 50
                        health = 5
                        armor = 0
                        weapons = 0
                        print("You have beat the monster... good job!")
                        print("You have no armor and weapons.")
                        print("Your health is at", health)
                        print("Your number of coins is now", total)
                    else:
                        print("You lost the fight, and you have lost the game...")
                        gameLoop = False
            elif health > 9:
                if armor >= 300 and weapons >= 3:
                    outcome = random.randint(1,2)
                    if outcome == 2:
                        total = total + 50
                        health = 1
                        armor = armor - 200
                        weapons = weapons - 2
                        print("You have beat the monster... good job!")
                        print("Your weapons have downgraded to level", weapons)
                        print("Your number of coins is now", total)
                        print("Your health is at 1 hp! Get health as soon as possible!")
                        print("Your armor is at", armor, "hitpoints")
                    else:
                        print("You lost the fight, and you have lost the game...")
                        gameLoop = False
            else:
                print("You lost the fight, and you have lost the game...")
                gameLoop = False

        else:
            ud = 0
            lr = 0
            armor = 0
            weapons = 0
            health = 0
            move_count = 0


    else:
        coin = random.randint(0, 5)
        if coin == 5:
            pick = input("You found a coin! Do you want to pick it up? (y,n): ")
            if pick.lower() == "y":
                total = total + 1
                print("You picked up the coin!")
                print("Your total number of coins is now", total)
    return

def movement(move):
    global lr
    global ud
    global total
    global move_count
    if move == "s":
        if ud < 4:
            ud = ud +1
            lists()
            find_something()
            move_count = move_count + 1
        else:
            print("You hit a wall!")

    if move == "w":
        if ud > 0:
            ud = ud - 1
            lists()
            find_something()
            move_count = move_count + 1
        else:
            print("You hit a wall!")

    if move == "d":
        if lr < 4:
            lr = lr +1
            lists()
            find_something()
            move_count = move_count + 1
        else:
            print("You hit a wall!")

    if move == "a":
        if lr > 0:
            lr = lr - 1
            lists()
            find_something()
            move_count = move_count + 1
        else:
            print("You hit a wall!")
    return

def lists():
    # get the number of rows
    # get the number of columns
    rows = len(m)
    cols = len(m[0])-1


    # print original list of strings which still includes newline characters
    for i in range(rows):
        for j in range(cols):

            if i == ud and j == lr:
                print("\033[1;32mX\033[1;m", end='')
            else:
                print(m[i][j], end='')  # prints space and no newline character
        print("")  # prints newline character
    return


while programLoop:
    lr = 2
    ud = 2
    move_count = 0
    total = 0
    health = 25
    armor = 0
    weapons = 0
    x = 2
    text = Menu_Start()
    if text == "1":
        gameLoop = True
        print("LEVEL 1 - COLLECT 20 COINS AND MOVE 20 SPACES TO REACH NEXT LEVEL...")
        print("GAME STARTING IN 5 SECONDS...")

        while gameLoop:

            text = Menu_Game()

            if text == "q":
                gameLoop = False
            else:
                movement(text)

    elif text == "2":
        print("Program Exiting")
        programLoop = False

input("Press enter to continue")
