def pattern(lst1):
    lst2=[]
    p=1
    for i in lst1:
        r=i**p
        lst2.append(r)
        p+=1
    print(lst1,"=>",lst2)
pattern([2,4,3])