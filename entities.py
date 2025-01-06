import random

class Player:
    def __init__(self):
        self.maxhp = 85
        self.hp = 85
        self.stun = False
        self.weapons = {}
        self.armour = []
        self.ess = 0
        self.loc = []
        
    def pickup(self, item):
        if len(self.weapons) <= 7:
            self.weapons[item.name.lower()] = item
        else:
            print(f"You cannot fit {item.name} into your rucksack")
    
    def drop(self, item):
        print(f"You drop {item.name} onto the floor and watch as it is consumed by the ground beneath you")
        (self.inv).pop(item)

    def heal(self, inventory, item):
        if item in inventory:
            self.hp += item.use(self)
        else:
            print(f"You realise that you don't have {item.name}")
    
    def wear(self, armour):
        armour.wear(self)
    
    def attack(self, enemy, weapon):
        if weapon not in self.inv:
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

    def inspect(self):
        print(f"You have {self.hp} health points remaining...")
    
    def move(self, where):
        self.loc = where.name


    
    # def move(self, location):
    #     self.loc = location

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
        
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 4
            print(f"You can hear a tinny screech come from the {self.name} before it's body stops jittering")

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
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 6
            print(f"You see the {self.name} writhe on the dirty foresty mushrooms")

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
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)

    def checkdead(self, player):
        if self.hp <= 0:
            self.num -= 1
            player.ess += 2
            if self.num == 0:
                self.dead = True
                print(f"You watch the {self.name} fall to the ground as they lay there")

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
        
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 6
            print(f"You watch the {self.name}'s body fall to the floor")
                
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
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 8
            print(f"The {self.name}'s body quivers before lying still")

class Stalker:
    def __init__(self):
        self.name = "Stalker"
        self.hp = 32
        self.dmg = 20
        self.dead = False
    
    def attack(self, player):
        print(f"The {self.name} takes their Makarov and unloads a round into you")
        player.hp -= self.dmg
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 10
            print(f"You see The {self.name}'s try to stand back up but they eventually die")
        chance = random.randint(1,10)
        if chance == 1:
            if len(player.inv) <= 7:
                print(f"You notice that The {self.name} had a Repair Kit on them")
            else:
                print(f"You see a repair kit in The {self.name}'s bag but realise that you cannot fit it into your rucksack")

class Wanderer:
    def __init__(self):
        self.name = "Wanderer"
        self.hp = 25
        self.dmg = 12
        self.dead = False
    
    def attack(self, player):
        chance = random.randint(1,10)
        print(f"The {self.name} raises their shiv and slash you on your cheek")
        player.hp -= self.dmg
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            player.ess += 8
            print(f"The {self.name} tries to give one final blow before falling to the floor")

class Wolfmann:
    def __init__(self):
        self.name = "Wolfmann"
        self.hp = 65
        self.lunge = 20
        self.claw = 12
        self.dead = False
    
    def attack(self, player):
        which = random.randint(1,10)
        if which <= 3:
            player.hp -= self.lunge
            print(f"You feel The {self.name}'s claws dig deep into your body")
        else:
            player.hp -= self.claw
            print(f"The {self.name}'s claws leave a scar on your arm")
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            print(f"You watch as The {self.name} drops dead onto the ground")
            print(f"You decide to pickup his trenchcoat and feel the immense weight of it on you")
            player.maxhp += random.ranndint(5,12)
            player.ess += 15

class Captain:
    def __init__(self):
        self.name = "Captain"
        self.hp = 70
        self.shoot = 20
        self.stab = 15
        self.dead = False
    
    def attack(self, player):
        which = random.randint(1,10)
        if which <= 4:
            player.hp -= self.shoot
            print(f"A sharp pain hits your chest")
        else:
            player.hp -= self.stab
            print(f"The {self.name} takes his knife and sinks it deep into your thigh")
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def checkdead(self, player, tokarev):
        if self.hp <= 0:
            self.dead = True
            print(f"Your final blow takes The {self.name} down")
            print(f"He hands you his Tokarev pistol as a sign of respect you believe")
            (player.inv).append(tokarev)
            player.ess += 15

class Leader:
    def __init__(self):
        self.name = "Village Leader"
        self.hp = 75
        self.shovel = 23
        self.spit = 10
        self.dead = False
    
    def attack(self, player):
        which = random.randint(1,10)
        if which <= 5:
            player.hp -= self.spit
            print(f"You wipe off a gross liquid from your face")
        else:
            player.hp -= self.stab
            print(f"A shovel is whacked over your head by The {self.name}")
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def checkdead(self, player, shovel):
        if self.hp <= 0:
            self.dead = True
            print(f"You watch as The {self.name} drops their shovel onto the ground and slump over")
            print(f"You see that his shovel is still intact and decide to take it")
            (player.inv).append(shovel)
            player.ess += 20

class Doctor:
    def __init__(self):
        self.name = "Doctor"
        self.hp = 60
        self.slash = 14
        self.acid = 25
        self.dead = False
    
    def attack(self, player):
        which = random.randint(1,10)
        if which <= 3:
            player.hp -= self.acid
            print(f"The {self.name} smashes a vial of bubbling acid onto your face")
        else:
            player.hp -= self.slash
            print(f"You feel the {self.name}'s scalpel slash into your cheek")
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    
    def heal(self):
        heal = random.randint(1,10)
        if heal <= 3:
            self.hp += 20
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            print(f"You watch as The {self.name} drops dead to the floor")
            player.ess += 20
        
class Amalgamation:
    def __init__(self):
        self.name = "Amalgamation"
        self.hp = 120
        self.chomp = 30
        self.sweep = 15
        self.dead = False
    
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
    
    def checkdead(self, player):
        if self.hp <= 0:
            self.dead = True
            print(f"You watch as The {self.name} begins to combust at no reason")
            player.ess += 20
    
    def fight(self, player):
        while not self.dead or player.hp <= 0:
            for weapon in player.weapons.items():
                print(f"- {weapon}")
            choice = input("Choose your weapon: ").lower()
            weapon = player.weapons.get(choice)
            weapon.use(self)
            self.attack(player)
            print(self.hp)
            self.checkdead(player)
    

    