from robot import Robot

class Herd:
    def __init__(self) -> None:
        self.dianosaurs = []
    
    def create_the_herd(self):

        dinosaur_1 = Robot('Trekks', 30)
        dinosaur_2 = Robot('Longneck', 40)
        dinosaur_3 = Robot('Velli', 15)

        self.dianosaurs = [dinosaur_1, dinosaur_2, dinosaur_3]

    

    

