n=int(input("number of repeation= "))
for i in range(1,n):
    m1=int(input("m1="))
    m2=int(input("m2="))
    m3=int(input("m3="))
    n1=m2+m3
    n2=m1+m3
    n3=m1+m2
    print([m1,m2,m3],"=>",[n1,n2,n3])
