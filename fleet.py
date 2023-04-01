from robot import Robot

class Herd:
    def __init__(self) -> None:
        self.robots = []
    
    def create_the_herd(self):

        robot_1 = Robot('Trekks')
        robot_2 = Robot('Longneck')
        robot_3 = Robot('Velli')

        self.robots = [robot_1, robot_2, robot_3]
