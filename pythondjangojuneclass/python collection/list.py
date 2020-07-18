element=int(input("enter the element= "))
list=[2,5,6,8,12,10,7]
for i in list:
    for j in list:
        if(i+j==element):
            print(i,j)