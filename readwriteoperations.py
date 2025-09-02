# f=open("c:\\data\\input.txt","a")
# f.write("\nI'm in love with Javascript")
# f.write("\nLearning Javascript will boost your career.")
# f.close()
# f=open("c:\\data\\input.txt","r")
# print(f.read())
# f.close()
f=open("c:\\data\\input.txt","r")
for line in f:
    tokens = line.split()
    print(line,"The tatal length is:",len(line), "Total words is:",len(tokens))
    with open("c:\\data\\output.txt","w+") as outfile:
        outfile.write(str(len(tokens)))


f.close()
