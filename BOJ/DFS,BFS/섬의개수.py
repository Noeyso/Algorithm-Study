##백준_4963


w,h=-1,-1
directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def dfs(i,j):
    visited[i][j]=True
    queue=[]
    queue.append((i,j))
    while queue:
        y,x=queue.pop(0)
        for dy,dx in directions:
            move_y,move_x=y+dy,x+dx
            if 0<=move_y<h and 0<=move_x<w and board[move_y][move_x]==1 and not visited[move_y][move_x]:
                visited[move_y][move_x]=True
                queue.append((move_y,move_x))
    
while True:
    board=[]
    w,h=map(int,input().split())
    visited=[[False]*w for _ in range(h)]
    cnt=0
    
    if w==0 and h==0:
        break
    for i in range(h):
        board.append(list(map(int,input().split())))

    for i in range(h):
        for j in range(w):
            if board[i][j]==1 and not visited[i][j]:
                dfs(i,j)
                cnt+=1

    print(cnt)
