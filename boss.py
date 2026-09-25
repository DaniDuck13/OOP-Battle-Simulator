from enemy import Enemy
import random

class Boss(Enemy):

    def __init__(self, name):
        super().__init__(name, health=150, attackPower=12)
    def randomMidBattleInsult(self):
            insults=["You challenge me with that stance? Preposterous.","Is that a weapon, or a toothpick? Fight harder!","I can hear your heartbeat from across the room.","I've stepped on bugs that put up a better fight."]
            print(f"{self.name} laughs. {insults[random.randint(0,(len(insults)-1))]}")
    def attack(self):
        damage=super().attack()
        bonus=5
        print(f"{self.name} unleashes a crushing blow!")
        if random.randint(0,6)==3:
             self.randomMidBattleInsult()
        return damage + bonus
    

    