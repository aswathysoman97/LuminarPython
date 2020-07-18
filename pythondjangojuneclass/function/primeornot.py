def prime(n):
    flg=0
    for i in range(2,n):
        if(n%i==0):
            flg=1
            break
    if(flg==0):
        print("number is prime")
    else:
        print("number is not prime")
num=int(input("enter no to be checked= "))
prime(num)