from dinosaur import Dinosaur
from robot import Robot


dinosaur = Dinosaur('Trex',20)
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
    