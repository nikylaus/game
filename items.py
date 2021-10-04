import random
empty = [["Empty", 0, 0]]
primarys = [["Wood Sword", 2, 3, "Weapon"], ["Great Sword", 12, 9, "Weapon"], ["Exe Sword", 22, 14, "Weapon"], ["Dragon Sword", 45, 23, "Weapon"], ["Dragon Knight Sword", 50, 30, "Weapon"]]
secondarys = [["Wood Shield", 2, 3, "Shield"], ["Great Shield", 13, 11, "Shield"], ["Exe Shield", 23, 15, "Shield"], ["Dragon Shield", 50, 21, "Shield"], ["Dragon Knight Shield", 53, 28, "Shield"]]
armors = [["Wood Armor", 2, 3, "Armor"], ["Great Armor", 9, 6, "Armor"], ["Exe Armor", 21, 10, "Armor"], ["Dragon Armor", 48, 14, "Armor"], ["Dragon Knight Armor", 54, 22, "Armor"]]


skills = [["Twisting", 25, 10, "Turn around in a circular motion and deal damage all around you", "Attack", 1], ["Regenerate", 25, 10, "You regenerate some health", "Regen", 1], ["Ice Storm", 25, 10, "You start a small Ice Storm", "Attack", 1]]
monsters = [["Spider", 1, 30, 8, 13, 15], ["Huge Spider", 2, 45, 10, 15, 20], ["Baby Dragon", 2, 50, 12, 15, 20], ["Goblin", 3, 45, 15, 19, 25], ["Stone Goblin", 4, 55, 20, 26, 27], ["Cyclop", 5, 70, 30, 36, 33], ["Great Dragon", 6, 100, 40, 43, 40], ["Golden Dragon", 7, 200, 50, 100, 65]]


class Items:
    def __init__(self, name, price, attack, type):
        self.name = name
        self.price = price
        self.attack = attack
        self.type = type


class Skill:
    def __init__(self, name, damage, manacost, description, type, lvl):
        self.name = name
        self.damage = damage
        self.manacost = manacost
        self.description = description
        self.type = type
        self.lvl = lvl


class Monster:
    def __init__(self, name, lvl, maxhp, minattack, maxattack, defense):
        self.name = name
        self.lvl = lvl
        self.maxhp = maxhp
        self.hp = self.maxhp
        self.minattack = minattack
        self.maxattack = maxattack
        self.defense = defense
        self.givegold = random.randint(1, 4) * self.lvl
        self.giveexp = lvl * 1.5


Wood_Sword = Items(primarys[0][0], primarys[0][1], primarys[0][2], primarys[0][3])
Great_Sword = Items(primarys[1][0], primarys[1][1], primarys[1][2], primarys[1][3])
Exe_Sword = Items(primarys[2][0], primarys[2][1], primarys[2][2], primarys[2][3])
Dragon_Sword = Items(primarys[3][0], primarys[3][1], primarys[3][2], primarys[3][3])
Dragon_Knight_Sword = Items(primarys[4][0], primarys[4][1], primarys[4][2], primarys[4][3])

Wood_Shield = Items(secondarys[0][0], secondarys[0][1], secondarys[0][2], secondarys[0][3])
Great_Shield = Items(secondarys[1][0], secondarys[1][1], secondarys[1][2], secondarys[1][3])
Exe_Shield = Items(secondarys[2][0], secondarys[2][1], secondarys[2][2], secondarys[2][3])
Dragon_Shield = Items(secondarys[3][0], secondarys[3][1], secondarys[3][2], secondarys[3][3])
Dragon_Knight_Shield = Items(secondarys[4][0], secondarys[4][1], secondarys[4][2], secondarys[4][3])

Wood_Armor = Items(armors[0][0], armors[0][1], armors[0][2], armors[0][3])
Great_Armor = Items(armors[1][0], armors[1][1], armors[1][2], armors[1][3])
Exe_Armor = Items(armors[2][0], armors[2][1], armors[2][2], armors[2][3])
Dragon_Armor = Items(armors[3][0], armors[3][1], armors[3][2], armors[3][3])
Dragon_Knight_Armor = Items(armors[4][0], armors[4][1], armors[4][2], armors[4][3])

rewardbox = [Wood_Sword, Great_Sword, Wood_Shield, Great_Shield,  Wood_Armor, Great_Armor]
rewardbox2 = [Great_Sword, Exe_Sword, Great_Shield, Exe_Shield, Great_Armor, Exe_Armor]
rewardbox3 = [Exe_Sword, Dragon_Sword,Exe_Shield, Dragon_Shield,Exe_Armor, Dragon_Armor]
rewardbox4 = [Dragon_Sword, Dragon_Knight_Sword, Dragon_Shield, Dragon_Knight_Shield, Dragon_Armor, Dragon_Knight_Armor]
rewardbox5 = [Dragon_Knight_Sword, Dragon_Knight_Shield, Dragon_Knight_Armor]

Twisting = Skill(skills[0][0], skills[0][1], skills[0][2], skills[0][3], skills[0][4], skills[0][5])
Regenerate = Skill(skills[1][0], skills[1][1], skills[1][2], skills[1][3], skills[1][4], skills[0][5])
Ice_Storm = Skill(skills[2][0], skills[2][1], skills[2][2], skills[2][3], skills[2][4], skills[0][5])


Spider = Monster(monsters[0][0],monsters[0][1],monsters[0][2],monsters[0][3],monsters[0][4],monsters[0][5])
Huge_Spider = Monster(monsters[1][0],monsters[1][1],monsters[1][2],monsters[1][3],monsters[1][4],monsters[1][5])
Baby_Dragon = Monster(monsters[2][0],monsters[2][1],monsters[2][2],monsters[2][3],monsters[2][4],monsters[2][5])
Goblin = Monster(monsters[3][0],monsters[3][1],monsters[3][2],monsters[3][3],monsters[3][4],monsters[3][5])
Stone_Goblin = Monster(monsters[4][0],monsters[4][1],monsters[4][2],monsters[4][3],monsters[4][4],monsters[0][5])
Cyclop = Monster(monsters[5][0],monsters[5][1],monsters[5][2],monsters[5][3],monsters[5][4],monsters[5][5])
Great_Dragon = Monster(monsters[6][0],monsters[6][1],monsters[6][2],monsters[6][3],monsters[6][4],monsters[6][5])
Golden_Dragon = Monster(monsters[7][0],monsters[7][1],monsters[7][2],monsters[7][3],monsters[7][4],monsters[7][5])