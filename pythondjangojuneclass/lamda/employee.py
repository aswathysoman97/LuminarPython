class Employee():
    def __init__(self,id,name,desgn,salary,exp):
        self.id=id
        self.name=name
        self.desgn=desgn
        self.sal=salary
        self.exp=exp
    def printval(self):
        print("\n id:",self.id,"\n","name:",self.name,"\n","desgn:",self.desgn,"\n","salary:",self.sal,"\n","exp:",self.exp)
f=open("emp")
emp=[]
for data in f:
    val=data.rstrip("\n").split(",")
    id=val[0]
    name=val[1]
    desgn=val[2]
    salary=int(val[3])
    exp=int(val[4])
    ob=Employee(id,name,desgn,salary,exp)
    ob.printval()
    emp.append(ob)
uprcs=list(map(lambda Employee:Employee.name.upper(),emp))
print("\n")
print("<uppercase>")
print(uprcs)
salary=list(filter(lambda Employee:Employee.sal>15000,emp))
print("\n<salary>15000>")
for i in salary:
    print(i.name)
salgrowth=list(filter(lambda Employee:Employee.exp>=2,emp))
print("\n<increment of 5000 for all employee who have exp>=2>")
for j in salgrowth:
    print("name= ",j.name,"salary= ",j.sal)
    sal=j.sal+5000
    print("new salary= ",sal)
    print("\n")
print("<designation=developer>")
dsg=list(filter(lambda Employee:Employee.desgn=="developer",emp))
for k in dsg:
    print (k.name)