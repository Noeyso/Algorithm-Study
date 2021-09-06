##백준_7568

from sys import stdin
input = stdin.readline

N = int(input())

bulk=[list(map(int,input().split())) for _ in range(N)]

res=[1]*N



for i in range(N):
    w=bulk[i][0]
    h=bulk[i][1]
    for j in range(N):
        if bulk[j][0]>w and bulk[j][1]>h:
            res[i]+=1


for i in res:
    print(i,end=' ')
