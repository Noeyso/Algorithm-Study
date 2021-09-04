##백준_1058 : 플로이드

N = int(input())

net=[]
visited=[]

for i in range(N):
    net.append(list(input()))
    visited.append([0]*N)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            if net[i][j]=='Y'or(net[i][k]=='Y' and net[k][j]=='Y'):
                visited[i][j]=1
result=0
for i in range(N):
    cnt=0
    for j in range(N):
        if visited[i][j]==1:
            cnt+=1
    result = max(result,cnt)
print(result)
