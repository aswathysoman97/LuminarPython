class Employee():
    def __init__(self,id,name,desgn,salary,exp):
        self.id=id
        self.name=name
        self.desgn=desgn
        self.sal=salary
        self.exp=exp
    def printval(self):
        print("\n id:",self.id,"\n","nmae:",self.name,"\n","desgn:",self.desgn,"\n","salary:",self.sal,"\n","exp:",self.exp)
f=open("emp")
emp=[]
for data in f:
    val=data.rstrip("\n").split(",")
    id=val[0]
    name=val[1]
    desgn=val[2]
    salary=int(val[3])
    exp=val[4]
    # if(salary>17000):
    ob=Employee(id,name,desgn,salary,exp)
    ob.printval()
    emp.append(ob)
    # another method for print salary greaterthan 17000
    # emp = []              }both used for this another method
    # emp.append(ob)        }

for employ in emp:
    if(employ.sal>17000):
        print(employ.name)

for employ in emp:
    name=employ.name
    print(name.upper())