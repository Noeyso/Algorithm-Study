import heapq

def dijkstra(dist,adj):
    heap=[]
    heapq.heappush(heap,[0,1])
    while heap:
        cost,node = heapq.heappop(heap)
        for c,n in adj[node]:
            if cost+c<dist[n]:
                dist[n]=cost+c
                heapq.heappush(heap,[cost+c,n])

def solution(N, road, K):
    dist = [float('inf')]*(N+1)
    dist[1]=0
    adj = [[]for _ in range(N+1)]
    for s,e,v in road:
        adj[s].append([v,e])
        adj[e].append([v,s])
    dijkstra(dist,adj)
    return len([i for i in dist if i<=K])
