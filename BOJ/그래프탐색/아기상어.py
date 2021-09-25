##백준_17086
from collections import deque

N,M = map(int,input().split())
board = []

moves=[(-1,-1),(-1,0),(1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1)]
que=deque()

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(M):
        if tmp[j]==1:
            que.append((i,j))
    board.append(tmp)

def bfs():
    while que:
        y,x = que.popleft()
        for my,mx in moves:
            move_y = y+my
            move_x = x+mx
            if 0<=move_y<N and 0<=move_x<M:
                if board[move_y][move_x]==0:
                    que.append((move_y,move_x))
                    board[move_y][move_x]=board[y][x]+1
    return

bfs()

res=0
for i in range(N):
    for j in range(M):
        res=max(res,board[i][j])
print(res-1)
