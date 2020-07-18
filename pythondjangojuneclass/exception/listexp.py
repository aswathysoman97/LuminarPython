lst=[2,5,8,6,]
i=int(input("index"))
try:
    print(lst[i])
# except:
#     print("error")
except Exception as f:
    print(f.args)