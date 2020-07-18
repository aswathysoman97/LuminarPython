name=input("enter name= ")
a=int(input("mark1= "))
b=int(input("mark2= "))
c=int(input("mark3= "))
total=a+b+c
print("total= ",total)
if(total>145):
    print("A+")
elif(total>140)&(total<=145):
    print("A")
elif(total>135)&(total<=140):
    print("B+")
elif(total>130)&(total<=135):
    print("B")
elif(total<=130):
    print("FAILD")
else:
    print("INVALID")