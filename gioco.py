import random
import os
import items
from maps import mappa
import pickle


class Player:
    def __init__(self, name):
        self.name = name
        self.lvl = 1
        self.points = 5
        self.attributepoints = 2
        self.str = 5
        self.agy = 5
        self.vit = 1
        self.ene = 1
        self.exp = 1
        self.exptolvl = self.lvl * 2.5
        self.maxhp = 100 + (self.vit * 2)
        self.maxmp = 100 + (self.ene * 2)
        self.hp = self.maxhp
        self.mp = self.maxmp
        self.gold = 50
        self.primary = [items.Wood_Sword]
        self.secondary = [items.Wood_Shield]
        self.armor = [items.Wood_Armor]
        self.attack = self.str + self.primary[0].attack + self.agy
        self.defense = self.agy + (self.armor[0].attack/2) + (self.secondary[0].attack/2) + (self.vit / 1.5)
        self.magicattack = ((self.ene * 1.5) + self.primary[0].attack + self.agy)/2
        self.inventory = []


    def update(self):
        self.attack = self.str + self.primary[0].attack + self.agy
        self.defense = self.agy + (self.armor[0].attack/2) + (self.secondary[0].attack/2) + (self.vit / 1.5)
        self.magicattack = ((self.ene * 1.5) + self.primary[0].attack + self.agy) / 2


def main():
    clear()
    print("New Game")
    print("Load Game")
    print("Options")
    print("Exit")
    option = input("What do you want to do: ").lower()
    if option == "new game":
        start()
    elif option == "load game":
        loadgame()
    else:
        main()


def load(save):
    global playerig
    playerig = save
    input(f"Welcome back {playerig.name}, we missed you")
    game()


def start():
    print("Hello welcome to mu")
    name = input("What is your name ? \n")
    global playerig
    playerig = Player(name)
    game()


def game():
    os.system('cls')
    print(f"Explore             Level {round(playerig.lvl, 2)}  Health {round(playerig.hp, 2)}/{round(playerig.maxhp, 2)}   Mana {round(playerig.mp, 2)}/{round(playerig.maxmp, 2)}")
    print("Inventory")
    print("Character           Primary Weapon       Armor         Shield")
    print(f"Harald                {playerig.primary[0].name}       {playerig.armor[0].name}     {playerig.secondary[0].name}")
    print("Skills")
    print(f"Credits             Experience   Attack   Magic Attack   Defense")
    print(f"Save                  {playerig.exp}/{playerig.exptolvl}       {round(playerig.attack, 2)}        {round(playerig.magicattack, 2)}         {round(playerig.defense, 2)}")
    print("Exit")
    option = input("\nWhat do you want to do ?\n").lower()
    if option == "credits":
        input("Just you")
        game()
    elif option == "skills":
        skillupgrade()
    elif option == "harald":
        harald()
    elif option == "inventory":
        inventory()
    elif option == "explore":
        explore(mappa)
    elif option == "character":
        character()
    elif option == "exit":
        input("Cyaaa\n")
        os.system("exit")
    elif option == "save":
        savegame()
    else:
        game()


