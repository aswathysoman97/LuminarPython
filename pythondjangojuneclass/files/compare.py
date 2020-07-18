f=open("names.txt","r")
fr=open("passed.txt","r")
fw=open("failed.txt","w")
#for data in f:
  #  if(data not in fr):
   #     fw.write(data)
#st1=set()
#st2=set()
def readfromline(fref):
    st=set()
    for data in fref:
        data=data.rstrip("\n")
        st.add(data)
    return(st)
st1=readfromline(f)
st2=readfromline(fr)
print(st1)
print(st2)
fail=st1-st2
print(fail)

