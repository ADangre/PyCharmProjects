class Vehicle:
       def general_usage(self):
        print("My general usage is transport")

class Car(Vehicle):
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
   def special_usage(self):
       print("My special usage is commuting to work and supporting family to move from point A to point B")

class Motorcycle(Vehicle):
   def __init__(self, make, model, year):
       self.make = make
       self.model = model
       self.year = year
   def special_usage(self):
       print("I'm two wheeler and can carry only one rider with me. ")

C = Car(make="Toyota", model="Mustang", year=2019)
C.general_usage()
C.special_usage()
myMotorcycle = Motorcycle("Honda", "CXC", 2025)
myMotorcycle.general_usage()
myMotorcycle.special_usage()


