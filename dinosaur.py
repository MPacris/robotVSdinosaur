class Dinosaur:

    def __init__(self,name, atack_power) -> None:
        self.name = name
        self.attack_power = atack_power
        self.health = 100

    def attack_enemy(self,attack_power, dinosaur):
        self.attack_power = attack_power
        self.enemy = dinosaur
        dinosaur.health -= attack_power
        
        

        
        
        
