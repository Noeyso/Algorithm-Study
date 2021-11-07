from collections import deque

move_x=[1,0,-1,0]
move_y=[0,-1,0,1]

def bfs(arr,x,y):
    visited=[[0]*5 for _ in range(5)]
    que = deque()
    que.append([x,y,0])
    visited[x][y]=1

    while que:
        x,y,w=que.popleft()

        if 1<=w<=2 and arr[x][y]=="P":
            return False
        if w>=3:
            break
        for m in range(4):
            mx,my,mdir=x+move_x[m],y+move_y[m],w+1
            if 0<=mx<5 and 0<=my<5:
                if arr[mx][my] !="X" and visited[mx][my]==0:
                    que.append([mx,my,mdir])
                    visited[mx][my]=1
    return True

def solution(places):
    answer = []
    for place in places:
        isok=True
        for r in range(5):
            for c in range(5):
                if place[r][c]=='P':
                    if bfs(place,r,c)==False:
                        isok=False
                        break
            if not isok:
                break
        if isok:
            answer.append(1)
        else:
            answer.append(0)
                                     
    return answer
