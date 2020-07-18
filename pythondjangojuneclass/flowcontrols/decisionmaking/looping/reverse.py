n=int(input("enter a no= "))
rv=0
while(n>0):
    rmndr=n%10
    rv=rv+(rmndr*rmndr*rmndr)
   # rev=(rev*10)+rmndr
    n=n//10
print("reverse= ",rv)