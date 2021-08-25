## 백준_1389 : 케빈베이컨의 6단계 법칙 (bfs)
import sys
from collections import deque

def bfs(num,n):
    bacon=[0]*(n+1)
    visited=[num]
    queue=deque()
    queue.append(num)

    while queue:
        k=queue.popleft()
        for i in G[k]:
            if i not in visited:
                bacon[i]=bacon[k]+1
                visited.append(i)
                queue.append(i)
    return sum(bacon)
    

N,M=map(int,sys.stdin.readline().split())    
G=[[] for i in range(N+1)]

for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    G[x].append(y)
    G[y].append(x)

result=[]
for num in range(1,N+1):
    result.append(bfs(num,N))

print(result.index(min(result))+1)
