from dinosaur import Dinosaur

class Herd:
    def __init__(self) -> None:
        self.dinosaurs = []
        self.create_the_herd()
    
    def create_the_herd(self):

        dinosaur_1 = Dinosaur('Trekks', 30, 100)
        dinosaur_2 = Dinosaur('Longneck', 40, 100)
        dinosaur_3 = Dinosaur('Velli', 15, 100)

        self.dinosaurs = [dinosaur_1, dinosaur_2, dinosaur_3]
        






