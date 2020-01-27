class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.character_name = ''

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        
        if enemy.character_name != 'zombie':
            enemy.health -= self.power
        if self.character_name == 'hero':
            print(f"You do {self.power} damage to the {enemy.character_name}.")
        elif( self.character_name == 'goblin' or self.character_name == 'zombie' ):
            print(f"The {self.character_name} does {self.power} damage to you.")

    def print_status(self):
        if self.character_name == 'hero':

            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == 'goblin' or self.character_name == 'zombie':
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")

class Hero(Character):
    def __init__(self, health, power):
        self.character_name = 'hero'
        super(Hero, self).__init__(health,power)
    

class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = 'goblin'
        super(Goblin, self).__init__(health,power)

class Zombie(Character):
    def __init__(self, health, power):
        self.character_name = 'zombie'
        super(Zombie, self).__init__(health, power)

hero = Hero(10,5)
goblin = Goblin(6,2)
zombi = Zombie(10,6)

def main(enemy):
    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.character_name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)
            
            if not enemy.alive():
                print(f"The {enemy.character_name} is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(hero)
            
            if not hero.alive():
                print("You are dead.")

main(zombi)
