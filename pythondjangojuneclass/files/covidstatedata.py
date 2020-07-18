  #import matplotlib.pylot as plt
f=open("F:\complete.csv","r")
i=0
cnfrmddict={}
for lines in f:
    report=lines.rstrip("\n").split(",")
    state=report[1]
    cnfrmdcases=(report[4])
    #print("state",state)
    #print("confirmed cases",cases)
    #print(report)
     #if(i==50):
         #breakpoint()
    if(state not in cnfrmddict):
        cnfrmddict[state]=cnfrmdcases
    else:
        cnfrmddict[state]=cnfrmddcases
print("total confirmed cases= ",cnfrmddict)
cnfrmdlist=[]
for k,v in cnfrmddict.items():
    cnfrmdlist.append((v,k))
sorteddata=sorted(cnfrmdlist,reverse=True)
print(sorteddata)
sorteddata=sorteddata[0:3]
cnfrmddcountlist=[]
statenameslist=[]
print("state with max rcvd cases")
for i in sorteddata:
    cnfrmdcountlist.append((i[0]))
    statenameslist.append((i[1]))
    print(i[1],"---->",i[0])



#states=[]
#cnt=[]
#for k,v in dict.items():
 #   states.append(k)
  #  cnt.appendI(v)
#plt.bar(states,cnt)
#plt.ylabel('somenumbers')
#plt.show