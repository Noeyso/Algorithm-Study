##백준_17070
from collections import deque
N = int(input())
board=[list(map(int,input().split())) for _ in range(N)]    
    
answer=0
def pipe(y,x,state):
    global answer
    ## moves=[(y,x+1),(y+1,x),(y+1,x+1)]
    moves={"hori":[(y,x+1),-1,(y+1,x+1)],"verti":[(y+1,x),-1,(y+1,x+1)],"diag":[(y,x+1),(y+1,x),(y+1,x+1)]}
    if y==N-1 and x==N-1 :
        answer+=1
    if state==0:
        if x+1<N and board[y][x+1]==0: pipe(y,x+1,0)
        if x+1<N and y+1<N:
            if board[y][x+1]==0 and board[y+1][x]==0 and board[y+1][x+1]==0:
                pipe(y+1,x+1,2)
    elif state==1:
        if y+1<N and board[y+1][x]==0: pipe(y+1,x,1)
        if x+1<N and y+1<N:
            if board[y][x+1]==0 and board[y+1][x]==0 and board[y+1][x+1]==0:
                pipe(y+1,x+1,2)
    elif state==2:
        if x+1<N and board[y][x+1]==0: pipe(y,x+1,0)
        if y+1<N and board[y+1][x]==0: pipe(y+1,x,1)
        if x+1<N and y+1<N:
            if board[y][x+1]==0 and board[y+1][x]==0 and board[y+1][x+1]==0:
                pipe(y+1,x+1,2)
        

   
pipe(0,1,0)
print(answer)
