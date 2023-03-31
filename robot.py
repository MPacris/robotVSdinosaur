from weapon import Weapon

class Robot:
    def __init__(self, name,active_weapon) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = Weapon()
    
    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power