def explore(map):
    clear()
    print(f"You are in {map.curzone}")
    print("\nWrite travel north or travel south to explore new zones else write back to go back.")
    option = input("\nWhat do you want to do?\n").lower()
    if option == "travel north" or option == "travel south":
        clear()
        if map.loot == True:
            luck = random.randint(1, 30)
            if luck == 17:
                print(f"There is something on the ground")
                print(f"...")
                print(f"You found  {items.Great_Sword.name}")
                giveitem(items.Great_Sword)
                input("Press enter to continue")
        if option == "travel north":
            if map.walking < 40:
                playerig.hp += (playerig.maxhp * 0.10)
                if playerig.hp > playerig.maxhp:
                    playerig.hp = playerig.maxhp
                playerig.hp += (playerig.maxhp * 0.10)
                if playerig.mp > playerig.maxmp:
                    playerig.mp = playerig.maxmp
                map.walking += 1
                if map.walking == 5:
                    map.count = 1
                    map.curzone = map.zone[map.count]
                    print(f"You arrived in {map.curzone}\n")
                elif map.walking == 10:
                    map.count = 2
                    map.curzone = map.zone[map.count]
                    print(f"You arrived in {map.curzone}\n")
                elif map.walking == 20:
                    map.count = 3
                    map.curzone = map.zone[map.count]
                    print(f"You arrived in {map.curzone}\n")
                elif map.walking == 40:
                    map.count = 4
                    map.curzone = map.zone[map.count]
                    print(f"You arrived in {map.curzone}\n")
                print("You advance\n")
                print("Nothing to see around")
            elif map.walking >= 4:
                input("You can't go more north than this\n")
        elif option == "travel south":
            if map.walking > 0:
                playerig.hp += (playerig.maxhp * 0.10)
                if playerig.hp > playerig.maxhp:
                    playerig.hp = playerig.maxhp
                playerig.hp += (playerig.maxhp * 0.10)
                if playerig.mp > playerig.maxmp:
                    playerig.mp = playerig.maxmp
                map.walking -= 1
                if map.walking == 0:
                    map.count = 0
                    map.curzone = map.zone[map.count]
                    print(f"You arrived in {map.curzone}\n")
                elif map.walking == 5:
                    map.count -= 1
                    map.curzone = map.zone[map.count]
                    print(f"You arrived in {map.curzone}\n")
                elif map.walking == 10:
                    map.count -= 2
                    map.curzone = map.zone[map.count]
                    print(f"You arrived in {map.curzone}\n")
                elif map.walking == 20:
                    map.count -= 3
                    map.curzone = map.zone[map.count]
                    print(f"You arrived in {map.curzone}\n")
                print("You advance\n")
                print("Nothing to see around")
            elif map.walking <= 0:
                input("You can't go more south than this\n")
        if map.fight == True:
            monsterlist = [items.Spider, items.Huge_Spider]
            monsterlist1 = [items.Baby_Dragon, items.Goblin]
            monsterlist2 = [items.Stone_Goblin, items.Cyclop]
            monsterlist3 = [items.Great_Dragon, items.Cyclop]
            monsterlist4 = [items.Great_Dragon, items.Great_Dragon, items.Great_Dragon, items.Golden_Dragon]
            luck = random.randint(1, 2)
            if luck == 2:
                if map.curzone == map.zone[0]:
                        luck1 = random.choice(monsterlist)
                        print(luck1.name)
                        fight(luck1)
                elif map.curzone == map.zone[1]:
                        luck1 = random.choice(monsterlist1)
                        fight(luck1)
                elif map.curzone == map.zone[2]:
                        luck1 = random.choice(monsterlist2)
                        fight(luck1)
                elif map.curzone == map.zone[3]:
                        luck1 = random.choice(monsterlist3)
                        fight(luck1)
                elif map.curzone == map.zone[4]:
                        luck1 = random.choice(monsterlist4)
                        fight(luck1)
            else:
                print("\nNo monsters around")
            input("\nPress enter to continue")
        explore(map)
    elif option == "back":
        game()
    else:
        input("\nPlease input a valid command")
        explore(map)


def fight(monster):
    clear()
    print(f"You are fighting {monster.name}")
    print(f"{playerig.name}'s Health {playerig.hp}      {monster.name}'s Health {monster.hp}")
    print(f"{playerig.name}'s Health {playerig.mp}")
    print("\nAttack")
    print("Skills")
    print("Run")
    if playerig.hp <= 0:
        dead()
    elif monster.hp <= 0:
        reward(monster)
    else:
        option = input("\nWhat do you want to do?\n").lower()
        if option == "attack":
            monster.hp -= playerig.attack
            damagetook = random.randint(monster.minattack, monster.maxattack)
            playerig.hp -= damagetook
            input(f"You gave {playerig.attack} damage and took {damagetook} damage")
            fight(monster)
        elif option == "skills":
            skills()
            option1 = input('\nWhat skill do you want to use?\n').lower()
            if option1 == "twisting" or option1 == "ice storm":
                monster.hp -= useskill(option1)
                damagetook = random.randint(monster.minattack, monster.maxattack)
                playerig.hp -= damagetook
                input(f"You gave {useskill(option1)} damage and take {damagetook} damage")
                fight(monster)
            elif option1 == "regenerate":
                damagetook = random.randint(monster.minattack, monster.maxattack)
                playerig.hp -= damagetook
                input(f"You took {damagetook} damage and healed for {useskill(option1)} hp")
                fight(monster)
            else:
                input("Enter a valid skill name\n")
                fight(monster)
        elif option == "run":
            probability = random.randint(1, 2)
            if probability == 1:
                print("You ran away")
                input("Press enter to continue")
                explore(mappa)
            else:
                print("You couldn't run away")
                playerig.mp -= 5
                print("Your mana decrease by 5")
                monster.hp -= playerig.attack
                damagetook = random.randint(monster.minattack, monster.maxattack)
                playerig.hp -= damagetook
                input(f"You gave {damagetook} damage and took {monster.attack} damage")
                fight(monster)
        else:
            input("Enter a valid command\n")
            fight(monster)


