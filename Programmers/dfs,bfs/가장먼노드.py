def solution(n, edge):
    di={}
    visited=[0]*(n+1)
    for i in range(1,n+1):
        di[i]=[]
        
    for i in range(len(edge)):
        di[edge[i][0]].append(edge[i][1])
        di[edge[i][1]].append(edge[i][0])

    que=[1]
    while que:
        n = que.pop(0)
        for i in di[n]:
            if visited[i]==0:
                visited[i]=visited[n]+1
                que.append(i)
    visited[1]=0
    
    return visited.count(max(visited))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
