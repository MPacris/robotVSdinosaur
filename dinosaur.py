#(10 points): As a developer, I want a Dinosaur to have a name, health, and attack_power.  

class Robot:

    def __init__(self, name, attack_power) -> None:
        self.name = name
        self.attack_power = attack_power
        self.health = 100

#(10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. 
# This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power. 
    def attack_robot(self,robot):
        robot.health -= self.attack_power
        print(f'robot health: {robot.health}')
        
        
        

        
        
        
