#list=[2,24,6,8,7,9]
#list.sort()
#for i in list:
 #   total=total*i
#print(list[-1])

#def mw(words):
#    # ctr=0
#    #  for word in words:
#         if len(word)>1 and word[0]==word[-1]:
#             ctr+=1
#     return ctr
# print(mw(['abc','xyz','acm','12212']))

# def list(n):
#     return n[-1]
# def srtlst(tuple):
#     return sorted(tuple,key=list)
# print(srtlst([(2,5),(1,2),(4,4),(2,3),(2,1)]))

a=[2,8,6,3,9,8,5,1,2,3]
dpitem=set()
unqitem=[]
for i in a:
    if i not in dpitem:
        unqitem.append(i)
        dpitem.add(i)
print(dpitem)
print(unqitem)

