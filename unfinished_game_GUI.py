from tkinter import *
import random

master = Tk()
a = 1
b = 1
file = open("saved.txt", "r")
m = file.readlines()
total = int(m[0])
health = int(m[1])
weapons = int(m[2])
armor = int(m[3])
level = int(m[4])
print(total, health, weapons, armor)
freeze = False

sold = False


##############################################################################

def restart():
    global character
    global freeze
    global level
    global a
    global b

    delete()
    a = 1
    b = 1
    total = 0
    armor = 0
    weapons = 0
    level = 1
    found.set("")
    bottom.set("")
    w.coords(character, 25, 25)
    stats.set("Coins - " + str(total) + " Health - " + str(health) + " Weapons - " + str(weapons) + " Armor - " + str(armor))
    level_disp.set("YOU ARE AT LEVEL " + str(level) + ". Reach the black square and collect " + str(
        level * 10) + " coins to level up.")
    Button1.forget()
    file = open("saved.txt", "w")
    file.write(str(total) + "\n")
    file.write(str(health) + "\n")
    file.write(str(weapons) + "\n")
    file.write(str(armor) + "\n")
    file.write(str(level) + "\n")
    file.close()
    freeze = False

def fight():
    global total
    global character
    global level
    global Button1
    global health
    delete()
    w.after(3000)
    if health < 10:
        num = 5
    elif health < 25:
        num = 3
    else:
        if level > 25:
            num = 2
        elif level > 10:
            if armor > 200 and weapons > 100:
                num = 2
            else:
                num = 3
        else:
            if armor >= 100 and weapons >= 25:
                num = 2
            else:
                num = 3

    chance = random.randint(1, num)
    if chance == 1:
        total = total + 20
        found.set("")
        health = round(health / 2)
        bottom.set("Hurray, you have beat the monster and earned 20 coins!")
        stats.set("Coins - " + str(total) + " Health - " + str(health) + " Weapons - " + str(weapons) + " Armor - " + str(
                armor))

    else:
        found.set("")
        bottom.set("SADLY, YOU LOST...")
        Button1 = Button(master, text="RESTART", command=restart)
        Button1.pack(side=BOTTOM)

def run():
    global character
    global a
    global b
    delete()
    a = 1
    b = 1
    total = 0
    armor = 0
    weapons = 0
    found.set("")
    bottom.set("You ran and lost all you weapons, armor, and coins! Good luck!")
    w.coords(character, 25, 25)
    stats.set(
        "Coins - " + str(total) + " Health - " + str(health) + " Weapons - " + str(weapons) + " Armor - " + str(armor))
    file = open("saved.txt", "w")
    file.write(str(total) + "\n")
    file.write(str(health) + "\n")
    file.write(str(weapons) + "\n")
    file.write(str(armor) + "\n")
    file.write(str(level) + "\n")
    file.close()


def level_up():
    global spot
    global level
    if total >= level * 10:
        level = level + 1
        level_disp.set("YOU ARE AT LEVEL " + str(level) + ". Reach the black square and collect " + str(
            level * 10) + " coins to level up.")
        w.itemconfig(spot, fill="green")
        w.tag_raise(character)
        black()
    else:
        bottom.set("You still need " + str(level * 10 - total) + " coins to level up!")
    return


def black():
    global bx
    global by
    global spot
    while True:
        bx = random.randint(1, 39)
        by = random.randint(1, 16)
        if map[by][bx] == "g":
            spot = w.create_rectangle(bx * 25, by * 25, bx * 25 + 25, by * 25 + 25, fill="black", outline=color)
            break


def no():
    global freeze
    Button1.forget()
    Button2.forget()
    freeze = False
    found.set("")
    bottom.set("")
    stats.set(
        "Coins - " + str(total) + " Health - " + str(health) + " Weapons - " + str(weapons) + " Armor - " + str(armor))


def delete():
    global sold
    global freeze
    bottom.set("")
    if sold:
        Button3.forget()
        Button4.forget()
        Button5.forget()
        Button6.forget()
        sold = False
    else:
        Button1.forget()
        Button2.forget()

    freeze = False
    stats.set(
        "Coins - " + str(total) + " Health - " + str(health) + " Weapons - " + str(weapons) + " Armor - " + str(armor))


def pick():
    global freeze
    global total
    total = total + 1
    bottom.set("You picked up the coin!")
    no()


def Health():
    global total
    global health
    if total >= 5:
        health = 25
        total = total - 5
        bottom.set("Your health was reset to 25 hp")
    else:
        found.set("You do not have enough coins to purchase this item!")
    delete()


def Weapons():
    global weapons
    global total
    found.set("")
    if total >= 10:
        weapons = weapons + level * 25
        total = total - 10
        found.set("You have successfully purchased hand weapons! It has " + str(weapons) + " ammunition!")
    else:
        found.set("You do not have enough coins to purchase this item!")
    delete()


def Armor():
    global armor
    global total
    if total >= 15:
        armor = armor + level * 100
        total = total - 15
        found.set("You have successfully purchased chest armor! It has " + str(armor) + " hitpoints!")
        found.set("Your total number of coins is now " + str(total))
    else:
        found.set("You do not have enough coins to purchase this item!")
    delete()


def menu_salesman():
    global sold
    global Button3
    global Button4
    global Button5
    global Button6
    global freeze
    delete()
    found.set("")
    sold = True
    freeze = True
    Button3 = Button(master, text="Health to 25 - 5 coins", command=Health)
    Button3.pack(side=BOTTOM)
    Button4 = Button(master, text = "Weapons - 10 coins", command = Weapons)
    Button4.pack(side = BOTTOM)
    Button5 = Button(master, text="Armor - 15 coins", command=Armor)
    Button5.pack(side=BOTTOM)
    Button6 = Button(master, text="Leave Items", command=delete)
    Button6.pack(side=BOTTOM)


