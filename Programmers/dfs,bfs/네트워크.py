from collections import deque

def network(i,j,n,computers):
    visited=set()

    que=deque()
    que.append((i,j))

    while que:
        start,end=que.popleft()
        visited.add(end)
        for k in range(n):
            if computers[end][k]==1:
                if k not in visited:
                    que.append((end,k))
                computers[end][k]=0

        
def solution(n, computers):
    answer=0
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                network(i,j,n,computers)
                answer+=1

    return answer


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
