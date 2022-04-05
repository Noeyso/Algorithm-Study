N = int(input())

x,y= 0,0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
direction=0
turnCnt=0

board = [[0]*N for _ in range(N)]
board[y][x]=1

while turnCnt<2:

    nextTwoY =y+dy[direction]*2
    nextTwoX = x+dx[direction]*2
    if not (nextTwoY<0 or nextTwoY>N-1 or nextTwoX<0 or nextTwoX>N-1) and board[nextTwoY][nextTwoX]==1:
        direction = (direction+1)%4
        turnCnt+=1
        continue

    nextOneY =y+dy[direction]
    nextOneX = x+dx[direction]

    if nextOneY<0 or nextOneY>N-1 or nextOneX<0 or nextOneX>N-1 :
        direction = (direction+1)%4
        turnCnt+=1
        continue

    if direction==0:
        x+=1
    elif direction==1:
        y+=1
    elif direction==2:
        x-=1
    elif direction==3:
        y-=1

    board[y][x]=1
    turnCnt=0


for arr in board:
    for i in arr:
        if i==1:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()