def find_something():
    global Button1
    global Button2
    global freeze
    global total
    global lr
    global ud

    salesman = random.randint(0, 20)
    monster = random.randint(1, 40)

    if monster == 17:
        freeze = True
        found.set("You have found a monster! Oh no!! They have " + str(level * 25) + " hitpoints!")
        bottom.set("Run and lose all you coins. Fight to either win coins or die")
        Button1 = Button(master, text="Run", command=run)
        Button1.pack(side=BOTTOM)
        Button2 = Button(master, text="Fight - Takes 3 seconds", command=fight)
        Button2.pack(side=BOTTOM)

    elif salesman == 10 and total >= 5:
        freeze = True
        found.set("You have found a traveling salesman!")
        Button1 = Button(master, text="Purchase Something?", command=menu_salesman)
        Button1.pack(side=BOTTOM)
        Button2 = Button(master, text="Don't Purchase", command=no)
        Button2.pack(side=BOTTOM)


    else:
        coin = random.randint(0, 15)
        if coin == 8:
            freeze = True
            found.set("You found a coin! Do you want to pick it up? (y,n): ")
            Button1 = Button(master, text="Pick Up?", command=pick)
            Button1.pack(side=BOTTOM)
            Button2 = Button(master, text="Leave", command=no)
            Button2.pack(side=BOTTOM)
    return


################################################################################
def movement():
    global lr
    global ud
    global total

    if letter == "s" and not freeze:
        if a < 18:
            find_something()
            move.set("You moved" + " down")
        else:
            move.set("You hit a wall!")

    elif letter == "w" and not freeze:
        if a > 0:
            find_something()
            move.set("You moved" + " up")
        else:
            move.set("You hit a wall!")

    elif letter == "d" and not freeze:
        if b < 41:
            find_something()
            move.set("You moved" + " right")
        else:
            move.set("You hit a wall!")

    elif letter == "a" and not freeze:
        if b > 0:
            find_something()
            move.set("You moved" + " left")
        else:
            move.set("You hit a wall!")

    if a == by and b == bx:
        bottom.set("")

        level_up()
    return


################################################################################

def key(event):
    global character
    global y
    global x
    global a
    global b
    global rows
    global cols
    global letter
    global freeze
    xm = 0
    ym = 0
    letter = event.char

    if letter == "l" and not freeze:
        file = open("saved.txt", "w")
        file.write(str(total) + "\n")
        file.write(str(health) + "\n")
        file.write(str(weapons) + "\n")
        file.write(str(armor) + "\n")
        file.write(str(level) + "\n")
        file.close()
        master.destroy()


    elif (letter == "w" or letter == "\uf700") and not freeze:
        if map[a - 1][b] == "g" and a - 1 >= 0:
            y = y - 25
            a = a - 1
            ym = -25
            found.set("")
    elif (letter == "a" or letter == "\uf702") and not freeze:
        if map[a][b - 1] == "g" and b - 1 >= 0:
            x = x - 25
            b = b - 1
            xm = -25
            found.set("")
    elif (letter == "d" or letter == "\uf703") and not freeze:
        if map[a][b + 1] == "g" and b + 1 <= len(m[0]) - 1:
            x = x + 25
            b = b + 1
            xm = 25
            found.set("")
    elif (letter == "s" or letter == "\uf701") and not freeze:
        if map[a + 1][b] == "g" and a + 1 <= len(m):
            y = y + 25
            a = a + 1
            ym = 25
            found.set("")
    w.move(character, xm, ym)
    movement()


################################################################################

x = 25
y = 25

file = open("map.txt", "r")
m = file.readlines()

rows = len(m)
cols = len(m[0]) - 1

map = [[" " for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        map[i][j] = m[i][j]

w = Canvas(master, width=cols * 25, height=rows * 25)
photo = PhotoImage(file='pic.gif')

bottom = StringVar()

move = StringVar()

L5 = Label(master, textvariable=move)
L5.pack(side=BOTTOM)

L1 = Label(master, textvariable=bottom)
L1.pack(side=BOTTOM)

found = StringVar()

L2 = Label(master, textvariable=found)
L2.pack(side=BOTTOM)

level_disp = StringVar()
level_disp.set("YOU ARE AT LEVEL " + str(level) + ". Reach the black square and collect " + str(
    level * 10) + " coins to level up.")

L4 = Label(master, textvariable=level_disp)
L4.pack(side=BOTTOM)

stats = StringVar()
stats.set(
    "Coins - " + str(total) + " Health - " + str(health) + " Weapons - " + str(weapons) + " Armor - " + str(armor))

L3 = Label(master, textvariable=stats)
L3.pack(side=BOTTOM)

instructions = StringVar()
instructions.set("w = up, d = right, a = left, s = down, l = leave and save")
L6 = Label(master, textvariable=instructions)
L6.pack(side=BOTTOM)

for i in range(rows):
    for j in range(cols):
        if map[i][j] == "g":
            color = "green"
        elif map[i][j] == "r":
            color = "blue"
        elif map[i][j] == "t":
            color = "yellow"
        elif map[i][j] == "b":
            color = "brown"
        w.create_rectangle(j * 25, i * 25, j * 25 + 25, i * 25 + 25, fill=color, outline=color)
    print("")

black()
character = w.create_image(x, y, image=photo, anchor=NW)

w.focus_set()
w.bind("<Key>", key)
w.pack()
master.mainloop()
