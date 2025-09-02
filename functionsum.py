total = 0
def sum(a, b=10):
    """This function returns the sum of two input numbers but also considers the second number as default 10"""
    total = a + b
    print("total inside the function sum:", total)
    return total


sum(1, 2)
print("total outside the function sum:", total)
sum(10)
print("total outside the function sum:", total)

