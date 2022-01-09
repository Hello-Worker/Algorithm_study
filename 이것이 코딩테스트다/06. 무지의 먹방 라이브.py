# 회전판에 먹어야 할 N개의 음식
# 음식에는 1번부터 N개의 번호표
# 무지는 1번부터 먹기 시작하며 회전판은 번호가 증가하는 순서대로 무지 앞에 갖다줌
# 마지막 번호를 섭취하면 1번이 다시 옴
# 무지는 음식 하나를 1초동안 섭취 후 남은 음식을 그대로 두고, 다음 음식을 섭취
# 회전판이 음식을 주는 시간은 없다고 가정
# K초 후에 네트워크 중단. 다시 방송을 이어갈 때 몇번부터 먹어야 하는지 알고자 한다.
# 각 음식을 먹는데 필요한 시간이 담겨져있는 배열 food_time, K초가 매개변수로 주어질 때 몇 번부터 다시 섭취하면 되는지 return하도록 solution 함수 완성하라

import heapq
def solution(food_times, k):
    answer = 0
    time = 0
    pq = []
    answer_rs = []
    # 1. 우선순위 큐에 (food_times, 음식 번호) 순으로 담는다.
    for i in range(len(food_times)):
        heapq.heappush(pq, [food_times[i], i + 1])

    pre_food = 0
    flag = True
    while flag:
        if not pq:
            return -1
        length = len(pq)
        time += (pq[0][0] - pre_food) * length
        if time > k:
            time -= (pq[0][0] - pre_food) * length
            while pq:
                answer_rs.append(heapq.heappop(pq)[1])
            answer_rs.sort()
            answer = answer_rs[(k - time) % length]
            flag = False
        else:
            pre_food = heapq.heappop(pq)[0]
    return answer
