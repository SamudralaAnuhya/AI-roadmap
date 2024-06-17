#vehicle has general usage(transportation)
#car has four wheels and different roof and specific use (family tour)
#bike has 2 wheels ,no roof ,soecific use racing

class Vehicle:
    def general_usage(self):
        print("Vehicle is used for transportation")

class car(Vehicle):
    def __init__(self):
        self.wheels : 4
        self.roof : "yes"
        print("I am car")
    def specific_usage(self):
        self.general_usage()
        print("Car is used for family tours")

class motorcycle(Vehicle):
    def __init__(self):
        self.wheels : 2
        self.roof : "No"
        print("I am motorcycle")
    def specific_usage(self):
        Vehicle.general_usage(self)
        print("Motorcycle is used for racing")


c = car()
c.general_usage()
m = motorcycle()
m.specific_usage()
print(isinstance(c,car))
print(issubclass(car,Vehicle))



