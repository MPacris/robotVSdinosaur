#(10 points): As a developer, I want a Robot to have a name, health, and active_weapon. 

from weapon import Weapon


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.weapon = Weapon("big stick", 15)

#(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon. 
    
    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f'dinosaur health {dinosaur.health}')