def shop():
    print(f"Available items: {items.Great_Sword.name} and {items.Exe_Sword.name}")
    print("Buy")
    print("Back")
    option = input("What do you do: ").lower()
    if option == "back":
        game()
    elif option == "buy":
        option1 = input("What do you want to buy ?\n").lower()
        if option1 == "great sword":
            print("You bought the item")
            playerig.inventory.append(items.Great_Sword)
            game()
        elif option1 == "exe sword":
            print("You bought the item")
            playerig.inventory.append(items.Exe_Sword)
            game()
        else:
            print("Invalid input")
            game()


def inventory():
    clear()
    print("Inside the Inventory you have: ")
    c = 1
    for i in playerig.inventory:
        print(f"{c}.{i.name}")
        c += 1
    print(f"\nGold: {playerig.gold}")
    c = 1
    option = input("\nWrite back to go back else write wear to equip an item\n").lower()
    if option == "back":
        game()
    elif option == "wear":
        wearitem()
    else:
        inventory()


def wearitem():
    try:
        item = int(input("Write the number of the item you want to wear\n"))
        item -= 1
        if item in range(len(playerig.inventory)):
            if playerig.inventory[item].type == "Weapon":
                playerig.inventory.append(playerig.primary[0])
                playerig.primary.pop(0)
                print(f"You wore the item {playerig.inventory[item].name}")
                playerig.primary.append(playerig.inventory[item])
                playerig.inventory.pop(item)
                playerig.update()
                input("Press enter to continue")
                game()
            elif playerig.inventory[item].type == "Shield":
                playerig.inventory.append(playerig.secondary[0])
                playerig.secondary.pop(0)
                print(f"You wore the item {playerig.inventory[item].name}")
                playerig.secondary.append(playerig.inventory[item])
                playerig.inventory.pop(item)
                playerig.update()
                input("Press enter to continue")
                game()
            elif playerig.inventory[item].type == "Armor":
                playerig.inventory.append(playerig.armor[0])
                playerig.armor.pop(0)
                print(f"You wore the item {playerig.inventory[item].name}")
                playerig.armor.append(playerig.inventory[item])
                playerig.inventory.pop(item)
                playerig.update()
                input("Press enter to continue")
                inventory()
    except:
        input("Please chose a number from the inventory.")
        inventory()

def giveitem(item):
    playerig.inventory.append(item)


def character():
    clear()
    print(f"Available points {playerig.points}\n")
    print(f"Strength {playerig.str}")
    print(f"Agility {playerig.agy}")
    print(f"Vitality {playerig.vit}")
    print(f"Energy {playerig.ene}")
    print("\nTo add points write: Attribute press enter then chose the amount of points you want to add")
    print("Example:")
    print("Strength")
    print("3")
    print("----------------------------------------------------------------------------------------")
    print("To reset points write 'reset'")
    option = input("\nWhat do you want to do? Write back to go back.\n").lower()
    if option == "back":
        game()
    elif option == "strength" or option == "agility" or option == "vitality" or option == "energy":
        try:
            option1 = int(input("How many points you want to add ?"))
            if option1 <= playerig.points:
                playerig.points -= option1
                adder(option, option1)
            else:
                input("Not enough available points")
                character()
        except:
                input("Invalid amount of points")
                character()
    elif option == "reset":
        resetPoints()
    else:
        input("Invalid choice")
        character()


