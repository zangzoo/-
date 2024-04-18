# 문자열 뒤집기

s=input()
cnt_0=0
cnt_1=0

for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        if s[i]=='0':
            cnt_0+=1
        else:
            cnt_1+=1
# if cnt_0>=cnt_1:
#     print(cnt_1)
#
#
# else:
#     print(cnt_0)
print(min(cnt_0,cnt_1))