class Bank():
    def accreate(self,acno,actype,name,balance):
        self.acno=acno
        self.actype=actype
        self.name=name
        self.balance=balance
    # def printval(self,acno,actype,name,balance):
    #     print("acno=",self.acno)
    #     print("actype=",self.actype)
    #     print("name=",self.name)
    #     print("balane=",self.balance)
    def deposit(self,dp):
        print("deposit")
        print("--------")
        self.balance+=dp
    def withdraw(self,wd):
        print("\n")
        print("withdraw")
        print("---------")
        self.balance-=wd
    def balenq(self):
        print("balance=",self.balance)

ob=Bank()
ob.accreate(11,"savings","anu",3000)
# ob.printval()
ob.deposit(20000)
ob.balenq()
ob.withdraw(2000)
ob.balenq()