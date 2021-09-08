##백준_2644 : bfs

N=int(input())
n1,n2=map(int,input().split())
R=int(input())

relations=[[] for _ in range(N+1)]
res=[0]*(N+1)

def bfs(start):
    queue=[]
    queue.append(start)
    visited=[False]*(N+1)
    visited[start]=True
    while queue:
        n = queue.pop(0)
        for i in relations[n]:
            if not visited[i]:
                visited[i]=True
                res[i]=res[n]+1
                queue.append(i)

for i in range(R):
    r1,r2=map(int,input().split())
    relations[r1].append(r2)
    relations[r2].append(r1)

bfs(n1)
print(res[n2] if res[n2]!=0 else -1)
