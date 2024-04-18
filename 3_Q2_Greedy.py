# 곱하기 혹은 더하기

s=input()
l=[]
for i in range(len(s)):
    l.append(int(s[i]))

l.sort()
result=1

for i in l:
    if i!=0:
        result*=i
print(result)