def skills():
    print(f"--Twisting-- Damage: {items.Twisting.damage}, Mana cost: {items.Twisting.manacost}, Description: {items.Twisting.description}, Level: {items.Twisting.lvl}")
    print(f"--Ice Storm-- Damage: {items.Ice_Storm.damage}, Mana cost: {items.Ice_Storm.manacost}, Description: {items.Ice_Storm.description}, Level: {items.Ice_Storm.lvl}")
    print(f"--Regenerate-- Damage: {items.Regenerate.damage}, Mana cost: {items.Regenerate.manacost}, Description: {items.Regenerate.description}, Level: {items.Regenerate.lvl}")


def skillupgrade():
    clear()
    skills()
    try:
        print(f"\nAvailable attribute points: {playerig.attributepoints}")
        option = input("\nWhat skill do you wanna upgrade? Or write back to go back\n").lower()
        if option == "twisting" and playerig.attributepoints > 0:
            items.Twisting.lvl += 1
            playerig.attributepoints -= 1
            items.Twisting.damage += 3
            items.Twisting.manacost += 3
            input(f"--Twisting-- Damage: {items.Twisting.damage}, Mana cost: {items.Twisting.manacost}, Description: {items.Twisting.description}, Level: {items.Twisting.lvl}")
            clear()
            skills()
        elif option == "ice storm" and playerig.attributepoints > 0:
            items.Ice_Storm.lvl += 1
            playerig.attributepoints -= 1
            items.Ice_Storm.damage += 4
            items.Ice_Storm.manacost += 8
            input(f"--Ice Storm-- Damage: {items.Ice_Storm.damage}, Mana cost: {items.Ice_Storm.manacost}, Description: {items.Ice_Storm.description}, Level: {items.Ice_Storm.lvl}")
            clear()
            skills()
        elif option == "Regenerate" and playerig.attributepoints > 0:
            items.Regenerate.lvl += 1
            playerig.attributepoints -= 1
            items.Regenerate.damage += 10
            items.Regenerate.manacost += 10
            input(f"--Regenerate-- Damage: {items.Regenerate.damage}, Mana cost: {items.Regenerate.manacost}, Description: {items.Regenerate.description}, Level: {items.Regenerate.lvl}")
            clear()
            skills()
        elif option == "back":
            game()
        else:
            input("Invalid command\n")
            skillupgrade()
    except:
        input("No skill with this name")
        skillupgrade()


def useskill(option):
    if option == "twisting":
        playerig.mp -= items.Twisting.manacost
        return items.Twisting.damage
    elif option == "ice storm":
        playerig.mp -= items.Ice_Storm.manacost
        return items.Ice_Storm.damage
    elif option == "regenerate":
        curhp = playerig.maxhp - playerig.hp
        playerig.mp -= items.Regenerate.manacost
        playerig.hp += items.Regenerate.damage
        if playerig.hp >= playerig.maxhp:
            playerig.hp = playerig.maxhp
            return curhp
        else:
            return items.Regenerate.damage
    else:
        input("Chose a valid skill")


def adder(option, option1):
    if option == "strength":
        playerig.str += option1
        input(f"You added {option1} points to {option}")
    elif option == "agility":
        playerig.agy += option1
        input(f"You added {option1} points to {option}")
    elif option == "stamina":
        playerig.vit += option1
        input(f"You added {option1} points to {option}")
    elif option == "energy":
        playerig.ene += option1
        input(f"You added {option1} points to {option}")
    playerig.update()
    character()


