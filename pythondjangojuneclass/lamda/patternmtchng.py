import re
# x='[a-z][369][a-z]*'
# vname=input("variable name= ")
# match=re.fullmatch(x,vname)
# if(match!=None):
#     print("valid")
# else:
#     print("invalid")

# validate vehicle registration number

x='[klKL]\d{2}[a-zA-Z]{2}\d{4}'
vname=input("variable name= ")
match=re.fullmatch(x,vname)
if(match!=None):
    print("valid")
else:
    print("invalid")
