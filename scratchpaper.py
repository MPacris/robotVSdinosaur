
#(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. 
# This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon. 
    

        self.weapons_choices = list()
        option_1 = Weapon('lazer', 30)
        option_2 = Weapon('missle', 40)
        option_3 = Weapon('big stick', 15)

#(5 points): As a developer, I want to choose from a List of 3 possible weapons before a robot makes an attack. 

        chosen_weapon = input(f'choose your weapon by selecting a number from 1 to 3 from your ----')
        if chosen_weapon == '1':
            self.weapon = option_1
        elif chosen_weapon == '2':
            self.weapon = option_2
        else: self.weapon = option_3
        
