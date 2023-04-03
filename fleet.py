from robot import Robot

class Fleet:
    def __init__(self) -> None:
        self.robots = []
    
    def create_the_herd(self):

        robot_1 = Robot('Robotto')
        robot_2 = Robot('Terminator')
        robot_3 = Robot('Johnny5')

        self.robots = [robot_1, robot_2, robot_3]
