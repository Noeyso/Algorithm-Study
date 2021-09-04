##백준_10026

from sys import stdin
from collections import deque

input=stdin.readline

N=int(input())

grid=[list(input().rstrip()) for _ in range(N)]
visited=[[False]*N for _ in range(N)]


direction=[(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x,y,color):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        visited[x][y]=True

        for move in direction:
            move_y,move_x = y+move[0],x+move[1]

            if 0<=move_y<N and 0<=move_x<N and grid[move_x][move_y]==color and not visited[move_x][move_y]:
                queue.append((move_x,move_y))
                visited[move_x][move_y]=True
                
cnt=0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j,grid[i][j])
            cnt+=1
        if grid[i][j]=='R':
            grid[i][j]='G'
            
print(cnt,end=' ')

cnt=0
visited=[[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j,grid[i][j])
            cnt+=1
print(cnt)
