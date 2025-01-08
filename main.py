import random
from entities import *
from items import *
from levels import *

player = Player()
ghoul = Ghoul()

Tokarev = Weapon("Tokarev", (30,40), 50, 1, (6,11), lambda enemy: f"You shot {enemy.name}")
KS = Weapon("KS-23", (30,35), 40, 1, (12,20), lambda enemy: f"You blast a hole through {enemy.name}")
Axe = Weapon("Axe", (70,87), 100, 1, (3,8), lambda enemy: f"You hurl the Axe at {enemy.name} and slash it")
Shovel = Weapon("Shovel", (80,90), 100, 1, (6,10), lambda enemy: f"You smash {enemy.name} over the head with your Shovel")
Shiv = Weapon("Shiv", (90,100), 120, 1, (10,12), lambda enemy: f"You slice the {enemy.name} into bits")
SlingShot = Weapon("SlingShot", (40,45), 50, 1, (5,10), lambda enemy: f"You launch a sharp stone towards {enemy.name}")

Syringe = Heals("Syringe", 50, "You feel the thick goo run through your body but it stimulates you")
FieldKit = Heals("FieldKit", 30, "You tighten the tourniquete around your wound so the blood stops bleeding")
Bandage = Heals("Bandage", 15, "You wrap the dirty bandage around your wound")
Stim = Heals("Stim", 30, "You inject the stim into your arm")
Vial = Heals("GooVial", 35, "You crush the vial and watch as the mysterious goop sinks into your skin")

Boots = Armour("Dirty Boots", 3)
Helmet = Armour("Rugged Helmet", 5)
Vest = Armour("Military Vest", 10)
CivilianVest = Armour("Civilian Vest", 5)
Jacket = Armour("Ripped Jacket", 5)
MinerCap = Armour("Miner's Cap", 2)

Mica = DmgArtifact(40)
Soul = HealArtifact(50)

SecretKey = Weapon("Bunker Key", (0,0), 100, 0, (0,0), lambda enemy: f"You pull out the key and {enemy.name} begins to laugh at you")

player.pickup(Axe)
player.fight(ghoul)