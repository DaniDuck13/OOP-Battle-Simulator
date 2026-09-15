from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Black Hole"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Bartholomew")
    hero= Hero("Merida", "Hacker")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
  
    goblin2 = Goblin("Jeffery")
    
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    print("But no hero has answered the call... yet.")
    print(f"{hero.name} the {hero.hero_class} enters the arena with {hero.health} health.")

    print(f"{hero.name} attacks {goblin2.name}.")
    goblin2.take_damage(hero.attack())
    


if __name__ == "__main__":
    main()
