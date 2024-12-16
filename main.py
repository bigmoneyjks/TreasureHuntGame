import random

class Player:
    def __init__(self):
        self.hp = 100
        self.stun = False
        self.inv = []
        self.loc = "Doctor's House"
        self.ess = 0
        
    def pickup(self, item):
        if len(self.inv) < 8:
            (self.inv).append(item)
        else:
            print(f"You cannot fit {item.name} into your rucksack")
    
    def drop(self, item):
        print(f"You drop {item.name} onto the floor and watch as it is consumed by the ground beneath you")
        (self.inv).pop(item)

    
    def heal(self, inventory):
        if "Spiral" in inventory:
            self.hp += random.randint(10,40)
        else:
            print("You realise that you don't have a Spiral")
    
    def attack(self, enemy, weapon):
        if weapon not in self.inv:
            print(f"You rummaged through your rucksack looking for {weapon.name} but could not find it")
            return
        if self.stun:
            print(f"You try to lift your {weapon.name} but it's weight seeminlgy doubled")
            return
        if enemy.dead:
            print("")
            return

        weapon.attackent(enemy)

    def inspect(self):
        print(f"You have {self.hp} health points remaining...")
    
    def move(self, location):
        self.loc = location

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
            print(f"You open your rucksack lookinh for a Repair Kit but realise you never had one in the first place")
        
    def attackent(self, enemy):
        self.dur -= self.durusage
        enemy.hp -= random.randint(self.dmgLower, self.dmgUpper)
        print(self.message(enemy))

class Ghoul:
    def __init__(self):
        self.name = "Ghoul"
        self.hp = 15
        self.dmg = 18
        self.dead = False
    
    def attack(self, player):
        super = random.randint(1,10)
        if super == 1:
            print(f"The {self.name} burrowed its claws deep into your skin")
            player.hp -= (self.dmg + 5)
        else:
            print(f"The {self.name} swung it's spindly arm at you and scratched you")
            player.hp -= self.dmg
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 4
            print(f"You can hear a tinny screech come from the {self.name} before it's body stops jittering")
        else:
            pass

class Chomper:
    def __init__(self):
        self.name = "Chomper"
        self.hp = 20
        self.dmg = 20
        self.dead = False
    
    def attack(self, player):
        super = random.randint(1,10)
        if super == 1:
            print(f"The {self.name} dug it's rotten jaw into your arm")
            player.hp -= (self.dmg + 5)
        else:
            print(f"The {self.name} bit down onto your leg")
            player.hp -= self.dmg
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 6
            print(f"You see the {self.name} writhe on the dirty foresty mushrooms")
        else:
            pass

class Bats:
    def __init__(self):
        self.name = "Bats"
        self.dmg = 1
        self.hp = 5
        self.dead = False
        self.num = random.randint(1,3)
    
    def attack(self, player):
        print(f"The {self.name} claw at your skin")
        player.hp -= self.dmg
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.num -= 1
            player.ess += 2
            if self.num == 0:
                self.dead = True
                print(f"You watch the {self.name} fall to the ground as they lay there")
        else:
            pass

class Villager:
    def __init__(self):
        self.name = "Mutated Villager"
        self.hp = 18
        self.dmg = 15
        self.dead = False
    
    def attack(self, player):
        super = random.randint(1,10)
        if super == 1:
            player.hp -= (self.dmg*2)
            print(f"The {self.name} rushes you and smashes his arms into your head")
        else:
            player.hp -= self.dmg
            print(f"The {self.name} screamed deafeningly whilst throwing his arm at you")
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 6
            print(f"You watch the {self.name}'s body fall to the floor")
        else:
            pass
                
class Banshee:
    def __init__(self):
        self.name = "Banshee"
        self.hp = 18
        self.dmg = 10
        self.dead = False
    
    def attack(self, player):
        super = random.randint(1,10)
        if super == 1:
            player.stun = True
            print(f"The deafening screech from the {self.name} disorientates you as you fall to the ground")
            print(f"The {self.name} jumps on top of you and claws at your chest vigorously")
            player.hp -= self.dmg
        else:
            print(f"The {self.name} stabs your arm and holes remain where it attacked")
            player.hp -= self.dmg

player = Player()

Tokarev = Weapon("Tokarev", (45,60), 20, 1, (6,11), lambda enemy: f"You shot {enemy.name}")
KS = Weapon("KS-23", (30,35), 20, 1, (12,20), lambda enemy: f"You blast a hole through {enemy.name}")
Axe = Weapon("Axe", (70,87), 20, 1, (3,8), lambda enemy: f"You hurl the Axe at {enemy.name} and slash it")
Shovel = Weapon("Shovel", , 20, 1, (6,10), lambda enemy: f"You smash {enemy.name} over the head with your Shovel")

ghoul = Ghoul()
player.pickup(Tokarev)
player.attack(ghoul, Tokarev)
print(ghoul.hp)

