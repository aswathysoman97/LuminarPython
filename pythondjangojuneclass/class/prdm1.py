class Employee():
    def setvalues(self,id,name,desgn,cname):
        self.id=id
        self.name=name
        self.desgn=desgn
        self.cname=cname
    def printval(self):
        print("\n eid:",self.id,"\n","enmae:",self.name,"\n","desgn:",self.desgn,"\n","cname:",self.cname,"\n")
ob=Employee()
ob.setvalues(11,"siva","manager","blossom")
ob.printval()