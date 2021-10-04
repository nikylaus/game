maps = [["Lorencia", "Lorencia is 1 of the oldest map of the ancient", True, True, [["Lorencia's safe zone"], ["Lorencia Woods"], ["Lorencia Sanctuary"], ["Lorencia Dungeon"], ["Lorencia Boss"]]]]


class Map:
    def __init__(self, name, desc, loot, fight, zone):
        self.name = name
        self.desc = desc
        self.loot = loot
        self.fight = fight
        self.zone = zone
        self.curzone = self.zone[0]
        self.count = 0
        self.walking = 0


mappa = Map(maps[0][0], maps[0][1], maps[0][2], maps[0][3], maps[0][4])