import heapq

def dijkstra(dis,adj):
    heap=[]
    heapq.heappush(heap,[0,1])

    while heap:
        value,node=heapq.heappop(heap)
        for v,n in adj[node]:
            if value+v<dis[n]:
                dis[n]=value+v
                heapq.heappush(heap,[value+v,n])
    


def solution(N, road, K):
    INF=float('inf')
    dis = [INF]*(N+1)
    dis[1]=0
    adj = [[] for _ in range(N+1)]
    for r in road:
        adj[r[0]].append([r[2],r[1]])
        adj[r[1]].append([r[2],r[0]])
    dijkstra(dis,adj)
    
    return len([x for x in dis if x<=K])

