from robot import Robot

class Fleet:
    def __init__(self) -> None:
        self.robots_list = []
    
    def create_the_herd(self):

        robot_1 = Robot('Robotto')
        robot_2 = Robot('Terminator')
        robot_3 = Robot('Johnny5')

        self.robots = list()
        self.robots_list = self.robots_list.append(robot_1)
        self.robots_list = self.robots_list.append(robot_2)
        self.robots_list = self.robots_list.append(robot_3)

        

    

