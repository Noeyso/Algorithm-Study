## 백준_1182

from sys import stdin
input = stdin.readline

N,S =map(int,input().split())
arr=list(map(int,input().split()))
cnt=0

def dfs(idx,s):
    print("idx: ",idx,"s: ",s)
    global cnt

    if idx>=N:
        return
    s+=arr[idx]

    if s==S:
        cnt+=1
    dfs(idx+1,s)
    dfs(idx+1,s-arr[idx])

dfs(0,0)
print(cnt)
    
    
'''
from itertools import combinations
##조합을 이용한 풀이
for i in range(1,N+1):
    per = combinations(arr,i)
    print(list(per))
    for j in list(per):
        if sum(j)==S:
            cnt+=1
print(cnt)
'''
