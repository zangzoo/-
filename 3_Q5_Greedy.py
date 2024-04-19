# 볼링공 고르기

n,m=map(int,input().split())
weight=list(map(int,input().split()))
cnt=0

for i in range(len(weight)-1):
    for j in range(i+1,len(weight)):
        if weight[i]==weight[j]:
            pass
        else:
            cnt+=1

print(cnt)

# -----------------------------------------------
# 답지 풀이

n,m=map(int,input().split())
weight=list(map(int,input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array=[0]*11

for x in weight:
    # 각 무게에 해당하는 볼링공 개수 카운트
    array[x]+=1

result=0
# 1부터 m까지의 각 무게에 대해 처리
for i in range(1,m+1):
    n-=array[i] # 무게가 i인 볼링공의 개수 제외 => 자신과 다른 무게의 볼링공만 남기기
    result+=array[i]*n # 경우의 수 계산

print(result)