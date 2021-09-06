##백준_2606

C = int(input())
P = int(input())

network=[list(map(int,input().split())) for _ in range(P)]
virus=[False]*(C+1)


def dfs(node):
    virus[node]=True
    for x,y in network:
        if virus[x] and virus[y]:
            continue
        if virus[x]:
            dfs(y)
        if virus[y]:
            dfs(x)

dfs(1)
print(virus.count(True)-1)
