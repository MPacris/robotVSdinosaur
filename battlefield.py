from dinosaur import Dinosaur
from robot import Robot

dinosaur = ('Trex',20)
robot = ('Robotto')


class Battlefield:
    def __init__(self) -> None:
        pass


    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()



    def display_welcome(self):
        print('Welcome to the THUNDERDOME!!!!')
        

    def battle_phase(self):
        while dinosaur.health > 0 and robot.health > 0:
            dinosaur.attack_robot
            robot.attack_dinosaur
            if robot.health <= 0 or dinosaur.health <= 0:
                print('we have a winnner!!!')
            
            
    
    def display_winner(self):
        if dinosaur.health <= 0:
            print(f'{robot} is our winner')
        elif robot.health <= 0:
            print(f'{dinosaur} is our winner')
    