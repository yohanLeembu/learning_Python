import random
class Character:
    def __init__(self, name, lvl, exp, hp, atk, defense):
        self.name = name
        self.lvl = lvl
        self.exp = exp
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.defense = defense
        
    def attack(self, other):
        damage = int(max(1, self.atk**2 / (self.atk + other.defense)))
        other.hp -= damage

        # prevent negative HP display
        if other.hp < 0:
            other.hp = 0

        return (
            f"{self.name} attacks {other.name}!\n"
            f"lvl: {other.lvl}\n"
            f"{other.name} HP: {other.hp}/{other.max_hp} -{damage}"
        )

class Player(Character):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = self.hp
        self.atk = 10
        self.defense = 10
        self.lvl = 1
        self.exp = 0
        self.equipped_items = []
        self.inventory = []

    def get_exp_to_next_level(self):
        return 100 * self.lvl

    def level_up(self):
        while self.exp >= self.get_exp_to_next_level():
            self.exp -= self.get_exp_to_next_level()
            self.lvl +=1

            print(f"You Leveled Up! Now Level {self.lvl}")
            
            self.hp += 20
            self.atk += 5
            self.defense += 3

    def equip_armor(self):
        if not self.inventory:
            print("nothing to equip")
            return
        
        for item in self.inventory:
            print(f"Name: {item['name']} | Atk: {item['atk']} | Def: {item['defense']}")

        while True:
            chosen_item = input("Enter the name of the item (or exit): ")

            if chosen_item == "exit":
                break

            for item in self.inventory:
                if chosen_item == item["name"]:
                    self.atk += item["atk"]
                    self.defense += item["defense"]

                    print(f"You equipped {item['name']}")
                    self.equipped_items.append(item)
                    self.inventory.remove(item)

                    return

            print("There is no item like that")

            

    def add_item(self, dropped_items):
        if not dropped_items:
            print("no items to pick")
            return
        
        for item in dropped_items:
            print(f"Name: {item['name']} | Atk: {item['atk']} | Def: {item['defense']}")

        print("Only one item can be taken")

        while True:
            chosen_item = input("Enter the item's name(no to exit): ")

            if chosen_item == "no" :
                break

            for item in dropped_items:
                if chosen_item == item["name"]:
                    print(f"You Added {item['name']} in the inventory.")
                    self.inventory.append(item)
                    dropped_items.remove(item)
                    return
                
            print("no item named like that")


    def delete_item(self):
        if not self.inventory:
            print("there is nothing to delete")
            return

        for item in self.inventory:
            print(f"Name: {item['name']} | Atk: {item['atk']} | Def: {item['defense']}")

        while True:
            chosen_item = input("Enter the name of the item (or exit): ")

            if chosen_item == "exit":
                break

            for item in self.inventory:
                if chosen_item == item["name"]:
                    print(f"You deleted {item['name']} from the inventory")
                    self.inventory.remove(item)
                    return

            print("There is no item like that")
            

    def check_inventory(self):
        if not self.inventory:
            print("nothing is in the inventory")
            return
        for item in self.inventory:
            print(f"Name: {item['name']} | Atk: {item['atk']} | Def: {item['defense']}")


class Enemy(Character):
    def __init__(self, name, lvl, exp, hp, atk, defense):
        super().__init__(name, lvl, exp, hp, atk, defense)
        self.max_hp = hp
        self.items_drops = []

    def item_drop(self):
        dropped_items = []

        for item in self.items_drops:
            roll = random.random()
            if roll >= item["chance"]:
                dropped_items.append(item)
        return dropped_items
    
    


# Example items
minotaur_sword = {
    "name": "Super Big Sword",
    "atk": 20,
    "defense": 30,
    "chance": 0.2
}

minotaur_armor = {
    "name": "Big Bad Armor",
    "atk": 10,
    "defense": 80,
    "chance": 0.4
}

# Enemy objects
minotaur = Enemy(
    name="Minotaur",
    lvl=5,
    exp=100,
    hp=200,
    atk=30,
    defense=15
)

minotaur.items_drops = [minotaur_sword, minotaur_armor]


goblin_dagger = {
    "name": "Rusty Dagger",
    "atk": 5,
    "defense": 2,
    "chance": 0.5
}

goblin = Enemy(
    name="Goblin",
    lvl=1,
    exp=20,
    hp=50,
    atk=10,
    defense=3
)

goblin.items_drops = [goblin_dagger]


enemies = [minotaur, goblin]

def enemy_list(enemies):
    if not enemies:
        print("No enemies available.")
        return

    for enemy in enemies:
        print("\n======================")
        print(f"Enemy: {enemy.name}")
        print(f"Level: {enemy.lvl}")
        print(f"HP: {enemy.hp}")
        print(f"ATK: {enemy.atk}")
        print(f"DEF: {enemy.defense}")

        print("Drops:")

        if not enemy.items_drops:
            print("  None")
        else:
            for item in enemy.items_drops:
                print(f"  - {item['name']} ({int(item['chance'] * 100)}%)")


    
def encounter(player, enemies):
    valid_enemies = []

    for enemy in enemies:
        if enemy.lvl <= player.lvl:
            valid_enemies.append(enemy)
    
    if not valid_enemies:
        print("No enemies available for your level.")
        return 
    
    chosen_enemy = random.choice(valid_enemies)

    print(f"\nA wild {chosen_enemy.name} appeared!!")
    print(f"Level: {chosen_enemy.lvl}")

    return chosen_enemy













