import random

class Player:
    def __init__(self):
        self.hp = 100
        self.stun = False
        self.inv = ["KS-23"]
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
        if self.stun == False and enemy.dead == False and weapon.name in self.inv:
            if weapon.name == "Tokarev":
                print(f"You shot {enemy.name}")
                enemy.hp -= random.randint(6, 11)
                weapon.dur -= 1
            elif weapon.name == "KS-23":
                damage = random.randint(12,20)
                if damage >= 17:
                    print(f"You blast a hole through {enemy.name}")
                    weapon.dur -= 2
                else:
                    print(f"You shot {enemy.name}")
            elif weapon.name == "Axe":
                print(f"You hurl the {weapon.name} at the {enemy.name} and slash it")
                enemy.hp -= random.randint(3, 8)
            elif weapon.name == "Shovel":
                print(f"You smash {enemy.name} over the head with {weapon.name}")
                enemy.hp -= random.randint(6,10)
        if self.stun == True:
            print(f"You try to lift your {weapon.name} but it's weight seeminlgy doubled")
        else:
            print(f"You rummaged through your rucksack looking for {weapon.name} but could not find it")

    def inspect(self):
        print(f"You have {self.hp} health points remaining...")
    
    def move(self, location):
        self.loc = location

class Weapon:
    def __init__(self, name, durability, maxdurability):
        self.name = name
        self.dur = durability
        self.maxdur = maxdurability
    
    def inspect(self):
        print(f"You inspect your weapon and believe it has {self.dur} uses left in it")
    
    def repair(self, player):
        if "Repair Kit" in player.inv:
            self.dur = self.maxdur
        else:
            print(f"You open your rucksack lookinh for a Repair Kit but realise you never had one in the first place")

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
player.drop()