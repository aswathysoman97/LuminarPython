 #import matplotlib.pylot as plt
f=open("F:\complete.csv","r")
i=0
rcvddict={}
for lines in f:
    report=lines.rstrip("\n").split(",")
    state=report[1]
    rcvddcases=(report[8].split(" "))
    #print("state",state)
    #print("confirmed cases",cases)
    #print(report)
     #if(i==50):
         #breakpoint()
    if(state not in rcvddict):
        rcvddict[state]=rcvddcases
    else:
        rcvddict[state]=rcvddcases
print("total recoverd cases= ",rcvddict)
rcvdlist=[]
for k,v in rcvddict.items():
    rcvdlist.append((v,k))
sorteddata=sorted(rcvdlist,reverse=True)
print(sorteddata)
sorteddata=sorteddata[0:3]
rcvdcountlist=[]
statenameslist=[]
print("state with max rcvd cases")
for i in sorteddata:
    rcvdcountlist.append((i[0]))
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