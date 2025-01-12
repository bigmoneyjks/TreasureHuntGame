import random

class Player:
    def __init__(self):
        self.maxhp = 85
        self.hp = 85
        self.stun = False
        self.weapons = {}
        self.heals = {}
        self.armour = []
        self.keys = {}
        self.ess = 0
        self.loc = ""
        self.dead = False
        
    def pickup(self, item):
        if len(self.weapons) <= 4:
            self.weapons[(item.name).lower()] = item
        else:
            print(f"You cannot fit {item.name} into your rucksack")

    def heal(self, item):
        if item in self.heals.items():
            item.use()
    
    def wear(self, armour):
        armour.wear(self)
    
    def attack(self, enemy, weapon):
        if weapon not in self.weapons.values():
            print(f"You rummaged through your rucksack looking for {weapon.name} but could not find it")
            return
        if self.stun:
            print(f"You try to lift your {weapon.name} but it's weight seeminlgy doubled")
            self.stun = False
            return
        if enemy.dead:
            print(f"You stare at {enemy.name}'s lifeless body")
            return

        weapon.use(enemy)
    
    def fight(self, enemy):
        while not enemy.dead or not self.dead:
            for weapon in self.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = self.weapons.get(choice)
            self.attack(enemy, weapon)
            print(f"The {enemy.name} has {enemy.hp} health left")
            enemy.attack(self)
            print(f"You have {self.hp} health left")
            self.checkdead()
            enemy.checkdead()
        self.ess += enemy.ess

    def inspect(self):
        print(f"You have {self.hp} health points remaining...")

    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print("You feel the forest consume you into the ground")

class Ghoul:
    def __init__(self):
        self.name = "Ghoul"
        self.hp = 15
        self.dmg = 18
        self.dead = False
        self.ess = 4
    
    def attack(self, player):
        super = random.randint(1,10)
        if super == 1:
            print(f"The {self.name} burrowed its claws deep into your skin")
            player.hp -= (self.dmg + 5)
        else:
            print(f"The {self.name} swung it's spindly arm at you and scratched you")
            player.hp -= self.dmg
    
    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"You can hear a tinny screech come from the {self.name} before it's body stops jittering")

class Chomper:
    def __init__(self):
        self.name = "Chomper"
        self.hp = 20
        self.dmg = 20
        self.dead = False
        self.ess = 6
    
    def attack(self, player):
        super = random.randint(1,10)
        if super == 1:
            print(f"The {self.name} dug it's rotten jaw into your arm")
            player.hp -= (self.dmg + 5)
        else:
            print(f"The {self.name} bit down onto your leg")
            player.hp -= self.dmg
    
    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"You see the {self.name} writhe on the dirty foresty mushrooms")

class Bats:
    def __init__(self):
        self.name = "Bats"
        self.dmg = 1
        self.hp = 5
        self.dead = False
        self.num = random.randint(1,3)
        self.ess = 2
    
    def attack(self, player):
        print(f"The {self.name} claw at your skin")
        player.hp -= self.dmg

    def checkdead(self):
        if self.hp <= 0:
            self.num -= 1
            if self.num == 0:
                self.dead = True
                print(f"You watch the {self.name} fall to the ground as they lay there")

class Villager:
    def __init__(self):
        self.name = "Mutated Villager"
        self.hp = 18
        self.dmg = 15
        self.dead = False
        self.ess = 6
    
    def attack(self, player):
        super = random.randint(1,10)
        if super == 1:
            player.hp -= (self.dmg*2)
            print(f"The {self.name} rushes you and smashes his arms into your head")
        else:
            player.hp -= self.dmg
            print(f"The {self.name} screamed deafeningly whilst throwing his arm at you")
    
    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"You watch the {self.name}'s body fall to the floor")
                
class Banshee:
    def __init__(self):
        self.name = "Banshee"
        self.hp = 18
        self.dmg = 10
        self.dead = False
        self.ess = 8
    
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
    
    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"The {self.name}'s body quivers before lying still")

