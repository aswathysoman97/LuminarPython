f=open("F:\complete.csv","r")
covid={}
for data in f:
    values=data.rstrip("\n").split(",")
    statename=values[0]
    latitude=values[1]
    longitude=values[2]
    cnfrmdcs=values[3]
    death=values[4]
    cured=values[5]
    newcase=values[6]
    newdeath=values[7]
    newrecover=values[8]
    if statename not in covid:
        covid[statename]={"statename":statename,"cnfrmdcs":cnfrmdcs,"cured":cured,"death":death}
    else:
        pass
#for k,v in covid.items():
 #   print(k,"\t",v)


def getValues(**kwargs): # ** is important for passing argmnts in function
    global statename
    if "statename" in kwargs:
        statename= kwargs["statename"]
        if statename in covid:
            print("state name: ",covid[statename]["statename"])
        else:
            print("there isno employee")

    if "property" in kwargs:
        prop = kwargs["property"]
        print(covid[statename][prop])


getValues(statename="telangana", property="death")