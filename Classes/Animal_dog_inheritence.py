# create inheritance using animal Dog relation.
# for example,
#     Animal and Dog both has same habitat so create a method for habitat


class Animal():
    def __init__(self , habitat):
        self.habitat = habitat

    def habitat(self):
       return  self.habitat

    def sound(self):
        return "sound"

class Dog(Animal):
    def __init__(self):
        super().__init__('Dog')

    def sound(self):
        print("bow bow")


x = Dog()
x.sound()
