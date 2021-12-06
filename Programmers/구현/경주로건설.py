import sys
from collections import deque

def solution(board):
    N=len(board)
    answer=sys.maxsize
    dp=[[sys.maxsize]*N for _ in range(N)]
    
    que=deque([(0,0,-1,0)])
    while que:
        y,x,d,c=que.popleft()

        if (y,x)==(N-1,N-1) and answer>c:
            answer=c     

        directions=[(y-1,x,0),(y+1,x,1),(y,x+1,2),(y,x-1,3)]
        for ny,nx,drt in directions:
            if ny<=-1 or ny>=N or nx<=-1 or nx>=N:
                continue
            if board[ny][nx]:
                continue
            cost = c+100 if d==drt or d==-1 else c+600
            if dp[ny][nx]<cost:
                continue
            que.append((ny,nx,drt,cost))
            dp[ny][nx]=cost
            

    return answer
