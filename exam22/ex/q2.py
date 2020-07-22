import re
f=open("employee")
emp=[]
for data in f:
    val=data.rstrip("\n").split(",")
    eid=val[0]
    ename=val[1]
    edsgn=val[2]
    mailid=val[3]
    salary=val[4]
    emp.append(mailid)
print(emp)
for data in emp:
    email=data.rstrip("\n").split(",")
    print(data)
    x='[a-zA-Z]\w*@gmail[.]com'
    match=re.fullmatch(x,data)
    if (match!= None):
        print("valid")
        y=match
        fw=open("validid.txt", "w")
        fw.write(str(y))
    else:
        print("invalid")