from logging import exception
result =0
try:
    x= int(input("Enter a number"))
    y= int(input("Enter a number"))
    result= int(x/y)
except ZeroDivisionError:
    print("You can't divide by zero")
except Exception as e:
    print(e)

print(result)
