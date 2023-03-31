class Dinosaur:

    def __init__(self,name, atack_power,health) -> None:
        self.name = name
        self.attack_power = atack_power
        self.health = 100

    def attack_robot(self,attack_power, robot):
        self.attack_power = attack_power
        self.enemy = robot
        robot.health -= attack_power
        
        

        
        
        
