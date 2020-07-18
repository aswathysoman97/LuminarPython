lst=[1,52,9,27,3,8,2,19,12,11]
x=sorted(lst)
#print(lst)
lower=0
upper=len(lst)
elmnt=int(input("enter the number to be searched= "))
while (lower<upper):
    mid = (lower + upper) // 2
    if(elmnt<x[mid]):
        upper=mid-1
    elif(elmnt>x[mid]):
        lower=mid+1
    elif(elmnt==x[mid]):
        print("number found ",mid)
        break
    else:
        print("number not found")
