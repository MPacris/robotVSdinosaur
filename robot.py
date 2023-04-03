#(10 points): As a developer, I want a Robot to have a name, health, and active_weapon. 

from weapon import Weapon


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('lazer', 30)
    
    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.active_weapon.attack_power} damage caused by {self.active_weapon.name} dinosaur health {dinosaur.health}')



