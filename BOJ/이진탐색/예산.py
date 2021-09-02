## 백준_2512 

import sys
input = sys.stdin.readline

N=int(input())
budget=list(map(int,input().rsplit()))
M=int(input())
s=0
e=max(budget)

def calSum(n):
    total=0
    for i in budget:
        if i>n:
            total+=n
        else:
            total+=i
    return total

tmp=0
while s<=e:
    mid=(s+e)//2

    if calSum(mid)>M:
        e=mid-1
    else:
        if mid>=tmp:
            tmp=mid
        s=mid+1

print(tmp)
