n=int(input("enter no to check prime or not= "))
flg=0
for i in range(2,n):
    if(n%i==0):
        flg=1
        break
    else:
        pass
if(flg>0):
    print("not prime")
else:
    print("prime")