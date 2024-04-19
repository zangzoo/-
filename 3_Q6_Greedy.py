# 무지의 먹방 라이브

# 회전판에 먹어야할 N개의 음식 존재 => 각 음식에는 1~N까지 번호, 각 음식 섭취에 일정 시간이 소요됨
# 음식 하나 1초, 남은 음식 그대로, 다음 음식 섭취
# 먹방 시작 k초 후, 방송 잠시 중단 => 몇 번 음식부터 섭취해야 하는지

import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같으면 -1 출력
    if sum(food_times) <= k:
        return -1
    # 시간이 작은 음식부터 뺴야 함 -> 우선순위 큐에 삽입
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호)로 넣기
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수

    # sum_value+ (현재 음식 시간 - 이전 음식 시간) * 현제 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # 현재 음식 pop하고 현재 음식의 음식 시간을 now에 넣기
        sum_value += (
                                 now - previous) * length  # 현재 음식에 필요한 시간에서 직전에 다 먹은 음식 시간 빼고 -> 남은 음식 곱해서 sum_value에 더하기 => 먹기 위해 사용한 시간 계산
        length -= 1  # 다 먹은 음식 빼기
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인해 출력
    result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준 정렬
    return result[(k - sum_value) % length][1]