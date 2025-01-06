import random
from entities import *
from items import *

player = Player()
captain = Captain()

Tokarev = Weapon("Tokarev", (30,40), 50, 1, (6,11), lambda enemy: f"You shot {enemy.name}")
KS = Weapon("KS-23", (30,35), 40, 1, (12,20), lambda enemy: f"You blast a hole through {enemy.name}")
Axe = Weapon("Axe", (70,87), 100, 1, (3,8), lambda enemy: f"You hurl the Axe at {enemy.name} and slash it")
Shovel = Weapon("Shovel", (80,90), 100, 1, (6,10), lambda enemy: f"You smash {enemy.name} over the head with your Shovel")

# player.pickup(KS)

# while not captain.dead:
#     player.attack(captain, KS)
#     print(captain.hp)
#     captain.checkdead(player)
#     (player.inv).append(Tokarev)
#     print(player.inv)




