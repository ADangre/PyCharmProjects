def dictionariesinpython():
    omnidirectionalities = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
    print("The dictionary names are:", omnidirectionalities)
    for key in omnidirectionalities:
        print("key:", key, "value:", omnidirectionalities[key])
    omnidirectionalities['g'] = 100
    # after inserting the new member in the dictionary
    print("after adding a new member g")
    print("The dictionary names are:", omnidirectionalities)
    # how to use the tuple to print key pair is mentioned below
    print("tuple representation")
    for a, b in omnidirectionalities.items():
        print("key:", a, "value:", b)
    return"dictionariesinpython"

print("calling a function", dictionariesinpython())
