from robot import Robot
from robot import Robot

from herd import Herd


dinosaur = Robot('Trex',20)
robot = Robot('Robotto')


class Battlefield:
    def __init__(self) -> None:
       self.run_game


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()



    def display_welcome(self):
        print('Welcome to the THUNDERDOME!!!!')
        
#(10 points): As a developer, I want the battle to conclude once either the Robot or the Dinosaur has its health points reduced to zero.

    def battle_phase(self,):
        while dinosaur.health > 0 and robot.health > 0:
            dinosaur.attack_robot(robot)
            robot.attack_dinosaur(dinosaur)
            if robot.health <= 0 or dinosaur.health <= 0:
                print('we have a winnner!!!')
            
            
    
    def display_winner(self):
        if dinosaur.health <= 0:
            print(f'{robot.name} is our winner')
        elif robot.health <= 0:
            print(f'{dinosaur.name} is our winner')

    
 #5 points): As a developer, I want to create 2 additional Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.
