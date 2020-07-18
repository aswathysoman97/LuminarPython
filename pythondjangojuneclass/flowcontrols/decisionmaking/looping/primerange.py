llm=int(input("enter lowerlimit= "))
ulm=int(input("enter upperlimit= "))
flg=0
for i in range(llm,ulm):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                flg=1
                break
            else:
                #print(i)
                pass
    if(flg>0):
        pass
    else:
        print(i)
        #pass