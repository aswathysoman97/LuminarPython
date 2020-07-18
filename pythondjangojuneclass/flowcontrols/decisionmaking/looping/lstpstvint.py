lst1=[]
r=int(input("range of list: "))
print("enter elements for list up to range ", r, ":")
for i in range (1,r+1):
    n = int(input())
    lst.append(n)
    lst.sort()
print(lst)
lst2=[]
for j in range(lst[0],len(lst1)):
    if(j not in lst1):
        lst2.append(j)
print("missing numbers= ",lst2)


