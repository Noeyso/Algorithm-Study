def solution(dirs):
    visited=set()
    direction = {"U":[0,-1],"D":[0,1],"R":[1,0],"L":[-1,0]}
    x,y = 0,0
    
    for d in dirs:
        nx,ny = x+direction[d][0],y+direction[d][1]
        go = (x,y,nx,ny)
        back = (nx,ny,x,y)
        if -5<= nx <= 5 and -5<= ny <= 5:
            visited.add(go)
            visited.add(back)
            x=nx
            y=ny
        
    return len(visited)//2
