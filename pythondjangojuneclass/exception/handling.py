n1=int(input("n1="))
n2=int(input("n2="))
try:
    res=n1/n2
    print(res)
# except:
#     print("<zero division error>")
except Exception as f:
    print(f.args)
    n2 = int(input("another n2="))
    res = n1 / n2
    print(res)
finally:
    print("exception is abnormal situation")
    print("program terminate the execution")