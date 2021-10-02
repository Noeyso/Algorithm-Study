from collections import deque

def solution(numbers, target):
    answer = 0
    que=deque()
    que.append((0,0))
    while que:
        current_sum,idx=que.popleft()

        if idx==len(numbers):
            if current_sum==target:
                answer+=1
        else:
            num = numbers[idx]
            que.append((current_sum+num,idx+1))
            que.append((current_sum-num,idx+1))

    return answer
