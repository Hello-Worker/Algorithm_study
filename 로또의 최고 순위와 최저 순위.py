# lottos = [44,1,0,0,31,25], win_nums = [31,10,45,1,6,19]
def solution(lottos, win_nums):
    answer = [0,0]
    rank = [6,6,5,4,3,2,1]
    
    cnt = 0
    cntz = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
        
    answer[0],answer[1] = rank[cnt+cntz],rank[cnt]
    
    return answer