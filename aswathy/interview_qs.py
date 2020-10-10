# def pattern(string):
#     dict={}
#     lst=[]
#     for i in string:
#         if i in dict:
#             dict[i]+=1
#         else:
#             dict[i]=1
#
#     print(dict)
#     s=(str(dict))
#     print(s)
#     for k,v in dict.items():
#         lst.append((v,k))
#     print(lst)
#     print(str(lst))
#     res = str(lst).strip('[]')
#     res1 = str(res).strip(',')
#     print(res1)
# pattern("HHHPPSAAA")



def pattern_count(mystring):
    dict= {}
    lst=[]
    for w in mystring:
        dict[w] = mystring.count(w)
    for k in dict:
        p = (str(dict[k]) + k)
        lst.append(p)
    res=(str(lst).strip('[]'))
    print(res)
mystring='HHHPPSAAA'
pattern_count(mystring)