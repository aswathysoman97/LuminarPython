llm=int(input("enter a lower limit= "))
upl=int(input("enter a upper limit= "))
i=0
evensum=0
oddsum=0
while(llm<=upl):
    if(llm%2==0):
        evensum+=llm
    else:
        oddsum+=llm
    llm+=1
print("evensum= ",evensum)
print("oddsum= ",oddsum)
