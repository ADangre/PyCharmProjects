exp = [2340, 2500, 2100, 3100, 2980]
total = exp[0] + exp[1] + exp[2] + exp[3]
total = 0
for i in exp :
    total = total + i
print("total expense is:", total)
for i in range(2, 10) :
    total = total + 1
    print("number is:", i, "The square is:", i * i)

print(total)

key_location = "chair"
locations = ["garage", "living room", "chair", "closet"]
i=0
for location in locations:
    i=i+1
    if location == "chair":
        print("chair is found at", i)
        break
    elif location == "garage":
        print("garage is found at", i)
print(i)