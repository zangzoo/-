#효율적인 화폐 구성
n,m=map(int,input().split())

#n개의 화폐단위 정보 입력받기_
array=[]
for i in range(n):
    array.append(int(input()))

#dp 테이블 초기화(가치의 합이 인덱스)
d=[10001]*(m+1)

#다이나믹 프로그래밍(바텀업)
d[0]=0
for i in range(n): #n번 반복 => 화폐별로 한번씩
    for j in range(array[i],m+1): #한 화폐일때, 가치값을 만드는 방법 계산을 위해
        if d[j-array[i]]!=10001: #(i-k)원을 만드는 방법이 존재하는 경우
            d[j]=min(d[j],d[j-array[i]]+1)
#계산된 결과 출력
if d[m]==10001:
    print(-1)
else:
    print(d[m])