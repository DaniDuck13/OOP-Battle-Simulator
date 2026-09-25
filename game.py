from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Black Hole"
def battle(hero: Hero, enemy: Goblin):
    while hero.isAlive() and enemy.is_alive():
        hero_damage=hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive:
           enemy_damage=enemy.attack()
           hero.takeDamage(enemy_damage)
    if hero.isAlive():
        print(f"{hero.name} won the battle!")
    else:
        print(f"{enemy.name} won the battle!")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Bartholomew")
    hero= Hero((input("What would you like to name your hero? ")), (input("What class is your hero? (Mage, Archer, Swordsman, Hacker, Alchemist ) ")))

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
  
    goblin2 = Goblin("Jeffery")
    
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("But no hero has answered the call... yet.")
    print(f"{hero.name} the {hero.hero_class} enters the arena with {hero.health} health.")

    battle(hero, goblin2)


if __name__ == "__main__":
    main()
