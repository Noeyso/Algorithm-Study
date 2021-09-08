## 백준_16948

N=int(input())


directions=[(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]
def bfs(r1,c1,r2,c2):
    visited=[[-1]*N for _ in range(N)]
    visited[r1][c1]=1
    queue=[]
    queue.append((r1,c1))
    
    while queue:
        x,y=queue.pop(0)
        for dx,dy in directions:
            move_x,move_y = x+dx,y+dy
            if move_x==r2 and move_y==c2:
                print(visited[x][y])
                return 
            if 0<=move_x<N and 0<=move_y<N and visited[move_x][move_y]==-1:
                    visited[move_x][move_y]=visited[x][y]+1
                    queue.append((move_x,move_y))
    print(visited[r2][c2])
    return
    



r1,c1,r2,c2 = map(int,input().split())
bfs(r1,c1,r2,c2)

