class uidException(Exception):
    def __init__(self, uid):
        self.uid = uid
    def printException(self):
        print("The custom exception is:",self.uid)
try:
    # raise ValueError("ValueError")
    raise uidException("I want to raise an exception")
except uidException as e:
   print(e)
   e.printException()