class Father():
    def garden(self):
        print("I like gardening")
class Mother():
    def eat(self):
        print("I like eating")

class Child(Mother, Father):
    def drive(self):
        print("I like driving")

myChild = Child()
myChild.drive()
myChild.eat()
myChild.garden()

