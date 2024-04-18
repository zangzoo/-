# 모험가 길드

n=int(input())
scares=list(map(int,input().split()))

count=0
result=0
scares.sort()

for scare in scares:
    count += 1  # 그룹인원 추가
    if count >= scare:  # 인원의 공포도가 그룹의 인원수보다 적으면,
        result += 1  # 그룹을 형성한다.
        count = 0  # 인원수를 다시 초기화 한다.

print(result)