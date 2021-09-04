##백준_1012

from sys import stdin
from collections import deque

input = stdin.readline

T = int(input())

directions = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(y,x):
    queue= deque()
    queue.append((y,x))

    while queue:
        y,x = queue.popleft()
        ground[y][x]=0

        for move in directions:
            move_y,move_x = y+move[0],x+move[1]

            if 0<=move_y<N and 0<=move_x<M and ground[move_y][move_x]==1:
                queue.append((move_y,move_x))
                ground[move_y][move_x]=0


for i in range(T):
    M,N,K = map(int,input().split())
    ground=[[0]*M for i in range(N)]
    cnt=0

    for i in range(K):
        x,y = map(int,input().split())
        ground[y][x]=1

    for m in range(M):
        for n in range(N):
            if ground[n][m]==1:
                dfs(n,m)
                cnt+=1
    print(cnt)
    
