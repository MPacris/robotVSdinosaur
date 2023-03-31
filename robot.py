from weapon import Weapon

Weapon('the big stick', 15)


class Robot:
    def __init__(self, name, health, active_weapon) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = Weapon()
    
    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power


