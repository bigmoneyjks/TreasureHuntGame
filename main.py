import random

class Player:
    def __init__(self):
        self.hp = 100
        self.stun = False
        self.inv = ["KS-23"]
        
    def pickup(self, item):
        if len(self.inv) != 8:
            (self.inv).append(item)
        else:
            print(f"You cannot fit {item.name} into your rucksack")
    
    def heal(self, inventory):
        if "Spiral" in inventory:
            self.hp += random.randint(10,40)

        else:
            print("You realise that you don't have a Spiral")
    
    def attack(self, enemy, weapon):
        if weapon.name == "Tokarev" and weapon.name in self.inv and self.stun == False and enemy.dead == False:
            print(f"You shot {enemy.name}")
            enemy.hp -= random.randint(6, 11)
            weapon.dur -= 1
        elif weapon.name == "KS-23" and weapon.name in self.inv and self.stun == False and enemy.dead == False:
            damage = random.randint(12,20)
            if damage >= 17:
                print(f"You blast a hole through {enemy.name}")
                weapon.dur -= 2
            else:
                print(f"You shot {enemy.name}")
        elif weapon.name == "Ruined Axe" and weapon.name in self.inv and self.stun == False and enemy.dead == True:
            print(f"You hurl the {weapon.name} at the {enemy.name} and slash it")
            enemy.hp -= random.randint(3, 8)
        elif weapon.name == "Shiny Shovel" 

    def move(self, location):
        pass

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
            player.hp -= self.damage
    
    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"You can hear a tinny screech come from the {self.name} before it's body stops jittering")
        else:
            pass

class Chomper:
    def __init__(self):
        self.hp = 20