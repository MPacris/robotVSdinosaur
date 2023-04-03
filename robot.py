#(10 points): As a developer, I want a Robot to have a name, health, and active_weapon. 

from weapon import Weapon



class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = ()

#in basic version, the weapon was defined and added in with Weapon('Lazer,' 30), 
# trying to figure a way to pick from a list and set that as the active weapon

    def select_active_weapon(self):

        option_1 = Weapon('lazer', 30)
        option_2 = Weapon('missle', 40)
        option_3 = Weapon('big stick', 15)
        
        weapons_list = list()
        weapons_list.append(option_1)
        weapons_list.append(option_2)
        weapons_list.append(option_3)
        
        print(f'choose from the following weapons option 1 --- {option_1.name}, option 2 --- {option_2.name}, or option 3 --- {option_3.name}')

        chosen_weapon = input(f'choose your weapon by selecting a number from the 1 to 3 from your ----')
        if chosen_weapon == '1':
                self.active_weapon = option_1
        elif chosen_weapon == '2':
                self.active_weapon = option_2
        else: self.active_weapon = option_3

#(5 points): As a developer, I want to choose from a List of 3 possible weapons before a robot makes an attack. 

 

    def attack_dinosaur(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.active_weapon.attack_power} damage caused by {self.active_weapon.name} dinosaur health {dinosaur.health}')
        




