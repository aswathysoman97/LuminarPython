# lst1=[2,8,9,4,6,2,3,1]
# square=[(i**2)for i in lst1]
# print(square)

# lst1=[1,2,3]
# lst2=[4,5,6]
# for i in lst1:
#     for j in lst2:
#         print(i,j)

# lst1=[1,2,3]
# lst2=[4,5,6]
# pairs=[(i,j)for i in lst1 for j in lst2]
# print(pairs)

# lst1=[1,2,3]
# lst2=[4,5,6]
# pairs=[(i**j)for i in lst1 for j in lst2]
# print(pairs)

lst1=[2,8,9,4,6,2,3,1]
evens=[i for i in lst1 if i%2==0]
print(evens)
