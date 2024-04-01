# 기본적인 서로소 집합 알고리즘

#특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x: # x의 루트 노드가 x의 부모노드인 parent[x]가 아닐때
        return find_parent(parent,parent[x]) # parent[x]에서 부모노드 호출 => 재귀적으로 실행 부모노드가 루트노드일 때까지
    return x

#두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a) # a의 부모노드
    b=find_parent(parent,b) # b의 부모노드
    if a<b: # a의 부모노드 값이 더 작으면
        parent[b]=a # b가 a를 가리킴 = b의 부모가 a가 됨 => b의 부모노드 값이 a의 부모노드 값이 됨
    else:
        parent[a]=b

# 노드의 개수와 간선(=union 연산)의 개수 입력받기
v,e=map(int,input().split())
parent=[0]*(v+1) #부모 테이블 초기화 => 1부터 시작하니까 v+1 개 생성

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

# union 연산을 각각 수행
for i in range(e): #union 연산 개수 만큼 노드들 입력받기
    a,b=map(int,input().split())
    union_parent(parent,a,b) #입력받은 a,b 합치기 => 부모노드 또한 달라지겠지

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ',end='')
for i in range(1,v+1):
    print(find_parent(parent,i),end=' ') #루트 노드 출력

print() # 줄 바꾸기

# 부모 테이블 내용 출력
print('부모 테이블: ',end='')
for i in range(1,v+1):
    print(parent[i],end=' ') #부모 테이블 출력