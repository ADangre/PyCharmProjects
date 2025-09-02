class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
    def do_work(self):
        if self.occupation == "tennis":
            print(self.name," plays tennis")
        elif self.occupation == "actor":
            print(self.name," plays roles in movies")
    def speaks(self):
        print(self.name," says hello to you! ")

Tom = Human("Tom", "actor")
Tom.do_work()
tom = Tom.speaks()
# print(tom)
Maria = Human("Maria", "tennis")
Maria.do_work()
maria = Maria.speaks()
# print(maria)