def reward(monster):
    print(f"\n{monster.name} died , you earn {monster.givegold} gold")
    playerig.gold += monster.givegold
    playerig.exp += monster.giveexp
    monster.hp = monster.maxhp
    if playerig.exp >= playerig.exptolvl:
        playerig.lvl += 1
        playerig.points += 5
        playerig.exptolvl = playerig.lvl * 2.5
        print(f"\nYou leveled up, you are level: {playerig.lvl}")
        print(f"You gained 5 points")
        print(f"You gained 2 attribute points\n")
    if monster.lvl == 1 or monster.lvl == 2:
        luck = random.randint(1, 2)
        if luck == 1:
            choice = random.choice(items.rewardbox)
            playerig.inventory.append(choice)
            print(f"You found {choice.name}")
    elif monster.lvl == 3 or monster.lvl == 4:
        luck = random.randint(1, 2)
        if luck == 1:
            choice = random.choice(items.rewardbox2)
            playerig.inventory.append(choice)
            print(f"You found {choice.name}")
    elif monster.lvl == 5 or monster.lvl == 6:
        luck = random.randint(1, 2)
        if luck == 1:
            choice = random.choice(items.rewardbox3)
            playerig.inventory.append(choice)
            print(f"You found {choice.name}")
    elif monster.lvl == 6:
        luck = random.randint(1, 2)
        if luck == 1:
            choice = random.choice(items.rewardbox4)
            playerig.inventory.append(choice)
            print(f"You found {choice.name}")
    elif monster.lvl == 7:
        luck = random.randint(1, 2)
        if luck == 1:
            choice = random.choice(items.rewardbox5)
            playerig.inventory.append(choice)
            print(f"You found {choice.name}")
    else:
        print(f"{monster.name} didn't dropped anything")
    input("\nPress enter to continue")
    explore(mappa)

def harald():
    clear()
    print("Inside the Inventory you have: ")
    c = 1
    for i in playerig.inventory:
        print(f"{c}.{i.name}")
        c += 1
    print(f"\nGold: {playerig.gold}")
    c = 1
    option = input("\nWrite back to go back else write sell to sell a item or recharge to heal/mana\n").lower()
    if option == "back":
        game()
    elif option == "sell":
        sellItem()
    elif option == "recharge":
        recharge()
    else:
        harald()


def recharge():
    clear()
    option = input("What do you want to recharge ? Health or Mana? back to go back\n").lower()
    if option == "health":
        if playerig.gold > 10:
            playerig.gold -= 10
            playerig.hp += playerig.maxhp
            if playerig.hp > playerig.maxhp:
                playerig.hp = playerig.maxhp
            input("Health refiled")
            game()
        else:
            input("Insufficient gold")
            game()
    elif option == "mana":
        if playerig.gold > 10:
            playerig.gold -= 10
            playerig.mp += playerig.maxmp
            if playerig.mp > playerig.maxmp:
                playerig.mp = playerig.maxmp
            input("Mana refiled")
            game()
        else:
            input("Insufficient gold")
            game()
    elif option == "back":
        game()
    else:
        input("Invalid command")
        game()

def sellItem():
    try:
        item = int(input("Write the number of the item you want to sell\n"))
        item -= 1
        if item in range(len(playerig.inventory)):
            playerig.gold += playerig.inventory[item].price
            print(f"You sold the item {playerig.inventory[item].name}")
            playerig.inventory.pop(item)
            input("Press enter to continue")
            harald()
    except:
        input("Please chose a number from the inventory.")
        inventory()


def dead():
    playerig.hp = playerig.maxhp
    playerig.mp = playerig.maxmp
    print("You died")
    print("...")
    input("Press enter enter to continue")
    game()

def resetPoints():
    option = input("Are you sure you want to reset all your points ? Yes or No?\n").lower()
    if option == "yes":
        if playerig.gold >= 100:
            playerig.gold -= 100
            playerig.points += (playerig.str + playerig.agy + playerig.vit + playerig.ene)-4
            playerig.str -= (playerig.str - 1)
            playerig.agy -= (playerig.agy - 1)
            playerig.vit -= (playerig.vit - 1)
            playerig.ene -= (playerig.ene - 1)
            input("You reset your points")
            clear()
            character()
        else:
            input("Insufficient gold, you need 100 gold")
            game()
    elif option == "no":
        input("You didn't reset your points")
        game()
    else:
        input("Please enter a valid command")
        resetPoints()


def savegame():
    with open("savegame.b", "wb") as save:
        pickle.dump(playerig, save)
        input(f"You saved your current status")
    game()


def loadgame():
    try:
        with open("savegame.b", "rb") as save:
            playerig = pickle.load(save)
            load(playerig)
    except:
        input("There is no saved game in the directory")
        main()


def clear():
    os.system('cls')


main()