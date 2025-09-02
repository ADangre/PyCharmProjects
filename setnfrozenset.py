def setnfrozenset():
    basket={"apple","orange","apple","orange","banana","banana","mango","pineapple","mango"}
    print(basket)
    print(len(basket))
    print(type(basket))

def setnfrozensetoperations():
#     converting a list of elements into a set and removing duplicates
    x=[1,2,3,4,4,3,2,1,0]
    print("The list x is:",x, "The length of x is:",len(x))
    xset=set(x)
    print("After removing the duplicate elements the xset set is:",xset," and the length of x is:",len(xset))
    yset = set(x)
    yset.add(100)
#  we can also use union, intersection and issubset operations on set
    print("After adding the additional elements the yset set is:",yset)
    print(xset < yset)
    print(yset < xset)
    print("union of both sets:",xset|yset)
    print(xset.issubset(yset))
    print("intersection of both sets:",xset&yset)
    print("differences in both sets:",yset-xset)

mybasket=setnfrozenset()
mybasket = setnfrozensetoperations()