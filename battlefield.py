from robot import Robot
from dinosaur import Dinosaur




class Battlefield:
    def __init__(self) -> None:
        self.dinosaur = Dinosaur('Trex',30) 
        self.robot = Robot('Robotto')

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to the THUNDERDOME!!!!')
    


#(10 points): As a developer, I want the battle to conclude once either the Robot or the Dinosaur has its health points reduced to zero.

    def battle_phase(self,):
        while self.dinosaur.health > 0 and self.robot.health > 0:
            self.robot.select_active_weapon()
            self.robot.attack_dinosaur(self.dinosaur)
            if self.dinosaur.health <= 0:
                print('we have a winnner!!!')
            elif self.dinosaur.health > 0:
                self.dinosaur.attack_robot(self.robot)
                if self.robot.health <= 0:
                    print('we have a winnner!!!')

    def display_winner(self):
        if self.dinosaur.health <= 0:
            print(f'{self.robot.name} is our winner')
        elif self.robot.health <= 0:
            print(f'{self.dinosaur.name} is our winner')
            
    
    
 #5 points): As a developer, I want to create 2 additional Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.
