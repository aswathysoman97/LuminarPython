# pattern matching
import re
# matcher=re.finditer("ab","abababababbbaaa")
# count=0
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     count+=1
# print(count)

# x='[abc]'
# x='[a-z]'
# x='[a-zA-Z]'
# x='[1-9]'
# matcher=re.finditer(x,"a2bb@7%$_ kz9")
# count=0
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     count+=1
# print(count)


# x='[^a-zA-Z1-9]'
# matcher=re.finditer(x,"a2bb@7%$_ kz9")
# count=0
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     count+=1
# print(count)

# predefind characters
# x='\s'
# x='\d'
# matcher=re.finditer(x,"a2bb@7%$_ kz9")
# count=0
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     count+=1
# print(count)

# quantifiers
# x='a+'
# x='a*'
# x='a?'
# x='{2}'
x='a{2}'
# x='a{2,3}'
matcher=re.finditer(x,"aaaabbaaaabbaaaabaa")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
