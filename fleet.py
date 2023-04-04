
from robot import Robot


class Fleet:
    def __init__(self,active_robot) -> None:
        self.active_robot = ()
        self.robots_list = [Robot('Robotto'), Robot('Terminator'), Robot('Johnny5')]

    def select_active_robot (self):
            chosen_robot = input(f'type the option number of the robot you wish to send to battle:  option 1 - {self.robots_list[0]},  option 2 - {self.robots_list[1]}, option 3 {self.robots_list[2]}   ')
            if chosen_robot == "1":
                self.active_robot = self.robots_list[0]
            elif chosen_robot == "2":
                self.active_robot = self.robots_list[1]
            else:
                self.active_robot = self.robots_list[2]
      

    
    



    

        
    
    


    
