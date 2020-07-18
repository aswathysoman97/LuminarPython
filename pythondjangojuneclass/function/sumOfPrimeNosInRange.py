def sumofprime(lower,upper):
    sum=0
    while(lower<=upper):
        flg=1
        for i in range(2,lower):
            if((lower%i==0)):
                flg=0
                break
        if (flg==1):
            sum=sum+lower
        lower+=1
    return(sum)
lower=int(input("enter lower range= "))
upper=int(input("enter upper limit= "))
total=sumofprime(lower,upper)
print("sum of prime numbers",lower,"and",upper,"is",total)