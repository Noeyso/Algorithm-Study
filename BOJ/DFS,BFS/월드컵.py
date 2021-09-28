##백준_6987

from itertools import combinations
from sys import stdin
input = stdin.readline

def dfs(cnt):
    global res,win,same,lose
    if cnt==15:
        if win.count(0)==6 and lose.count(0)==6 and same.count(0)==6:
            res=1
        return
    x1,x2=game[cnt]
    if win[x1]>0 and lose[x2]>0:
        win[x1]-=1
        lose[x2]-=1
        dfs(cnt+1)
        win[x1]+=1
        lose[x2]+=1
    if win[x2]>0 and lose[x1]>0:
        win[x2]-=1
        lose[x1]-=1
        dfs(cnt+1)
        win[x2]+=1
        lose[x1]+=1
    if same[x1]>0 and same[x2]>0:
        same[x1]-=1
        same[x2]-=1
        dfs(cnt+1)
        same[x1]+=1
        same[x2]+=1
        
        
game = list(combinations(range(6), 2))
result=[]
for _ in range(4):
    arr=list(map(int,input().split()))
    win,same,lose=[],[],[]
    for i in range(18):
        if i%3==0: win.append(arr[i])
        elif i%3==1: same.append(arr[i])
        elif i%3==2: lose.append(arr[i])
    res=0
    dfs(0)
    result.append(res)

print(*result)
            
