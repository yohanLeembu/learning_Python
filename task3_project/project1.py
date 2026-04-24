
class Character:
    def __init__(self, name, health_points):
        self.name = name
        self.health_points = health_points

    def attack (self, other):
        other.health_points -= 2
        return other.health_points


class Enemy(Character):
    pass
        

class Player(Character):
    pass


player1 = Player("Yohan", 12)

enemy1 = Enemy("Boss", 20)

while(enemy1.health_points > 0 and player1.health_points > 0 ):
    print("""Option
          1. Attack
          2. Display Stats
          3. Exit
          """)
    action = int(input("enter your choice: "))
    if action == 1:
        player1.attack(enemy1)
        print(f"{player1.name} attacked {enemy1.name}!!!")
        print(f"{enemy1.name} took 2 damamge!!")
        enemy1.attack(player1)


if enemy1.health_points == 0:
    print("You won!!")

else:
    print("You Lost...")