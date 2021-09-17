##백준_12851 : 숨바꼭질2

from collections import deque

MAX=10**5
N,K = map(int,input().split())
visited=[[-1,0] for _ in range(MAX+1)]


def bfs():
    que=deque()
    que.append(N)
    visited[N][0]=0
    visited[N][1]=1
    
    while que:
        n = que.popleft()
        moves=[n+1,n-1,n*2]
        for m in moves:
            if 0<=m<=MAX:
                if visited[m][0]==-1:
                    que.append(m)
                    visited[m][0]=visited[n][0]+1
                    visited[m][1]=visited[n][1]
                elif visited[m][0]==visited[n][0]+1:
                    visited[m][1]+=visited[n][1]
    print(visited[K][0])
    print(visited[K][1])
            
bfs()
