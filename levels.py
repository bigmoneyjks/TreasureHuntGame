class Area:
    def __init__(self, name, locked):
        self.name = name
        self.locked = locked
        self.unexplored = []
        self.keys = []

    def add_next_place(self, place):
        print(f"You spot the {place.name} off in the distance... maybe it leads you out of this forsaken land")
        self.unexplored.append(place)
    
    def foundkey(self, item):
        print(f"You think that this may be useful in the future")
        self.keys.append(item)
    
    def options(self, choices):
        choices = choices
        


    



































# class Level1:
#     def __init__(self, startdesc, area2desc, enemy1, boss):
#         self.start  = "House"
#         self.startdesc = startdesc
#         self.area2 = "Forest"
#         self.area2desc = area2desc
#         self.monster = enemy1
#         self.boss = boss
    
#     def enterHouse(self, player, axe):
#         print(self.startdesc)
#         (player.inv).append(axe)
    
#     def enterForestFight(self, player, enemy1):
#         print("As you step out of the run down house, you spot an inhuman creature scurrying towards you before launching at you")
#         while not enemy1.dead:
#             print(f"{player.inv}")
#             action = int(input("Please choose which item to use (enter number)"))
#             player.attack(enemy1, (player.inv)[action+1])
#             print(enemy1.hp)
#             enemy1.checkdead(player)
#             (player.inv).append(enemy1)
    