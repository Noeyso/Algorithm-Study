##백준_8911 : 거북이
from sys import stdin

input = stdin.readline

dx=[0,-1,0,1]
dy=[1,0,-1,0] # 북 서 남 동

T = int(input())

for _ in range(T):
    ctr = list(input().rstrip())
    move_x,move_y = 0,0
    tmp_dir =0
    res=[(move_x,move_y)]
    
    for c in ctr:
        if c=="F":
            move_x = move_x+dx[tmp_dir]
            move_y = move_y+dy[tmp_dir]
        elif c=="B":
            move_x = move_x-dx[tmp_dir]
            move_y = move_y-dy[tmp_dir]
        elif c=="L":
            if tmp_dir==3:
                tmp_dir=0
            else:
                tmp_dir+=1
        elif c=="R":
            if tmp_dir==0:
                tmp_dir=3
            else:
                tmp_dir-=1
        res.append((move_x,move_y))
    width= max(res,key=lambda x:x[0])[0] - min(res,key=lambda x:x[0])[0]
    height = max(res,key=lambda x:x[1])[1]-min(res,key=lambda x:x[1])[1]
    print(width*height)
