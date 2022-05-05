from collections import deque
def solution(board):
    answer=-1
    N = len(board[0])
    visited=[[-1]*N for _ in range(N)]
    
    que=deque([(0,0,-1,0)])
    move = [(-1,0,0),(1,0,1),(0,-1,2),(0,1,3)]
    
    while que:
        y,x,d,c = que.popleft()
        if y==N-1 and x==N-1 and (answer>c or answer==-1):
            answer=c
        
        for my,mx,drt in move:
            ny=y+my
            nx=x+mx
            if ny>N-1 or ny<0 or nx>N-1 or nx<0:
                continue
            if board[ny][nx]==1:
                continue
            cost = c
            if d==drt or d==-1:
                cost+=100
            else:
                cost+=600
            
            if visited[ny][nx]!=-1 and visited[ny][nx]<cost:
                continue
            que.append((ny,nx,drt,cost))
            visited[ny][nx]=cost
    return answer
