from collections import deque
    
def solution(maps):
    answer = 0
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    n=len(maps)
    m=len(maps[0])


    graph=[[-1 for _ in range(m)] for _ in range(n)]
    
    que=deque([(0,0)])
    graph[0][0]=1
    
    while que:
        y,x=que.popleft()

        for dx,dy in directions:
            nx=x+dx
            ny=y+dy

            if 0<=ny<n and 0<=nx<m and maps[ny][nx]==1:
                if graph[ny][nx]==-1:
                    graph[ny][nx]=graph[y][x]+1
                    que.append([ny,nx])
            
    return graph[-1][-1]
