##백준_1697 : 숨바꼭질
from collections import deque

N,K = map(int,input().split())
MAX=10**5
visited=[0]*(MAX+1)

def bfs():
    que=deque()
    que.append(N)

    while que:
        n = que.popleft()
        if n==K:
            print(visited[n])
            break
        moves=[n+1,n-1,n*2]
        for mv in moves:
            if 0<=mv<=MAX and not visited[mv]:
                que.append(mv)
                visited[mv]=visited[n]+1
                

bfs()
