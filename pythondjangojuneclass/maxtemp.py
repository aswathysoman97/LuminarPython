f=open("C:/Users/chakkara/PycharmProjects/pythondjangojuneclass/data.csv","r")
dict={}
for data in f:
    value=data.rstrip("\n").split(",")
    dist=value[0]
    temp=value[1]
    print(dist)
    print(temp)
    if (dist not in dict):
        dict[dist]=temp
    else:
        dict[dist]+=temp
print("maximum temperature= ",dict)
