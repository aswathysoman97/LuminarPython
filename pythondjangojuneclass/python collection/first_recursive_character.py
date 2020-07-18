str=input("enter string to find first recursing character= ")
letter=list(str)
print (letter)
dict={}
for let in letter:
    if(let not in dict):
        dict[let]=1
    else:
        print("first recursing characher= ",let)
        break