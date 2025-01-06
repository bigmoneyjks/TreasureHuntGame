import random

class Weapon:
    def __init__(self, name, durBounds, maxdurability, durusage, dmgBounds, msgFunction):
        self.name = name
        self.dur = random.randint(durBounds[0], durBounds[1])
        self.maxdur = maxdurability
        self.durusage = durusage
        self.dmgLower, self.dmgUpper = dmgBounds
        self.message = msgFunction
    
    def inspect(self):
        print(f"You inspect your weapon and believe it has {self.dur} uses left in it")
    
    def repair(self, player):
        if "Repair Kit" in player.inv:
            self.dur = self.maxdur
        else:
            print(f"You open your rucksack looking for a Repair Kit but realise you never had one in the first place")
        
    def attackent(self, enemy):
        self.dur -= self.durusage
        enemy.hp -= random.randint(self.dmgLower, self.dmgUpper)
        print(self.message(enemy))

class Heals:
    def __init__(self, name, healamount, msgFunction):
        self.name = name
        self.heal = healamount
        self.msg = msgFunction

    def use(self, player):
        print(self.msg)
        player.hp += self.heal