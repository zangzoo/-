# 팀 결성

#n,m 입력받기
n,m=map(int,input().split())
# 부모테이블 생성
parent=[0]*(n+1)
# 부모테이블 자기자신으로 초기화
for i in range(1,n+1):
    parent[i]=i

# find_parent 함수 생성
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀적 호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# union 함수 생성
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for _ in range(m):
    check,a,b=map(int,input().split())
    if check==0:
        union_parent(parent,a,b)
    else:
        if find_parent(parent,a)==find_parent(parent,b):
            print('YES')
        else:
            print('NO')