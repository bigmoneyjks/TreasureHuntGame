import random
class Player:
    def __init__(self):
        self.hp = 100
        self.stun = False
        
    def pickup(self, item, inventory):
        if len(inventory) != 8:
            inventory.append(item)
        else:
            print(f"You cannot fit {item.name} into your rucksack")
    
    def heal(self, inventory):
        if "Spiral" in inventory:
            self.hp += random.randint(10,40)
        else:
            print("You realise that you don't have a Spiral")
    
    def attack(self, enemy, inventory):
        if "Tokarev" in inventory:

