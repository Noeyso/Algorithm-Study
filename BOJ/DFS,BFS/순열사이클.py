##백준_10451

from sys import stdin
input = stdin.readline

T=int(input())

def dfs(idx):
    visited[idx]=True
    next=arr[idx]
    if visited[next]==False:
        dfs(next)
    
    

for i in range(T):
    cnt=0
    N=int(input())
    arr =[0]+ list(map(int,input().split()))
    visited=[False]*(N+1)
        
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            cnt+=1
    print(cnt)
