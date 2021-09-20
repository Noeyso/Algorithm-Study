from collections import deque

MAX=10**5

N,K=map(int,input().split())
visited=[[-1,-1] for _ in range(MAX+1)]

def bfs():
    que=deque()
    que.append(N)
    visited[N][0]=1
    visited[N][1]=0
    
    while que:
        n = que.popleft()
        moves=[[n+1,1],[n-1,1],[n*2,0]]
        for mv,time in moves:
            if 0<=mv<=MAX:
                if visited[mv][0]==-1:
                    que.append(mv)
                    visited[mv][0]=1
                    visited[mv][1]=visited[n][1]+time
                else:
                    visited[mv][1]=min(visited[n][1]+time,visited[mv][1])
    print(visited[K][1])

bfs()
