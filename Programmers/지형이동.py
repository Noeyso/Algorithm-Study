import heapq

def solution(land, height):
    
    N = len(land)
    visited=[[False]*N for _ in range(N)]
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    que=[(0,0,0)]

    visit_count=0
    max_count = N*N
    value = 0

    while (visit_count<max_count):
        v,y,x= heapq.heappop(que)
        if visited[y][x]:
            continue
        visited[y][x]=True

        visit_count+=1
        value+=v

        c_height = land[y][x]
        
        for dx,dy in direction:
            mx=x+dx
            my=y+dy
            
            if mx<N and mx>=0 and my<N and my>=0:
                n_height = land[my][mx]
                diff = abs(n_height-c_height)
                if diff>height:
                    heapq.heappush(que,(diff,my,mx))
                else:
                    heapq.heappush(que,(0,my,mx))
    return value
