##백준_2805

from sys import stdin
N,M=map(int,stdin.readline().split())
trees=list(map(int,stdin.readline().split()))

start,end=1,max(trees)

while start<=end:
    mid=(start+end)//2
    tmp=0
    for i in trees:
        if i>=mid:
            tmp+= i-mid
    if tmp>=M:
        start=mid+1
    else:
        end=mid-1

print(end)
