class Employee:
    def __init__(self,eid,ename,edsgn,mailid,salary):
        self.eid=eid
        self.ename=ename
        self.edsgn=edsgn
        self.mailid=mailid
        self.salary=salary
    def printval(self):
        print("\n eid:", self.eid, "\n", "ename:", self.ename, "\n", "edsgn:", self.edsgn, "\n", "mailid:", self.mailid, "\n",
              "salary:", self.salary)

f=open("employee")
emp=[]
for data in f:
    val=data.rstrip("\n").split(",")
    eid=val[0]
    ename=val[1]
    edsgn=val[2]
    mailid=val[3]
    salary=val[4]
    ob=Employee(eid,ename,edsgn,mailid,salary)
    ob.printval()
    emp.append(ob)

for e in emp:
    lst=[]
    sal=e.salary
    lst.append(sal)
print("maximum salary=",max(lst))
