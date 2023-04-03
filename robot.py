#(10 points): As a developer, I want a Robot to have a name, health, and active_weapon. 

from weapon import Weapon



class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = ()
        self.weapons_list = [ Weapon('lazer', 30),Weapon('missile', 40),Weapon('big stick', 15)]

#in basic version, the weapon was defined and added in with Weapon('Lazer,' 30), 
# trying to figure a way to pick from a list and set that as the active weapon

    def select_active_weapon(self): 
        chosen_weapon = input(f"choose the Robot's weapon: option 1 - {self.weapons_list[0].name}, option 2 - {self.weapons_list[1].name}, or option 3 - {self.weapons_list[2].name} choose your weapon by typing in a the option number!  ")
        if chosen_weapon == '1':
                self.active_weapon = self.weapons_list[0]
        elif chosen_weapon == '2':
                self.active_weapon = self.weapons_list[1]
        else: self.active_weapon = self.weapons_list[2]

#(5 points): As a developer, I want to choose from a List of 3 possible weapons before a robot makes an attack. 


    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'Robot inflicts {self.active_weapon.attack_power} damage caused by {self.active_weapon.name}. Dinosaur health is now {dinosaur.health}')
        