class Stalker:
    def __init__(self):
        self.name = "Stalker"
        self.hp = 32
        self.dmg = 20
        self.dead = False
        self.ess = 10
    
    def attack(self, player):
        print(f"The {self.name} takes their Makarov and unloads a round into you")
        player.hp -= self.dmg
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 10
            print(f"You see The {self.name}'s try to stand back up but they eventually die")
        chance = random.randint(1,10)
        if chance == 1:
            if len(player.inv) <= 1:
                print(f"You notice that The {self.name} had a Repair Kit on them")
            else:
                print(f"You see a repair kit in The {self.name}'s bag but realise that you cannot fit it into your rucksack")

class Wanderer:
    def __init__(self):
        self.name = "Wanderer"
        self.hp = 25
        self.dmg = 12
        self.dead = False
        self.ess = 2
    
    def attack(self, player):
        chance = random.randint(1,10)
        if chance <= 3:
            print(f"The {self.name}'s shiv causes your blood to gush out of you")
            player.hp -= self.dmg + 5
        else:
            print(f"The {self.name} raises their shiv and slash you on your cheek")
            player.hp -= self.dmg
    
    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"The {self.name} tries to give one final blow before falling to the floor")

class Wolfmann:
    def __init__(self):
        self.name = "Wolfmann"
        self.hp = 65
        self.lunge = 20
        self.claw = 12
        self.dead = False
        self.ess = 15
    
    def attack(self, player):
        which = random.randint(1,10)
        if which <= 3:
            player.hp -= self.lunge
            print(f"The {self.name} lunges at you")
        else:
            player.hp -= self.claw
            print(f"The {self.name}'s claws leave a scar on your arm")
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            print(f"You watch as The {self.name} drops dead onto the ground")
            print(f"You decide to pickup his trenchcoat and feel the immense weight of it on you")
            player.maxhp += random.ranndint(5,12)

class Captain:
    def __init__(self):
        self.name = "Captain"
        self.hp = 70
        self.shoot = 20
        self.stab = 15
        self.dead = False
        self.ess = 15
    
    def attack(self, player):
        which = random.randint(1,10)
        if which <= 4:
            player.hp -= self.shoot
            print(f"A sharp pain hits your chest")
        else:
            player.hp -= self.stab
            print(f"The {self.name} takes his knife and sinks it deep into your thigh")

    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"Your final blow takes The {self.name} down")
            print(f"He hands you his Tokarev pistol as a sign of respect you believe")

class Leader:
    def __init__(self):
        self.name = "Village Leader"
        self.hp = 75
        self.shovel = 23
        self.spit = 10
        self.dead = False
        self.ess = 20
    
    def attack(self, player):
        which = random.randint(1,10)
        if which <= 5:
            player.hp -= self.spit
            print(f"You wipe off a gross liquid from your face")
        else:
            player.hp -= self.stab
            print(f"A shovel is whacked over your head by The {self.name}")
    
    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"You watch as The {self.name} drops their shovel onto the ground and slump over")
            print(f"You see that his shovel is still intact and decide to take it")

class Doctor:
    def __init__(self):
        self.name = "Doctor"
        self.hp = 60
        self.slash = 14
        self.acid = 25
        self.dead = False
        self.ess = 0
    
    def attack(self, player):
        which = random.randint(1,10)
        heal = random.randint(1,10)
        if which <= 3:
            player.hp -= self.acid
            print(f"The {self.name} smashes a vial of bubbling acid onto your face")
        else:
            player.hp -= self.slash
            print(f"You feel the {self.name}'s scalpel slash into your cheek")
        if heal <= 1:
            self.hp += 20
            print(f"The {self.name} takes out a bubbling vial and drinks whatever is inside")
        
    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"You watch as The {self.name} finally drops dead to the floor")
        
class Amalgamation:
    def __init__(self):
        self.name = "Amalgamation"
        self.hp = 120
        self.chomp = 30
        self.sweep = 15
        self.dead = False
        self.ess = 0
    
    def attack(self, player):
        which = random.randint(1,10)
        stunned = random.randint(1,10)
        if which >= 7:
            player.hp -= self.chomp
            print(f"The {self.name} launches a chomper towards you")
            if stunned >= 4:
                print(f"The chomper managed to immobilise your leg *stunned*")
                player.stun = True
        else:
            player.hp -= self.slash
            print(f"You feel the {self.name}'s whip of the branch")
    
    def checkdead(self):
        if self.hp <= 0:
            self.dead = True
            print(f"You watch as The {self.name} begins to combust at no reason")

    