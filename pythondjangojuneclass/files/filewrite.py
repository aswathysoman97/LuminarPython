#f=open("abc.txt","w")
#f.write("hello world")
#lst=["hai","how","are","you"]
#for data in lst:
#    f.write(data)



f=open("abc.txt","r")
fw=open("evenodd.txt","w")
for data in f:
    num=int(data)
    if(num%2==0):
        fw.write(str(num)+"\n")