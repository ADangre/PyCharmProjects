def Fib():
    a, b = 0, 1
    while True:
        yield a
        a = b
        b = a + b


for myFib in Fib():
    if myFib > 30:
        break
    print(myFib)
