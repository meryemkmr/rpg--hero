#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

from random import randint


class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def alive(self):
        if self.health > 0 or self.name == "Zombie":
            return True

    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))
        print("--------------------------------------")
    
    def attack(self, enemy):
        random20 = randint(1,5)
        random10 = randint(1,10)
        ## Hero does basic damage and can crit(20%)
        ## Medic does basic damage and can heal
        ## Wizard does basic damage and can crit(40%)
        ## Archer does high damage but can miss(40%)
        if self.name == "Knight" and random20 == 1:
            enemy.health -= self.power * 2
            print(f"{self.name} has CRIT!")
        elif enemy.name == "Medic" and random20 == 1:
            enemy.health -= self.power
            enemy.health += 2
            print(f"{self.name} has restored 2 health")
        elif enemy.name == "Wizard" and random20 <= 2:
            enemy.health -= self.power * 2
            print(f"{self.name} used a Fire Blast!")
        elif self.name == "Archer" and random20 <= 2:
            enemy.health += 0
            print(f"{self.name} missed a shot.")
        elif enemy.name == "Shadow" and random10 <= 9:
            enemy.health += 0
            print(f"{enemy.name} dodged your attack.")
        else:
            enemy.health -= self.power
    
    # def block(self, enemy):
    #     random20 = randint(1,5)
    #     ## Option 2 is a 40% chance at blocking
    #     if random20 <= 2:
    #         print(f'{self.name} has blocked the attack.')
    #         pass
    #     else:
    #         print(f"{self.name}'s block was unsuccessful")
    #         enemy.health -= self.power

class Hero(Character):
    def __init__(self, name, health, power, armor, gold):
        super().__init__(name, health, power)
        self.gold = gold
        self.backpack = []

class Enemy(Character):
    def __init__(self, name, health, power, bounty):
        super().__init__(name, health, power)
        self.bounty = bounty

class SuperTonic():
    cost = 5
    name = "Super Tonic"
    
    def apply(self, hero):
        hero.health += 10
        print(f"{hero.name}'s health has increased to {hero.health}'")

class Armor():
    cost = 5
    name = "Heavy Armor"

    def apply(self, hero):
        pass

class Sword():
    cost = 5
    name = "Long Sword"

    def apply(self, hero):
        hero.power += 2

class Store():
    items = [SuperTonic, Armor, Sword]

    def do_shopping(self, hero):
        while True:
            print(f"""
            ==============================
            Welcome to the general store!
            ==============================
            You have {hero.gold} gold.
            What would you like to buy?
            """)
            for s in range(len(Store.items)):
                item = Store.items[s]
                print(f"{s + 1}. {item.name} {item.cost} gold")
            print("4. Leave")
            selection = int(input(">> "))
            if selection == 1:
                SuperTonic().apply(hero)
            elif selection == 2:
                Armor().apply(hero)
            elif selection == 3:
                Sword().apply(hero)
            elif selection == 4:
                cont()
            else:
                print("That is not a valid option.")


def cont():
    selection = int(input("""
    What would you like to do now?
    1. Visit Store
    2. Battle
    3. Leave
    >> """))
    if selection == 1:
        store = Store()
        store.do_shopping(hero)
    elif selection == 2:
        battle()
    elif selection == 3:
        print("Goodbye.")
        quit()
    else:
        print("That is not a valid option.")

def heroSelection():
    selection = int(input("""
Please Choose Your Hero:
          Hero    Health  Power   Armor   Gold 
     -------------------------------------------
    | 1.  Knight    12      5       0      10   |
    | 2.  Medic      8      3       0      10   |
    | 3.  Wizard     6      4       0      10   |
    | 4.  Archer     5      6       0      10   |
>> """))
    print("")
    if selection == 1:
        hero = Hero("Knight", 12, 5, 0, 10)
    elif selection == 2:
        hero = Hero("Medic", 8, 3, 0, 10)
    elif selection == 3:
        hero = Hero("Wizard", 6, 4, 0, 10)
    elif selection == 4:
        hero = Hero("Archer", 5, 6, 0, 10)
    else:
        hero = Hero("Knight", 12, 5, 0, 10)
    print("--------------------------------------")
    print(f"You have chosen the {hero.name}")
    
    return hero

def monsterRoll():
    roll = randint(1,20)

    if roll <= 8:
        enemy = Enemy("Goblin", 6, 2, 5)
    elif roll >= 9 and roll < 14:
        enemy = Enemy("Zombie", 0, 2, 100)
    elif roll >= 14 and roll < 18:
        enemy = Enemy("Shadow", 1, 1, 10)
    else:
        enemy = Enemy("Giant", 20, 3, 20)

    print("--------------------------------------")
    print(f"A {enemy.name} has appeared!!")

    return enemy

def battle():
    enemy = monsterRoll()
    enemy.print_status()

    while enemy.alive() and hero.alive():
        print()
        print("What's your next move?")
        print(f"1. fight {enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)
            print("--------------------------------------")
            print("You do {} damage to the {}.".format(hero.power, enemy.name))
            enemy.print_status()
            if enemy.name == "Zombie":
                print(f"You can't kill something that's already dead... RUN!")
                print("--------------------------------------")
            elif enemy.health <= 0:
                print("--------------------------------------")
                print(f"You have killed the {enemy.name}!")
                print(f"You have found {enemy.bounty} gold.")
                hero.gold += enemy.bounty
                print(f"Wallet: {hero.gold} gold")
                print("--------------------------------------")
                cont()
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You run away...")
            cont()
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0 or enemy.name == "Zombie":
            # Enemy attacks hero
            enemy.attack(hero)
            print("The {} does {} damage to you.".format(enemy.name, enemy.power))
            hero.print_status()
            if hero.health <= 0:
                print("You are dead.")
                main()


def main():
    hero = heroSelection()
    hero.print_status()
    return hero

hero = main()

cont()