# myShoppingList = ["Mangoes", "Rice", "Bananas","Cheese", "Pepperoni"]
# for item in myShoppingList:
#     print(item)
#
# # I want to know print the list in the reverse order
# print("-------------------------------------\n Revese shopping list")
# myReverseShoppingList = reversed(myShoppingList)
# for item in myReverseShoppingList:
#     print(item)

class RemoteControl():
    def __init__(self):
        self.channels = ["HBO", "Zee","CNN","Cartoon"]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index >= len(self.channels):
            try:
                raise StopIteration
            except Exception as e:
                print("StopIteration",e)
        return self.channels[self.index]

remoteControl = RemoteControl()
# for item in remoteControl:
#     print(item)
iter=remoteControl.__iter__()
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
