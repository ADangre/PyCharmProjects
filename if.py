# num=input("Enter a number:")
# num= int(num)
# result=num%2
# if(result==0):
#     print(num,"is even")
# else:
#     print(num, "is odd")


indian=["samosa", "daal","naan"]
chinese=["eggroll","pot sticker","fried rice"]
italian=["pizza","pasta","risotto"]

dish= input("Enter a dish:")
if dish in indian:
    print(dish,"is in indian")
elif dish in chinese:
    print(dish,"is chinese")
elif dish in italian:
    print(dish,"is italian")
else:
    print(dish,"is unknown")