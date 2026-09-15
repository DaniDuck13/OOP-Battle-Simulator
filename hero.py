import random
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self,name):
        self.name=name
        self.health=125
        self.attackPower=10

    def attack(self):
        return random.randint(1,self.attackPower)
    def takeDamage(self,damage):
        self.health= max(0, self.health-damage)
    def isAlive(self):
        print("{self.name} takes {damage} damage. Health {self.health}." )