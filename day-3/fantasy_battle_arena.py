import random
class Character():
    def __init__(self,name,health,attack_power,defense,speed):
        self.name=name
        self.health=health
        self.attack_power=attack_power
        self.defense=defense
        self.speed=speed
    
    def attack(self,target):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(self.attack_power) 

    def take_damage(self,amount):
        damage = max(1, amount - self.defense)
        self.health-=amount
        print(f"{self.name} takes {damage} damage. Health now: {self.health}")

    def is_alive(self):
        return self.health > 0


class warrior(Character):
    def __init__(self, name, health, attack_power, defense, speed, rage=0):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage = rage

    
    def take_damage(self, amount):
        super().take_damage(amount)
        self.rage += 10

    def attack(self, target):
        if self.health < 40:
            print(f"{self.name} enters Berserk Mode!")
            damage = self.attack_power * 2
        else:
            damage = self.attack_power
        print(f"{self.name} strikes with {damage} damage.")
        target.take_damage(damage)

class mage(Character):
    def __init__(self, name, health, attack_power, defense, speed, mana):
        super().__init__(name, health, attack_power, defense, speed)
        self.mana = mana


    def attack(self, target):
        if self.mana >= 10:
            print(f"{self.name} casts Fireball!")
            damage = self.attack_power + 20
            target.take_damage(damage)
            self.mana -= 10
            self.health -= 5
            print(f"{self.name} loses 5 health from recoil. Mana left: {self.mana}")
        else:
            print(f"{self.name} attacks normally.")
            super().attack(target)


class archer(Character):
    def __init__(self, name, health, attack_power, defense, speed, critical_chance):
        super().__init__(name, health, attack_power, defense, speed)
        self.critical_chance = critical_chance


    def attack(self, target):
        if random.random() < self.critical_chance:
            print(f"{self.name} lands a Critical Hit!")
            damage = self.attack_power * 2
        else:
            damage = self.attack_power
        print(f"{self.name} deals {damage} damage.")
        target.take_damage(damage)

def battle(c1, c2):
    print("\nBattle Begins!\n")
    fighters = sorted([c1, c2], key=lambda x: x.speed, reverse=True)
    print(f"Battle: {c1.name} vs {c2.name} \n")
    while c1.is_alive() and c2.is_alive():
        for fighter in fighters:
            opponent = c2 if fighter == c1 else c1
            if fighter.is_alive():
                fighter.attack(opponent)
            if not opponent.is_alive():
                print(f"\n{opponent.name} is defeated!")
                print(f"{fighter.name} wins the battle!\n")
                return

w = warrior("Thor", 130, 25, 15, 8, rage=0)
m = mage("Gandalf", 85, 35, 4, 10, mana=50)
a = archer("Alex", 95, 22, 7, 18, critical_chance=0.3)
battle(w, a)
