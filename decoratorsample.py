import  time
def time_it(junk):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = junk(*args, **kwargs)
        end = time.time()
        print((end-start)*1000)
        return result
    return wrapper
@time_it
def calculatesquare(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result
@time_it
def calculatecubes(numbers):
    result = []
    for number in numbers:
        result.append(number * number*number)
    return result

myNumber = range(1,10000)
calculatesquare(myNumber)
calculatecubes(myNumber)