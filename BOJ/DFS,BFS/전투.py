##백준_1303
from sys import stdin
from collections import deque
input = stdin.readline

N,M = map(int,input().split())
area=[list(map(str,input().rstrip())) for _ in range(M)]
visited=[[False]*N for _ in range(M)]
dirs = [(-1,0),(1,0),(0,1),(0,-1)]
w,b=0,0

def dfs(y,x,color):
    global w,b
    que=deque()
    que.append((y,x))
    visited[y][x]=True
    cnt=1
    while que:
        y,x = que.popleft()
        for dy,dx in dirs:
            move_y=y+dy
            move_x=x+dx
            if 0<=move_y<M and 0<=move_x<N and area[move_y][move_x]==color and not visited[move_y][move_x]:
                cnt+=1
                visited[move_y][move_x]=True
                que.append((move_y,move_x))
    if color=='W':
        w+=(cnt*cnt)
    else:
        b+=(cnt*cnt)

for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j,area[i][j])
    
print(w,b)
