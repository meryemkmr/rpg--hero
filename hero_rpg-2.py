import random 

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.character_name = 'character name'
        self.bank_account = 0

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def gain_bounty(self, enemy):
        self.bank_account += enemy.bounty

    def attack(self, enemy):
        

        if self.character_name == 'hero':
            randomInt = random.randint(1,5)
            if randomInt == 1:
                self.power = self.power * 2
            print(f"You do {self.power} damage to the {enemy.character_name}.")

        if enemy.character_name != 'zombie':
            enemy.health -= self.power
            
        if enemy.character_name == 'medic':
            randomInt = random.randint(1,5)
            if randomInt == 1:
                enemy.health = enemy.health + 2

        if enemy.character_name == 'shadow':
            randomInt = random.randomInt(1,10)
            if randomInt != 1:
                print("The shadow dodged your attack!")
                enemy.health = 1
            else:
                print("The shadow is vanquished!")

        elif( self.character_name == 'goblin' or self.character_name == 'zombie' ):
            print(f"The {self.character_name} does {self.power} damage to you.")

    def print_status(self):
        if self.character_name == 'hero':
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == 'goblin' or self.character_name == 'zombie':
            print(f"The {self.character_name} has {self.health} health and {self.power} power.")
    def enemy_list(self):
        enemy_list = [ 'hero', 'goblin', 'zombie', 'medic', 'shadow']
        print(random.choice(enemy_list))


class Hero(Character):
    def __init__(self, health, power,):
        super(Hero, self).__init__(health,power)
        self.character_name = 'hero'
        self.bank_account = 0
    

class Goblin(Character):
    def __init__(self, health, power):
        super(Goblin, self).__init__(health,power)
        self.character_name = 'goblin'
        self.bounty = 5

class Zombie(Character):
    def __init__(self, health, power):
        super(Zombie, self).__init__(health, power)
        self.character_name = 'zombie'
        self.bounty = 6

class Medic(Character):
    def __init__(self, health, power):
        super(Medic, self).__init__(health, power)
        self.character_name = 'medic'
        self.bounty = 7

class Shadow(Character):
    def __init__(self, health, power):
        super(Shadow, self).__init__(health, power)
        self.character_name = 'shadow'
        self.bounty = 8

hero = Hero(10,5)
goblin = Goblin(6,2)
zombi = Zombie(10,6)
medic = Medic(10,2)
shadow = Shadow(1,3)

print("Hero name:")
print(hero)
print(hero.character_name)
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
                hero.gain_bounty(enemy.enemy_list)
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

main()
