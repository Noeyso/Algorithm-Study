##백준_2178 : 미로탐색

from sys import stdin
input=stdin.readline

N,M = map(int,input().split())
board=[list(input().rstrip()) for _ in range(N)]
visited=[[0]*M for _ in range(N)]

directions=[(0,1),(1,0),(-1,0),(0,-1)]
def dfs():
    queue=[(0,0)]
    visited[0][0]+=1
    
    while queue:
        y,x=queue.pop(0)

        for my,mx in directions:
            move_y=y+my
            move_x=x+mx
            if 0<=move_y<N and 0<=move_x<M and board[move_y][move_x]=='1':
                if visited[move_y][move_x]==0:
                    visited[move_y][move_x]=visited[y][x]+1
                    queue.append((move_y,move_x))
                else:
                    if visited[move_y][move_x]>visited[y][x]+1:
                        visited[move_y][move_x]=visited[y][x]+1
                        queue.append((move_y,move_x))
                    
                
        
dfs()
print(visited[N-1][M-1])
