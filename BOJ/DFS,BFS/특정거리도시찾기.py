## 백준_18352

from sys import stdin
from collections import deque
input = stdin.readline
N,M,K,X=map(int,input().rsplit())

roads=[[] for _ in range(N+1)]
for i in range(M):
    s,e = map(int,input().split())
    roads[s].append(e)
        
visited=[-1]*(N+1)
visited[X]=0

queue=deque([X])
while queue:
    q = queue.popleft()
    for i in roads[q]:
        if visited[i]==-1:
            visited[i]=visited[q]+1
            queue.append(i)
for i in range(N+1):
    if visited[i]==K:
        print(i)
if K not in visited:
    print(-1)
