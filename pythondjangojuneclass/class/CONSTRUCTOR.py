class Student:
    def __init__(self,name,roll,course):
        self.name=name
        self.roll=roll
        self.course=course
    def printval(self):
        print(self.name,",",self.roll,",",self.course)
ob=Student("anu",12,"cs")

ob.printval()

