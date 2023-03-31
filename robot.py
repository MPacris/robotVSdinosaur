from weapon import Weapon


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.weapon = Weapon("big stick", 15)

    
    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(dinosaur.health)


