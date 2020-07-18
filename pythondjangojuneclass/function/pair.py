#for i in range(1,50):
  #  list.append(i)
def pair(n):
    for j in list:
        res=n-j
        if(res>=j):
            if res in list:
                sumList.append(j,res)
            else:
                break
    return sumList
n=int(input("enter a number= "))
res=pair(n)
print("the number whose sum equels to",num,"are= ",res())