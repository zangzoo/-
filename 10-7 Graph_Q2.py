# 도시 분할 계획

# 노드 n, 간선 m 입력받기
n,m=map(int,input().split())
# 모든 간선 담을 리스트 생성
edges=[]
# 최종 비용 담을 변수 생성
result=0
# 가장 큰 비용 담을 변수
last=0

# m 동안 길의 정보 a,b,c 입력받아 리스트에 넣기 (a,b 연결 비용 c)
for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,a,b)) #비용 순 정렬을 위해 튜플의 첫번째 원소를 c로 설정

# 간선을 비용순으로 정렬
edges.sort()

#부모테이블 생성, 자기자신으로 초기화
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

# find_union 함수 생성
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# union_parent 함수 생성
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 간선 하나씩 확인
for edge in edges:
    cost,a,b=edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        last=cost

print(result-last)