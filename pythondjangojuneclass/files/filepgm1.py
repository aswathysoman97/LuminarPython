f=open("C:/Users/chakkara/PycharmProjects/pythondjangojuneclass/files/names.py","r")
dict={}
for line in f:
    print(line)
    words=line.rstrip("\n").split(" ")
    print(words)
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,"=",v)
  