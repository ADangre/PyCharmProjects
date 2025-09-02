class Father():
    def skill(self):
        print("I like gardening")
class Mother():
    def skill(self):
        print("I like eating")

class Child(Mother, Father):
    def skill(self):
        print("I like driving")

myChild = Child()
myChild.skill()
myChild = Mother()
myChild.skill()
myChild=Father()
myChild.skill()