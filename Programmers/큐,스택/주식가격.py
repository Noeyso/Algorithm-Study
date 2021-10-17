from collections import deque

def solution(prices):
    answer=[0]*len(prices)
    que = deque(prices)
    idx=0
    while que:
        n = que.popleft()
        for i in que:
            answer[idx]+=1
            if i < n:
                break
        idx+=1   
                
    return answer

print(solution([1, 2, 3, 2, 3]))
