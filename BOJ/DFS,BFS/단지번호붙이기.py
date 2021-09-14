##백준_2667 : 단지번호붙이기

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
board=[list(input().rstrip()) for _ in range(N)]
directions=[(0,1),(0,-1),(1,0),(-1,0)]


def dfs(y,x):
    que=deque()
    que.append((y,x))
    cnt=0
    while que:
        y,x=que.popleft()
        board[y][x]=0
        cnt+=1
        for my,mx in directions:
            move_y,move_x=y+my,x+mx
            if 0<=move_y<N and 0<=move_x<N and board[move_y][move_x]=='1':
                que.append((move_y,move_x))
                board[move_y][move_x]=0
    return cnt
    
cnt_arr=[]
for i in range(N):
    for j in range(N):
        if board[i][j]=='1':
            cnt_arr.append(dfs(i,j))

cnt_arr.sort()
print(len(cnt_arr))
for c in cnt_arr:
    print(c)
