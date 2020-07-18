import re
f=open("emails")
email={}
for data in f:
    value=data.rstrip("\n").split(",")
    for val in value:
        x='[a-zA-Z0-9]\w*@gmail[.]com'
        match=re.fullmatch(x,val)
        # for m in match:
        if(match!=None):
            print("valid")
            y=match
            fw=open("validid.txt","w")
            fw.write(str(y))
        else:
            print("invalid")
