class Student:
    def __init__(self,rollno,name,course,tmark):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.tmark=tmark
    def printval(self):
        print("rollno:",self.rollno,"\n","name:",self.name,"\n","course:",self.course,"\n","total mark:",self.tmark)
f=open("studdata")
student=[]
for data in f:
    val=data.rstrip("\n").split(",")
    rollno=val[0]
    name=val[1]
    course=val[2]
    tmark=int(val[3])
    ob=Student(rollno,name,course,tmark)
    ob.printval()
    student.append(ob)
print("\n")
for stud in student:
    print(stud.name.upper())
     # print(name.upper())

print("\n")
fw=open("winner.txt","w")
for stud in student:
    if(stud.tmark>460):
        fw.write(stud.name+"\t"+stud.course+"\n")
        # print(stud.name,":",stud.tmark)


