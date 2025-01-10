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
            print(f"You patch up your {self.name}")
            (player.inv).remove("Repair Kit")
        else:
            print(f"You open your rucksack looking for a Repair Kit but realise you never had one in the first place")
        
    def use(self, enemy):
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

class Armour:
    def __init__(self, name, hpincrease):
        self.name = name
        self.increase = hpincrease
    
    def wear(self, player):
        if len(player.armour) <=3:
            print(f"You put on {self.name}")
            player.maxhp += self.increase
        else:
            print("You realise that it will be too heavy to put on")
        
class HealArtifact:
    def __init__(self, heal):
        self.name = "Soul"
        self.heal = heal

    def use(self, player):
        print("You feel an immense pulsing from the artifact couring through your hand")
        player.hp += self.heal

class DmgArtifact:
    def __init__(self, dmgDone):
        self.name = "Mica"
        self.dmg = dmgDone
    
    def use(self, enemy):
        print(f"An incredibly bright flash of light almost blinds you as it strikes the {enemy.name}")
        enemy.hp -= self.dmg