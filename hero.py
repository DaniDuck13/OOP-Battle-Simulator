import random
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self,name,heroClass):
        #heroClass can be Hacker, Archer, Mage, Swordsman, or Alchemist
        self.name=name
        self.health=50
        self.attackPower=15
        self.hero_class=heroClass

    def attack(self):
        return random.randint(1,self.attackPower)
    def takeDamage(self,damage):
        self.health= max(0, self.health-damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
    def isAlive(self):
        return self.health > 0