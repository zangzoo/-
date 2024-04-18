# 커리큘럼

from collections import deque
import copy
n=int(input())
#진입차수 생성
indegree=[0]*(n+1)
#graph 생성
graph=[[] for _ in range(n+1)]
# 각 강의별 소요 시간
time=[0]*(n+1)

for i in range(1,n+1):
    test=list(map(int,input().split()))
    time[i]=test[0]
    for j in test[1:-1]:
        indegree[i]+=1
        graph[j].append(i)

# 위상정렬 함수 정의
def topology_sort():
    result=copy.deepcopy(time) #알고리즘 수행 결과 담기
    q=deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
    #큐가 빌 때까지 반복
    while q:
        now=q.popleft()
        for i in graph[now]:
            result[i]=max(result[i],result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in range(1,n+1):
        print(result[i])
topology_sort()