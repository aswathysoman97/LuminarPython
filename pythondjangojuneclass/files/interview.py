f=open("person.txt")
emp={}
for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    age=values[2]
    desgn=values[3]
    exp=values[4]
    salary=values[5]
    if(id not in emp):
        emp[id]={"ïd":id,"name":name,"age":age,"designation":desgn,"exp":exp,"salary":salary}
    else:
        pass
#for k,v in emp.items():
   # print(k,"\t",v)

#def printEmployee(**kwargs): #** is important for passing argmnts in function
 #   for k,v in kwargs.items():
  #      id=v
   #     if(id in emp):
    #        print(emp[id])
     #   else:
      #      print("there is no employee with id",id)
#printEmployee(id="105")



def printEmployee(**kwargs): #** is important for passing argmnts in function
    if "id" in kwargs:
        id=kwargs["id"]
        if id in emp:
            print("employee name: ",emp[id]["name"])
        else:
            print("there isno employee")

    if "property" in kwargs:
        prop=kwargs["property"]
        print(emp[id][prop])
    

printEmployee(id="104",property="age")