import sys

INF=sys.maxsize

def solution(n, s, a, b, fares):
    dist=[[INF]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dist[i][i]=0
    for i in range(len(fares)):
        arr=fares[i]
        dist[arr[0]][arr[1]]=arr[2]
        dist[arr[1]][arr[0]]=arr[2]

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
        
    return min([dist[i][s]+dist[i][a]+dist[i][b] for i in range(1,n+1)])
