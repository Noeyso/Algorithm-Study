## 백준_11724 : 연결요소의개수(dfs)

N,M = map(int,input().split())

def dfs(v):
    visited[v]=True
    for e in G[v]:
        if not visited[e]:
            dfs(e)
    

G=[[]for i in range(N+1)]
for i in range(M):
    v1,v2 = map(int,input().split())
    G[v1].append(v2)
    G[v2].append(v1)

visited=[False]*(N+1)
cnt=0

for v in range(1,N+1):
    if not visited[v]:
        cnt+=1
        dfs(v)

print(cnt)
